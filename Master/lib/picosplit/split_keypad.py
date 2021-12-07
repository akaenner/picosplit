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

import board
import busio
from adafruit_binascii import hexlify, unhexlify, a2b_base64, b2a_base64
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
from .keypad import Keypad
import keypad

class SplitKeypad(Keypad):
    """
    Subclass of Keypad to be used with the PicoSplit-Keyboard.
    """
    def __init__(self, numberOfSlaveKeys, pins):
        super().__init__()
        self.hasSlaveKeyboard = False
        if numberOfSlaveKeys > 0:
            # Max baud rate is 921600
            self.uart = busio.UART(board.GP0, board.GP1, baudrate=256000)
            self.hasSlaveKeyboard = True
        self._pressed_buttons = 0
        self._last_own_pressed_buttons = 0
        self._last_other_pressed_buttons = 0
        self.key_pins = pins
        self.keys = keypad.Keys(self.key_pins, value_when_pressed=False, pull=True)
        self.states = [False] * self.keys.key_count
        self.own_button_count = len(self.key_pins)
        self.button_count = self.own_button_count + numberOfSlaveKeys

    def update(self):
        event = self.keys.events.get()
        if event:
            self.states[event.key_number] = event.pressed
            return True
        return False

    def _own_pressed_buttons(self):
        self.update()
        value = 0
        for i in range(0, self.keys.key_count):
            if self.states[i]:
                value += 1 << i
        return value

    def pressed_buttons(self):
        changed = False
        
        # our own pressed buttons
        own_pressed_buttons = self._own_pressed_buttons()
        if own_pressed_buttons != self._last_own_pressed_buttons:
            self._last_own_pressed_buttons = own_pressed_buttons 
            changed = True
        
        if self.hasSlaveKeyboard:
            # pressed buttons from the other keyboard half
            data_count = self.uart.in_waiting
            if data_count > 0:
                data = self.uart.readline()
                self._last_other_pressed_buttons = int.from_bytes(a2b_base64(data), "little")
                changed = True
        
        # compute a new value
        if changed:
            self._pressed_buttons = (self._last_other_pressed_buttons << self.own_button_count) + own_pressed_buttons

        return self._pressed_buttons

    
