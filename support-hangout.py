


class Person(object):
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        
    def calculate_age(self):
        return 2015 - self.birth_year
        
    @classmethod
    def foobar(cls):
        print("Worked!")
        
    
    
martin = Person("Martin", "Zugnoni", 27)
Person.foobar()





