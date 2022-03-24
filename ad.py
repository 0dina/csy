from gpiozero import MCP3008
from gpiozero import PWMLED

pot = MCP3008(0)
led = PWMLED(21)

led.on()
led.off()
led.value=0.5

while True:
    print('pot:',pot.value)
    led.value = pot.value

#led.source = pot.value
