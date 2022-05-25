from machine_states import *
from user_interface.user_interface import *
from initialise import coffee_types, coffee_names
from payments import transaction, payment_history, save_history

coffeeChoice = 0
amount_paid = 0
change = 0

def chooseCoffee(test = None):
    sendMessage("")        
    global coffeeChoice
    if test != None: coffeeChoice = test   
    else: coffeeChoice = get_int_selection("Drink", coffee_names)
    if coffeeChoice == -1:
        return CM_state.QUIT
    else:
        show_choice(coffee_names[coffeeChoice])
        return CM_state.TAKE_PAYMENT

def takePayment(test = None):
    global amount_paid
    if test != None: amount_paid = test   
    else: amount_paid = request_cash(coffee_names[coffeeChoice],coffee_types[coffeeChoice].cost)
    global change
    change = amount_paid - coffee_types[coffeeChoice].cost
    if change > 0:
        return CM_state.GIVE_CHANGE
    else:
        return CM_state.CREATE_TRANSACTION

def giveChange():
    take_change(change)
    return CM_state.CREATE_TRANSACTION

def createTransaction():
    newTransaction = transaction.Transaction(coffee_names[coffeeChoice],coffee_types[coffeeChoice].cost,amount_paid)
    save_history.saveTransaction(newTransaction)
    #payment_history.payments.append(newTransaction)
    return CM_state.GET_COFFEE_SELECTION

def showTransactions():
    #for transaction in payment_history.payments:
        #sendMessage(transaction)
    save_history.printHistory()
    