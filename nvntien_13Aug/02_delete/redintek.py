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
        return False


def delete(key):
    database.pop(key, None)
    return database
