storage = {}


def put(key, value):
    storage[key] = value
    return True


def get(key):
    return storage[key]


def __str__():
    for key in storage:
        print(key, storage[key])
