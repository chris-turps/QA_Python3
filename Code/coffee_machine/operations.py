from machine_states import *
from user_interface.user_interface import *
from initialise import coffee_types, coffee_names

coffeeChoice = 0
amount_paid = 0
change = 0

def chooseCoffee():
    global coffeeChoice
    coffeeChoice = get_int_selection("Coffee", coffee_names)
    if coffeeChoice == -1:
        return CM_state.QUIT
    else:
        show_choice(coffee_names[coffeeChoice])
        sendMessage("")
        return CM_state.TAKE_PAYMENT

def takePayment():
    amount_paid = request_cash(coffee_names[coffeeChoice],coffee_types[coffeeChoice]["Cost"])
    global change
    change = amount_paid - coffee_types[coffeeChoice]["Cost"]
    if change > 0:
        return CM_state.GIVE_CHANGE
    else:
        return CM_state.GET_COFFEE_SELECTION

def giveChange():
    take_change(change)
    return CM_state.GET_COFFEE_SELECTION