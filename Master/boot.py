# This file is part of the PicoSplit-Keyboard project, http://kaenner.de/PicoSplit.html
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

from digitalio import DigitalInOut, Direction, Pull
import busio
import board
import usb_hid 
import usb_midi
import usb_cdc
import storage

maintenance_mode = False

buttons = []
buttons.append(DigitalInOut(board.GP2))
buttons.append(DigitalInOut(board.GP3))
buttons.append(DigitalInOut(board.GP4))
buttons.append(DigitalInOut(board.GP5))
buttons.append(DigitalInOut(board.GP6))
buttons.append(DigitalInOut(board.GP7))
buttons.append(DigitalInOut(board.GP8))
buttons.append(DigitalInOut(board.GP9))
buttons.append(DigitalInOut(board.GP10))
buttons.append(DigitalInOut(board.GP11))
buttons.append(DigitalInOut(board.GP12))
buttons.append(DigitalInOut(board.GP13))
buttons.append(DigitalInOut(board.GP14))
buttons.append(DigitalInOut(board.GP15))
buttons.append(DigitalInOut(board.GP16))
buttons.append(DigitalInOut(board.GP17))
buttons.append(DigitalInOut(board.GP18))
buttons.append(DigitalInOut(board.GP19))
buttons.append(DigitalInOut(board.GP20))
buttons.append(DigitalInOut(board.GP21))

try:
    f = open("mapping.js")
except IOError:
    maintenance_mode = True
finally:
    f.close()

for button in buttons:
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN
    if button.value:
        maintenance_mode = True

if not maintenance_mode:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_midi.disable()
    
usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1 if not maintenance_mode else 0)

  
    
