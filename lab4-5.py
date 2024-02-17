from adafruit_circuitplayground import cp

def CelToFahr(Celsius):
    Temperature = Celsius * 9 / 5 + 32
    return Temperature

def FahrToCel(Temperature):
    Celsius = 5 / 9 * (Temperature - 32)
    return Celsius

while True:
    if cp.button_a == True:
        if cp.switch == True:
            print("The Temperature in F : ", CelToFahr(cp.temperature))
        else:
            print("The Temperature in C: ", cp.temperature)
