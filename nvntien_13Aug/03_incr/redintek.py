database = {}


def put(key, value):
    database[key] = value
    return database


def get(key):
    if key in database.keys():
        return database[key]
    else:
        return None


def exists(key):
    if key in database.keys():
        return True
    else:
        database[key] = 0
        return False


def delete(key):
    database.pop(key, None)
    return database


def incrby(key, delta):
    if type(database[key]) is int or type(database[key]) is float:
        database[key] = database[key] + delta
    else:
        raise ValueError('Incorrect value')
    return database


def incr(key):
    if type(database[key]) is int or type(database[key]) is float:
        database[key] = database[key] + 1
    else:
        raise ValueError('Incorrect value')
    return database
