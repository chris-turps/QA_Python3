'''
SR: to switch between states
'''
from user_interface.user_interface import *
from operations import *
from machine_states import *

cm_state = CM_state.GET_COFFEE_SELECTION

def state_machine(current_state):
    match current_state:
        case CM_state.GET_COFFEE_SELECTION:
            current_state = chooseCoffee()
        case CM_state.TAKE_PAYMENT:
            current_state = takePayment()
        case CM_state.GIVE_CHANGE:
            current_state = giveChange()
        case CM_state.CREATE_TRANSACTION:
            current_state = createTransaction()
        case CM_state.QUIT:
            showTransactions()
            sendMessage("Bye...")
            current_state = CM_state.OFF
    return current_state

if __name__ == "__main__":  
    state_machine(CM_state.GET_COFFEE_SELECTION)