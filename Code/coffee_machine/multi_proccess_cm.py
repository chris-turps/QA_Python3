from payments.transaction import Transaction
from initialise import coffee_names, coffee_types
import time
import random
from multiprocessing import Queue, Process

def drinkCoffee(*args):
    queue = args[0]
    coffee = queue.get()

    while coffee != "GO_HOME":
        print(f"Programmer {args[1]} drank {coffee.drink}")
        time.sleep(1)
        if queue.empty():
            print(f"Programmer {args[1]} is thirsty...")
        else:
            coffee = queue.get()
    else:
       print(f"Programmer {args[1]} told to go home") 

def makeCoffee(*args):
    queue = args[0]
    quit = args[1]
    random.seed()
    while quit.empty():
        nextCoffeeSelection = random.randint(0,len(coffee_names)-1)
        coffee = Transaction(coffee_names[nextCoffeeSelection]
         , coffee_types[nextCoffeeSelection].cost
         , coffee_types[nextCoffeeSelection].cost
        )
        print(f"Machine {args[2]} made {coffee.drink}")
        time.sleep(1)
        if queue.empty():
            print(F"Machine {args[2]} is rushed off its feet!")
            queue.put(coffee)
    else:
        print(f"Machine {args[2]} told to {quit.get()}")

if __name__ == '__main__':
    queue = Queue()
    quit = Queue()
    makeCoffee_1 = Process(target=makeCoffee, args=(queue, quit, '1'))
    makeCoffee_2 = Process(target=makeCoffee, args=(queue, quit, '2'))
    makeCoffee_1.start()
    makeCoffee_2.start()

    drinkCoffee_1 = Process(target=drinkCoffee, args=(queue, '1'))
    drinkCoffee_2 = Process(target=drinkCoffee, args=(queue, '2'))
    drinkCoffee_1.start()
    drinkCoffee_2.start()

    time.sleep(20)
    quit.put('END')
    quit.put('END')
    queue.put('GO_HOME')
    queue.put('GO_HOME')

    makeCoffee_1.join()
    makeCoffee_2.join()
    drinkCoffee_1.join()
    drinkCoffee_2.join()

    print("Time to go home...")
    