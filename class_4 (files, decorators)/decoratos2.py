


def safe_execution(original_func):
    def new_func(*args, **kwargs):
        try:
            return original_func(*args, **kwargs)
        except:
            print('Something went wrong!')
    return new_func


@safe_execution
def divide(a1, a2):
    return a1 / a2
    
@safe_execution
def my_sum(a1, a2, a3):
    return a1 + a2 + a3
    

print(my_sum(1, 2, 3))