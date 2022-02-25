# Flowshutter
# Copyright (C) 2021  Hugo Chiang

# Flowshutter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Flowshutter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with flowshutter.  If not, see <https://www.gnu.org/licenses/>.
from machine import UART, Pin, SoftI2C, ADC

def init_bat():
    batpin=Pin(36, Pin.IN)
    bat = ADC(batpin)
    return bat

def init_crsf_uart():
    uart1 = UART(1, baudrate=420000, bits = 8, parity = None, stop = 1, tx = 18, rx = 19)
    return uart1
    
def init_audio():
    audio_pin = Pin(18, Pin.OUT)
    return audio_pin

def init_i2c():
    i2c = SoftI2C(scl=Pin(21), sda=Pin(22),freq = 400000)
    return i2c

def init_buttons():
    button_page = Pin(33, Pin.IN, Pin.PULL_UP)
    button_enter = Pin(32, Pin.IN, Pin.PULL_UP)
    return button_page, button_enter

def init_uart2():
    uart2 = UART(2, baudrate = 9600, bits = 8, parity = 0,    stop = 1, tx = 25, rx = 26)
    return uart2
