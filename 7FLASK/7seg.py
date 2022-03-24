from flask import Flask, render_template, request
import spidev
from time import sleep



symbols = {0 : [~0x3F],
           1 : [~0x06],
           2 : [~0x5B],
           3 : [~0x4F],
           4 : [~0x66],
           5 : [~0x6D],
           6 : [~0x7D],
           7 : [~0x07],
           8 : [~0x7F],
           9 : [~0x67]}


spi = spidev.SpiDev()
spi.open(0, 0)              # open(bus, device)

spi.mode = 3
spi.max_speed_hz = 1000000  # set transfer speed

i=0


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('segflask.html')
        
        
@app.route('/post', methods=['POST'])
def display():
    num = request.form['number']
    print(num)
    print(type(num))
    i = int(num)
    spi.xfer2(symbols[i])
    


if __name__ == '__main__':
    app.run(debug=True, host='172.30.1.11')