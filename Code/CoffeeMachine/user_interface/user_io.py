def sendMessage(msg):
    print(msg)

def sendContinuationMessage(msg):
    print(msg, end = "")

def getInt(msg):
    return int(input(msg))

def getIntSequence(msg):
    return [int(value) for value in input(msg) if value.isnumeric()]