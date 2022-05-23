
def showRange(min, max = None):
    if max is None:
        rangeStr = f'(at least {str(min)})'
    else:
        rangeStr = f'({str(min)} - {str(max)})'
    return rangeStr

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

def make_selection(prompt, options):
    sendMessage(f"Please select {prompt}")
    for i, name in enumerate(options, start=1):
        sendMessage(f"{i} {name}")
    sendContinuationMessage(f"{showRange(1,i)} or 0 to quit: ")
    return getIntResponse(0, i) - 1

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

def sendMessage(msg):
    print(msg)

def sendContinuationMessage(msg):
    print(msg, end = "")