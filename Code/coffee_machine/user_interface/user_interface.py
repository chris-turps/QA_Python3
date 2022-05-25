from .synthesise_message import *
from .user_io import *

def getIntResponse(min, max = None, testResponse = None):
    while(True):
        if testResponse == None:
            response = getInt("")
        else: response = testResponse
        isOK = response >= min
        if response >= min and max is not None:
            isOK = response <= max
        if isOK: break
        else:
            sendMessage(showRange(min,max))
    return response

def get_int_selection(prompt, options):
    sendContinuationMessage(make_selection(prompt, options))
    return getIntResponse(0, len(options)) - 1

def show_choice(msg):
    sendMessage(f"You chose {msg}")
    
def request_cash(name, amount):
    sendContinuationMessage(f"Please insert money for {name} {showRange(amount)}: ")
    return getIntResponse(amount)

def request_refill(name, minRequired, space):
    sendContinuationMessage(f"Please refill {name} {showRange(minRequired,space)}: ")
    return getIntResponse(minRequired, space)

def give_coffee(coffee):
    sendMessage(f"Enjoy your {coffee}")

def take_change(change):
    sendMessage(f"Please take your change: {change}")
    return True