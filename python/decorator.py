# decorator = a function that extends the behavior of another function
# without modifying the base function
# pass the base function as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):                      # wrapper is important because add_sprinklers func will be called only if get_ice_cream func is called.
        print("*You add sprinkels*")    # without wrapper func add_sprinklers will be executed without even calling get_ice_cream func.
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla")