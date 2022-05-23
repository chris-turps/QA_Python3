def makeCoffee(coffeeChoice):
    print("Making ", coffeeChoice)

def drinkCoffee():
    print("Enjoy your coffee")
    return "I need a pee"

def writeSomeCode(soFar):
    soFar += "£$%^KJHFG"
    return soFar

code = ""
while (len(code) < 100):
    makeCoffee("Americano")
    print(drinkCoffee())
    code = writeSomeCode(code)
    print("")

print(code)
