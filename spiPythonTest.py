'''
const unsigned char symbols[16] = {                   //(msb) HGFEDCBA (lsb)
     0b00111111, 0b00000110, 0b01011011, 0b01001111,  // 0123
     0b01100110, 0b01101101, 0b01111101, 0b00000111,  // 4567
     0b01111111, 0b01100111, 0b01110111, 0b01111100,  // 89Ab
     0b00111001, 0b01011110, 0b01111001, 0b01110001   // CdEF
};

'''

import spidev
from time import sleep

symbols = [[~0x3F], [~0x06], [~0x5B],[~0x4F],[~0x66],[~0x6D],[~0x7D],[~0x07],
           [~0x7F],[~0x67]]# note: we must invert to hex value, from common anode type 7segment
spi = spidev.SpiDev()
spi.open(0, 0)              # open(bus, device)

spi.mode = 3
spi.max_speed_hz = 1000000  # set transfer speed

i=0
while(i<10):

    spi.xfer2(symbols[i])
    i+=1
    sleep(1)#delay 1 second
print("good bye")
spi.close()


