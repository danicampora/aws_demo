import demo
from network import WLAN

wlan = WLAN(mode=WLAN.STA)
wlan.connect('Daniel', auth=(None, '123456abc'))

while not wlan.isconnected():
    pass

demo.run()
