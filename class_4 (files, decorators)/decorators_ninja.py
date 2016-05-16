import json
import os
import tempfile



######## Example 1 ########
def trace_execution_decorator(original_f):
    """Prints a log before an after calling to original_f."""
    def new_function(*numbers):
        print("Before calling")
        returned_by_original_f = original_f(*numbers)
        print("After calling")
        return returned_by_original_f
    return new_function


@trace_execution_decorator
def add(numbers):
    return sum(numbers)
# TIP! this is equals to the block above!
# add_improved = trace_execution_decorator(add)



######## Example 2 ########
class DummyClassDecorator(object):
    """
    Dummy decorator using classes
    """
    def __init__(self, original_function):
        self._original_function = original_function

    def __call__(self):
        print('Decorator using a class :)')
        returned_data = self._original_function()
        return returned_data


@DummyClassDecorator
def add_using_class():
    return "add_using_class()"
# TIP! this is equals to the block above!
# add_using_class_improved = DummyClassDecorator(add_using_class)



######## Example 3 ########
class AuthException(Exception):
    """Custom exception for the door_control example."""
    pass


######## Example 4 ########
def door_control(original_function):
    """Check if the door could be open by the person who_is_trying."""
    def inner(who_is_trying):
        if who_is_trying.upper() != "NINJA":
            print('Access forbidden for {0}'.format(who_is_trying))
            raise AuthException('Access forbidden!')

        print('Access granted for {0}!'.format(who_is_trying))
        return original_function(who_is_trying)
    return inner


@door_control
def open_door(who):
    return 'The door is open now!'



######## Example 5 ########
def jsonify(original_function):
    """Returns a JSON version of an object returned by original_function."""
    def inner(*args, **kwargs):
        returned_data = original_function(*args, **kwargs)
        try:
            data = returned_data.to_dict()
        except AttributeError:
            # continue the object should be JSON serializable
            data = returned_data

        try:
            json_data = json.dumps(data)
        except TypeError:
            # The object is not JSON serializable!
            raise

        return json_data
    return inner


@jsonify
def get_user_dict():
    user = {
        'name': 'Martin',
        'last': 'Alderete',
        'company': 'rmotr'
    }
    return user


class User(object):
    def __init__(self, name, last, company):
        self._name = name
        self._last = last
        self._company = company

    def to_dict(self):
        return self.__dict__


@jsonify
def get_user_object():
    return User('Martin', 'Alderete', 'rmotr')


@jsonify
def get_user_bad():
    # object() is not JSON serializable!
    return object()



######## Example 6: A function decorated by more than 1 decorator! ########

@jsonify
@trace_execution_decorator
def get_user_object_chain():
    return User('Martin', 'Alderete', 'rmotr')
# TIP! this is equals to the block above!
# improved_get_user_object_chain = jsonify(trace_decorator(get_user_object_chain))



######## Example 7 ########
def ensure_file_start(original_function):
    """Ensure reading a file from the very beginning."""
    def inner(file_object):
        try:
            # Ensure the byte 0 always ;)!
            file_object.seek(0)
        except AttributeError as e:
            # file_object is not a file!
            raise
        else:
            return original_function(file_object)
    return inner



@ensure_file_start
def reader(file_obj):
    """Reads a file from the current position."""
    return file_obj.read()



##### BEGIN USES #####
if __name__ == "__main__":
    print(add((1, 2, 3, 4)))
    
    
    add_decorated = trace_execution_decorator(add)   # decorate a function MANUALLY!!!
    print("Code executed when we call add_decorated: {0}".format(add_decorated))
    
    print(add_decorated((1, 2, 3, 4)))  # call the decorated version!
    print(add_using_class())   # call the decorated version built by using classes!



    # Door example!
    print('Entering...\n')
    try:
        open_door('ninja')
    except AuthException as e:
        print(e)


    print('Entering...\n')
    try:
        open_door('Martin')
    except AuthException as e:
        print('Something was wrong with open_door(): {0}\n'.format(e))


    
    # JSON serializable example!
    print 'JSON returned by get_user_dict(): {0}\n'.format(get_user_dict())
    try:
        print get_user_bad()
    except Exception as e:
        print('Something was wrong with get_user_bad(): {0}\n'.format(e))
    print 'JSON returned get_user_object(): {0}\n'.format(get_user_object())

    print('get_user_object_chain(): {0}\n'.format(get_user_object_chain()))


    print('reader()')
    f_name = os.path.join(tempfile.gettempdir(), 'example.txt')
    with open(f_name, 'w') as my_file:  # Opened for writing ;)
        # Writes some bytes in the file!
        my_file.write('Hello\nGuys\nat\rmotr')


    f = open(f_name)  # just for reading!
    f.seek(5)  # go to the 5th byte
    print('Current position at the file: {0}'.format(f.tell()))
    content = reader(f)
    print('File content from the current position:\n{0}'.format(content))
