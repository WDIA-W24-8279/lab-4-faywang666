import time
from adafruit_circuitplayground import cp

# fahrenheit_to_celsius
def FahrToCel(fahrenheit):
    Celsius = 5/9*(fahrenheit-32)
    return Celsius

# celsius_to_fahrenheit
def CeltoFah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    if cp.switch == True:
        print(CeltoFah(cp.temperature))
    else:
        print(FahrToCel(cp.temperature))
    time.sleep(1)