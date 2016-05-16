
def safe_divide(f):
    def new_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ZeroDivisionError:
            print("Come on dude! a2 can not be 0")
    return new_f


@safe_divide
def divide(a1, a2):
    return a1 / a2
    
print(divide(1, 0))