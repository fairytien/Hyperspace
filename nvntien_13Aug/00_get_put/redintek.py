database = {}


def put(key, value):
    database[key] = value
    return database


def get(key):
    if key in database.keys():
        return database[key]
    else:
        return None
