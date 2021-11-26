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
import time
from lib.picosplit.config_loader import ConfigLoader
from lib.picosplit.split_keypad import SplitKeypad


# Sleep for a bit to avoid a race condition on some systems
time.sleep(1)

# load the configuration from the config.kbdconfig file
loader = ConfigLoader(configFilePath="layout.js") 
kb = loader.keyboard(SplitKeypad(20, 
						(board.GP2,
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
						 board.GP21)))
kb.start()
