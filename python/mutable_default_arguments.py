# List Accumulation Bug
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

print(add_item('apple'))  # ['apple']
print(add_item('banana')) # ['apple', 'banana'] — Unexpected!


# fixed List Accumulation
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print(add_item('apple')) 
print(add_item('banana'))


# Dictionary Mutation Bug
def set_config(key, value, config={}):
    config[key] = value
    return config

print(set_config('debug', True))  # {'debug': True}
print(set_config('port', 8080))   # {'debug': True, 'port': 8080} — Unexpected!

# fixed Dictionary Mutation
def set_config(key, value, config=None):
    if config is None:
        config = {}
    config[key] = value
    return config

print(set_config('debug', True))
print(set_config('port', 8080))

# Class-Level Mutable Defaults
class User:
    def __init__(self, name, tags=[]):
        self.name = name
        self.tags = tags

u1 = User('Alice')
u2 = User('Bob')
u1.tags.append('admin')

print(u2.tags)  # ['admin'] — Why does Bob have 'admin'?

# fixed Class-Level Mutable Defaults

class User:
    def __init__(self, name, tags=None):
        self.name = name
        self.tags = tags if tags is not None else []

u1 = User('Alice')
u2 = User('Bob')
u3 = User('Ron')
u1.tags.append('admin')
u2.tags.append('guest')

print(u1.tags)
print(u2.tags)
print(u3.tags)