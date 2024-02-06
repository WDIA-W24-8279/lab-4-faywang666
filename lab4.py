
def displayInstructions():
    print("Hello there")
    print("This amazing piece of python code")
    print("Converts Fahrenheit to Celsius")
    return


def FahrToCel(Temperature):
    Celsius = 5/9*(Temperature-32)
    return Celsius

def validateFloat():
    n = input("Value in Fahrenheit?>")
    while isinstance(n,float) == False:
        print("This is not a float")
        n = input("Value in Fahrenheit?>")
    return n


displayInstructions()
F = validateFloat()

C = FahrToCel(F)
print("{} F = {} C".format(F,C))

'''
F = float(input("Value in Fahrenheit?>"))
C = 5 / 9 * (F - 32)
'''
