import math


def FahrToCel(Temperature):
    Celsius = 5/9*(Temperature-32)
    return Celsius

def min(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return "equal"

def VolumeOfSphere(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume

print(FahrToCel(45))
print(min(34,43))
print(VolumeOfSphere(5))