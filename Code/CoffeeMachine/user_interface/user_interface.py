from .synthesise_message import *
from .user_io import *

def getIntResponse(min, max = None):
    while(True):
        response = input()
        isOK = response.isnumeric() and int(response) >= min
        if isOK and max is not None:
            isOK = int(response) <= max
        if isOK: break
        else:
            sendMessage(showRange(min,max))
    return int(response)

def get_int_selection(prompt, options):
    sendMessage(make_selection(prompt, options))
    return getIntResponse(0, len(options)) - 1

def show_choice(msg):
    sendMessage(f"You chose {msg}")
    
def request_cash(name, amount):
    sendMessage(f"Please insert money for {name} {showRange(amount)}: ", end='')
    return getIntResponse(amount)

def request_refill(name, minRequired, space):
    sendMessage(f"Please refill {name} {showRange(minRequired,space)}: ", end='')
    return getIntResponse(minRequired, space)

def give_coffee(coffee):
    sendMessage(f"Enjoy your {coffee}")

def take_change(change):
    sendMessage(f"Please take your change: {change}")
    return True