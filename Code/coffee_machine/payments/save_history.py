import shelve

def saveTransaction(transaction):
    db = shelve.open('payment_history.log', writeback=True)
    if 'transaction' not in db.keys():
        db['transactions'] = []
    db['transactions'].append(transaction)
    db.close()

def printHistory():
    db = shelve.open('payment_history.log')
    for transaction in db['transactions']:
        print(transaction)
        print("")
    db.close()