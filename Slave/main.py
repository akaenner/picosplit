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

from adafruit_binascii import hexlify, unhexlify, a2b_base64, b2a_base64
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer
import busio
import board
import keypad
import time

class SlaveKeypad:
    """
    SlaveKeypad reads button states from the second half of my diy split keyboard. 
    """
    def __init__(self):
        super().__init__()
        self.key_pins = (board.GP2,
                         board.GP3,
                         board.GP4,
                         board.GP5,
                         board.GP6,
                         board.GP7,
                         board.GP8,
                         board.GP9,
                         board.GP10,
                         board.GP11,
                         board.GP12,
                         board.GP13,
                         board.GP14,
                         board.GP15,
                         board.GP16,
                         board.GP17,
                         board.GP18,
                         board.GP19,
                         board.GP20,
                         board.GP21)
        self.keys = keypad.Keys(self.key_pins, value_when_pressed=True, pull=True)
        self.states = [False] * self.keys.key_count

    def value(self):
        value = 0
        for i in range(0, self.keys.key_count):
            if self.states[i]:
                value += 1 << i
        return value

    def update(self):
        event = self.keys.events.get()
        if event:
            self.states[event.key_number] = event.pressed
            return True
        return False

class SlaveKeyboard:
    """
    SlaveKeyboard runs the main loop. It reads button states from the keypad and sends them 
    over a serial connection to the master keyboard.
    """
    def __init__(self, keypad):
        self.keypad = keypad
        self.isRunning = False
        self.uart = busio.UART(board.GP0, board.GP1, baudrate=256000)
  
    def start(self):
        if not self.isRunning:
            self.isRunning = True
            keypad = self.keypad
            
            while self.isRunning:
                if keypad.update():
                    self.send_keys(keypad.value())

    def stop(self):
        self.isRunning = False

    def send_keys(self, value):
        """
        Keys are sent as a base64 encoded integer to the master keyboard.
        """
        # print("keys: ", value)
        self.uart.write(b2a_base64(value.to_bytes(3, "little", signed=False)))

# Create the keyboard 
keyboard = SlaveKeyboard(keypad=SlaveKeypad())

# Start the main loop
keyboard.start()
