database = {}


def put(key, value):  # Put a pair of key/value in the database
    database[key] = value
    return database[key]


def get(key):  # Return the value associated with the key in the database
    if key in database.keys():
        return database[key]
    else:
        return None


def exists(key):  # Return True if the key is in the database, False otherwise
    if key in database.keys():
        return True
    else:
        database[key] = 0
        return False


def delete(key):  # Delete the key from the database
    if key in database.keys():
        database.pop(key)
        return True
    else:
        return False


def incrby(key, delta):  # Increment the value associated with `key` by `delta`
    if type(database[key]) is int or type(database[key]) is float:
        database[key] = database[key] + delta
    else:
        raise ValueError('Incorrect value')
    return database[key]


def incr(key):  # Increment the value associated with `key` by one
    if type(database[key]) is int or type(database[key]) is float:
        database[key] = database[key] + 1
    else:
        raise ValueError('Incorrect value')
    return database[key]


def sadd(key, value):  # Add `value` to the set associated with `key`
    if key not in database.keys():
        database[key] = {value}
    else:
        if type(database[key]) is not set:
            database[key] = {value}
        else:
            database[key].add(value)
    return value


def smembers(key):  # Return the set values associated with `key`
    if key in database.keys():
        if type(database[key]) is set:
            return database[key]
        else:
            return None
    else:
        return None


def sunion(key1, key2):  # Return all elements present accross both Sets
    for key in [key1, key2]:
        if key not in database.keys():
            database[key] = {}  # non-existing key - empty Set
    union_set = set()
    return union_set.union(database[key1], database[key2])


def sinter(key1, key2):  # Return all elements shared between both Sets
    for key in [key1, key2]:
        if key not in database.keys():
            database[key] = {}  # non-existing - empty Set
    return database[key1].intersection(database[key2])


def srem(key, value):  # Remove `value` in the set associated with `key`
    if key in database.keys():
        if type(database[key]) is set:
            pre_values = database[key]
            database[key].discard(value)
            if pre_values != database[key]:
                return True
            else:
                return False
        else:
            return False
    return False
