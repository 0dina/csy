from flask import Flask, render_template, request
#from gpiozero import MCP3008
#from gpiozero import PWMLED
#from adafruit_motorkit import MotorKit
import time

#kit = MotorKit()
#pot = MCP3008(0)

throttle = 0.0

adc_ch0_binary = 0

'''
def testmotor ():
    print('speed up')
    for i in range(100):
        throttle = i/100
        print('throttle: ', throttle)
        kit.motor1.throttle = throttle
        time.sleep(0.01)

    print('speed down')
    for i in range(100):
        throttle = 1 - i/100
        print('throttle: ', throttle)
        kit.motor1.throttle = throttle
        time.sleep(0.01)
        '''
        
def readadc_ch0 ():
    #adc_ch0_binary = pot.value
    print('ch0:', adc_ch0_binary)

        
        
app = Flask(__name__)

@app.route('/')
def index():
    i = 0
    while i < 100 :
        #readadc_ch0()
        adc_ch0_binary = 12.3
        i = i+1
        sleep(0.1)
        render_template('PCing.html',adc_ch0_binary = adc_ch0_binary)
        
        
#@app.route('/post', methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True, host='172.30.1.10')