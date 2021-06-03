from machine import Pin
import utime
import time
echo=Pin(2,Pin.IN)
trigger= Pin(3,Pin.OUT)
buzzer= Pin(4,Pin.OUT)
led_Red = Pin(5,Pin.OUT)
led_Yellow =Pin(6,Pin.OUT)
led_Blue = Pin(7,Pin.OUT)
led_Green = Pin(8,Pin.OUT)

while True:
    trigger.value(0)
    utime.sleep_us(2)
    trigger.value(1)
    utime.sleep_us(5)
    while echo.value()==0:
        signaloff = utime.ticks_us()
    while echo.value()==1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance =(timepassed *0.0343)/2
    print("The distance",distance,"cm")
    utime.sleep(2)
    
    if distance <=30:
        led_Red.on()
        led_Yellow.on()
        led_Blue.on()
        led_Green.on()
        
        for j in range(50):
         buzzer.toggle()
         time.sleep_ms(10)
    else:
        buzzer.off()
        led_Red.off()
        
        
    if distance <=40:
        led_Yellow.on()
        led_Blue.on()
        led_Green.on()
    else:
        led_Yellow.off()
        led_Blue.off()
        led_Green.off()
        
    if distance <= 50:
        led_Blue.on()
        led_Green.on()
    else:
        led_Blue.off()
        led_Green.off()
        
    if distance <= 60:
        led_Green.on()
    else:
        led_Green.off()
        
        
    
    
    