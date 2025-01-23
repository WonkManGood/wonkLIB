from machine import Pin, PWM
from wERRORS import wGenericError
from time import sleep

purple_1b = PWM(Pin(2, Pin.OUT), freq=100, duty_ns=100)
purple_2g = PWM(Pin(3, Pin.OUT), freq=100, duty_ns=100)
purple_3r = PWM(Pin(4, Pin.OUT), freq=100, duty_ns=100)
orange_1b = PWM(Pin(6, Pin.OUT), freq=100, duty_ns=100)
orange_2g = PWM(Pin(7, Pin.OUT), freq=100, duty_ns=100)
orange_3r = PWM(Pin(8, Pin.OUT), freq=100, duty_ns=100)
grey_1b = PWM(Pin(10, Pin.OUT), freq=100, duty_ns=100)
grey_2g = PWM(Pin(11, Pin.OUT), freq=100, duty_ns=100)
grey_3r = PWM(Pin(12, Pin.OUT), freq=100, duty_ns=100)

toggle_switch = Pin(22, Pin.IN, Pin.PULL_DOWN)


purple_1b.duty_u16(0)
purple_2g.duty_u16(0)
purple_3r.duty_u16(0)
orange_1b.duty_u16(0)
orange_2g.duty_u16(0)
orange_3r.duty_u16(0)
grey_1b.duty_u16(0)
grey_2g.duty_u16(0)
grey_3r.duty_u16(0)



while True:
    
    sleep(1)
    while True:
        
        try:
            for i in range(1, 60000):
                purple_1b.duty_u16(i)
                orange_2g.duty_u16(i)
                grey_3r.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
            for i in range(1, 60000):
                purple_2g.duty_u16(i)
                orange_3r.duty_u16(i)
                grey_1b.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
            for i in range(1, 60000):
                purple_3r.duty_u16(i)
                orange_1b.duty_u16(i)
                grey_2g.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
            for i in range(60000, 1, -1):
                purple_1b.duty_u16(i)
                orange_2g.duty_u16(i)
                grey_3r.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
            for i in range(60000, 1, -1):
                purple_2g.duty_u16(i)
                orange_3r.duty_u16(i)
                grey_1b.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
            for i in range(60000, 1, -1):
                purple_3r.duty_u16(i)
                orange_1b.duty_u16(i)
                grey_2g.duty_u16(i)
                if toggle_switch.value() == 1: raise wGenericError
        
        except wGenericError or KeyboardInterrupt:
            purple_1b.duty_u16(0)
            purple_2g.duty_u16(0)
            purple_3r.duty_u16(0)
            orange_1b.duty_u16(0)
            orange_2g.duty_u16(0)
            orange_3r.duty_u16(0)
            grey_1b.duty_u16(0)
            grey_2g.duty_u16(0)
            grey_3r.duty_u16(0)
            break
    
    sleep(1)
    while True:
        try:
            if toggle_switch.value() == 1: raise wGenericError
            else: pass
        except wGenericError:
            break