'''
SR: to send and receive IO
'''

def sendMessage(msg):
    print(msg)

def sendContinuationMessage(msg):
    print(msg, end = "")

def getInt(msg):
    response = input(msg)
    while not response.isnumeric():
        sendMessage("Please type a number")
        response = input(msg)
    return int(response)

def getIntSequence(msg, test = None):
    if test == None:
        response = input(msg)
    else: response = test
    return [int(value) for value in response.split() if value.isnumeric()]