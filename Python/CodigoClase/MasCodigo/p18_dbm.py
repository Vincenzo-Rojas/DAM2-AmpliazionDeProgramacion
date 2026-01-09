import dbm

def ejem1():

    # Open database, creating it if necessary.
    with dbm.open('cache.db', 'c') as db:

        # Record some values
        db[b'hello'] = b'there'
        db['www.python.org'] = 'Python Website'
        db['www.cnn.com'] = 'Cable News Network'

        # Note that the keys are considered bytes now.
        assert db[b'www.python.org'] == b'Python Website'
        # Notice how the value is now in bytes.
        assert db['www.cnn.com'] == b'Cable News Network'

        # Often-used methods of the dict interface work too.
        print(db.get('python.org', b'not present'))
        print(db.get('www.python.org', b'not present'))

        # Storing a non-string key or value will raise an exception (most
        # likely a TypeError).
        #db['www.yahoo.com'] = 4


def ejem2():

    # Open database, creating it if necessary.
    db = dbm.open('cache2.db', 'c')

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    
    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))
    print(db.get('www.python.org', b'not present'))
    print(db['www.python.org'])
    print(db.keys())
    print(db.values())
    for i in db.values():
        print(i)

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    #db['www.yahoo.com'] = 4
    
    db.close()

print("Empezamos")
ejem1()
print("*"*25)

ejem2()

print("Fin")
