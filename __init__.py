from wonkLED_package.led_interface import (
    simpleLED,
    rgbLED
)

__all__ = [simpleLED, rgbLED]

try:
    with open(file='.wonkKEY', mode='r'): ...
    from sys import path
    path.append('/home/ej/wonkLIB')
except BaseException: ...
print(dir())