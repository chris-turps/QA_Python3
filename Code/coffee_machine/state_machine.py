'''
SR: to manage state
'''
from user_interface.user_interface import *
from initialise import coffee_types, coffee_names
from enum import Enum, auto

class CM_state(Enum):
    OFF = auto()
    GET_COFFEE_SELECTION = auto()
    QUIT = auto()

cm_state = CM_state.GET_COFFEE_SELECTION

def state_machine(current_state):
    match current_state:
        case CM_state.GET_COFFEE_SELECTION:
            choice = get_int_selection("Coffee", coffee_names)
            if choice == -1:
                current_state = CM_state.QUIT
            else:
                show_choice(coffee_names[choice])
                sendMessage("")
        case QUIT:
            sendMessage("Bye...")
            current_state = CM_state.OFF
    return current_state

if __name__ == "__main__":  
    state_machine(CM_state.GET_COFFEE_SELECTION)