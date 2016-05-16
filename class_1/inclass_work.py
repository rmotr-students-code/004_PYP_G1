def multiply(num1, num2):
    return num1 * num2
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
    
def divide(num1, num2):
    return float(num1)/num2

operation_list = [multiply, divide, add, subtract]

def calculator(num1, num2, operation):
    if operation in operation_list:
        return operation(num1, num2)
    return None

# tests
print calculator(1, 3, add) # 4
print calculator(2, 3, operation=multiply) # 6

# return operation(num1, num2) if operation in operation_list else None

