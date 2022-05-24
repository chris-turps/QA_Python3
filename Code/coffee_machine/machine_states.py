from enum import Enum, auto

class CM_state(Enum):
    OFF = auto()
    GET_COFFEE_SELECTION = auto()
    TAKE_PAYMENT = auto()
    GIVE_CHANGE = auto()
    CREATE_TRANSACTION = auto()
    QUIT = auto()