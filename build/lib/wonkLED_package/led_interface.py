try:
    from gpiozero import LED
except ImportError:
    print('\n\nMissing package: gpiozero')

def simpleLED(
        pin: int = 0,
        state: None | bool = False
        ) -> None:

    '''
    Modifies listed pin. If true, return led.on and false, return led.off. Turns pin off if state undefined.\n
    \n
    Used for single I/O LED's.
    '''
    

    led = LED(pin)
    if state == True: led.on()  # noqa: E712
    if state == False: led.off()

def rgbLED(
        pin_r: int | int = 0,
        pin_g: int | int = 0,
        pin_b: int | int = 0,
        red: float | int = 0,
        green: float | int = 0,
        blue: float | int = 0
) -> None:
    '''
    Takes rgb formats and returns them into LED.value's. Returns LED.value() for each Pin specified.
    '''

    pins = [red, green, blue]
    for i in range(0, 2):
        if 1 < float(pins[i]) < 0:
            raise ValueError('Pin value out of range. [0.00 -> 1.00]')
    
    red, green, blue = ((red * 4) / 1000), ((green * 4) / 1000), ((blue * 4) / 1000)
    if red > 1:
        red = red - (red - 1)
    if green > 1:
        green = green - (green - 1)
    if blue > 1:
        blue = blue - (blue - 1)
    
    red_led = LED(pin_r)
    green_led = LED(pin_g)
    blue_led = LED(pin_b)

    red_led.value = red
    green_led.value = green
    blue_led.value = blue
