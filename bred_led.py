#RasPi ブレッドボード＋LED
#https://docs.sunfounder.com/projects/thales-kit/en/latest/hello_breadboard.html#hello-breadboard
import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
while True:
    led.toggle()
    utime.sleep(1)