
# This file is part of the PicoSplit-Keyboard project, http://kaenner.de/PicoSplit.html/
# 
# The MIT License (MIT)
# 
# Copyright (c) 2021 Andreas Känner
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from .split_keypad import SplitKeypad
from .pico_keyboard import *
from adafruit_hid.keycode import Keycode

class ConfigLoader:

  def __init__(self, configFilePath):
    self.configFilePath = configFilePath
    self.keyboardProperties = {}
    self.layout = {}
    self.layers = []

  def isFloat(self, value):
    try:
      num = float(value)
      return True, num
    except ValueError:
      return False, None

  def parse_key_value(self, text, separator='='):
    parts = [part.strip() for part in text.split(separator)]
    if len(parts) == 2:
        value = parts[1]
        isnum, num = self.isFloat(value)
        if isnum:
          value = num
        return parts[0], value
    return None, None
    
  def readlines_until_empty_line(self, file, handler):
    line = file.readline()
    while line and line.strip() != '':
      if not line.startswith('//') and line.find('`') == -1:
        handler(line)
      line = file.readline()
    
  def parse_keyboard(self, file):
    def handler(line):
      key, value = self.parse_key_value(line)
      if key:
        self.keyboardProperties[key] = value
    self.readlines_until_empty_line(file, handler)
    
  def parse_layout(self, file):
    def handler(line):
      key, value = self.parse_key_value(line)
      if key:
        self.layout[key] = value
    self.readlines_until_empty_line(file, handler)
    
  def text_between(self, text, opening, closing):
    opening_bracket_index = text.find(opening)
    closing_bracket_index = text.rfind(closing)
    if opening_bracket_index == -1 or closing_bracket_index == -1 or closing_bracket_index <= opening_bracket_index:
      return None
    return text[opening_bracket_index+1:closing_bracket_index].strip()
    
  def parse_codes_action(self, text):
    text = self.text_between(text, '[', ']')
    if not text:
      return None
    raw_codes = [part.strip() for part in text.split(',')]
    codes = []
    for raw_code in raw_codes:
      code = getattr(Keycode, raw_code, None)
      if code != None:
        codes.append(code)
    return EmitKeyCodes(codes)
  
  # Sequence[Codes[ LEFT_ALT, U ]; Codes[ A ]]
  # keep it simple without nestable sequences
  def parse_sequence_action(self, text):
    text = self.text_between(text, '[', ']')
    if not text:
      return None
    raw_sequences = [part.strip() for part in text.split(';')]
    sequence = []
    for raw_sequence in raw_sequences:
      action = self.parse_action(raw_sequence)
      if action:
        sequence.append(action)
    return EmitSequence(sequence) 
    
  def parse_change_layer_action(self, text):
    layer_name = self.text_between(text, '(', ')')
    if not layer_name:
      return None
    return ChangeLayer(layer_name)

  def parse_reset_keyboard_action(self, text):
    return ResetKeyboard()
    
  def parse_action(self, text):
    if text == 'Shift':
      return Autoshift()
    elif text.startswith('Codes'):
      return self.parse_codes_action(text)
    elif text.startswith('Sequence'):
      return self.parse_sequence_action(text)
    elif text.startswith('ChangeLayer'):
      return self.parse_change_layer_action(text)
    elif text.startswith('ResetKeyboard'):
      return self.parse_reset_keyboard_action(text)
      
  def parse_key(self, line):
    parts = [part.strip() for part in line.split(':')]
    part_count = len(parts)
    isnum, num = self.isFloat(parts[0])
    tap = None
    long_tap = None
    hold = None
    if not isnum or part_count < 2:
      return None, None, None, None
    for i in range(1, part_count):
      property, value = self.parse_key_value(parts[i])
      action = self.parse_action(value)
      if action:
        if property == 'tap':
          tap = action
        if property == 'long_tap':
          long_tap = action
        if property == 'hold':
          hold = action
          
    num = int(num)
    mappedNum = self.keyMapping.get(num)
    if mappedNum != None:
      num = mappedNum 
    return num, tap, long_tap, hold
    
  def parse_layer(self, file):
    properties = {'keys':{}}
    def handler(line):
      if ':' in line:
          num, tap, long_tap, hold = self.parse_key(line)
          if num != None:
            properties['keys'][num] = Key(tap, long_tap, hold)
      else:
        key, value = self.parse_key_value(line)
        if key:
          properties[key] = value 

    self.readlines_until_empty_line(file, handler)
    self.layers.append(Layer(properties['name'], properties['keys'])) 

  # Returns a dictionary. The keys are virtual key numbers and the values are hardware key numbers.
  # The keyboard layout is always described by using the virtual key numbers.    
  def hwMapping(self):
    mapping = {}
    try:
      with open('mapping.js', 'r') as file:
        line = file.readline()
        while line:
          stripped = line.strip()
          if stripped != '' and stripped.find('`') == -1:
            key, value = self.parse_key_value(line, ',')
            if key:
              mapping[int(key)] = int(value)
          line = file.readline()
    finally:
      return mapping

  # Returns a configured PicoKeyboard object
  def keyboard(self, keypad):
    data = {}  
    self.keyMapping = self.hwMapping()
    with open(self.configFilePath, 'r') as file:
      line = file.readline()
      while line:
        stripped = line.strip()
        if stripped != '' and not line.startswith('//') and stripped.find('`') == -1:
          method_name = "parse_" + stripped
          do = f"{method_name}"
          if hasattr(self, do):
            getattr(self, do)(file)
        line = file.readline()

    return PicoKeyboard(keypad=keypad, 
                        tap_timeout=self.keyboardProperties['tap_timeout'], 
                        long_tap_timeout=self.keyboardProperties['long_tap_timeout'], 
                        layout=Layout(self.layout['name'], self.layers),
                        emitHardwareKeyNumbers=not bool(self.keyMapping))

