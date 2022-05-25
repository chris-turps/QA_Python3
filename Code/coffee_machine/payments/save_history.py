import shelve

def saveTransaction(transaction):
    db = shelve.open('payment_history.log', writeback=True)
    if 'transactions' not in db.keys():
        db['transactions'] = []
    db['transactions'].append(transaction)
    db.close()

def printHistory():
    db = shelve.open('payment_history.log')
    if 'transactions' in db.keys():
        for transaction in db['transactions']:
            print(transaction)
            print("")
    db.close()

    