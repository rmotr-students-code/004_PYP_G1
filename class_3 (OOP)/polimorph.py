
class Animal:
    
    def __init__(self, name):
        self.name = name
'''        
    def talk(self):
        raise NotImplementedError("Must be implemented in subclasses")
'''


class Cat(Animal):
    
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    
    def talk(self):
        return 'Woof! Woof!'


class Human(Animal):
    
    def talk(self):
        return 'Hello world, Im {}'.format(self.name)

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie'),
           Human("David")]

for animal in animals:
    print('{}: {}'.format(animal.name, animal.talk()))

# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!