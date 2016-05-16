class First(object):
    def __init__(self):
        self.var1 = 'Im the first'
        
    def another_method(self, x, y):
        print(x)
        print(y)


class Second(First):
    def my_function(self):
        super(Second, self).another_method(1, 2)
        print("I'm the second class")
        print(self.var1)
        
    
s = Second()
s.my_function()
