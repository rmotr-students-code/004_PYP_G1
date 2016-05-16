
class Student(object):
    
    def __init__(self, firstname, lastname, birthyr):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyr = birthyr
    
    def __str__(self):
        return '{} : {}'.format(self.full_name(), self.age)
    
    def __gt__(self, other):
        return self.age > other.age
        
    def __eq__(self, other):
        return self.age == other.age
    
    def full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    @staticmethod
    def calculate_age(birthyr):
        return 2015 - birthyr
        
    @property    
    def age(self):
        return Student.calculate_age(self.birthyr)
    @classmethod
    def batch_create(cls, data):
        students = []
        for student_info in data:
            new_student = Student(
                student_info.get('firstname'), 
                student_info.get('lastname'), 
                student_info.get('birthyr')
            )
            students.append(new_student)
        return students
        
    
david = Student('David', 'Jones', 1990)
martin = Student('Martin', 'Zugnoni', 1988)
    
    
david.full_name()
print(Student.calculate_age(1990))


print(david.age)


a_list_of_instances = Student.batch_create([
    {'firstname': 'Martin', 'lastname': 'Zugnoni', 'birthyr': 1988},    
    {'firstname': 'Santiago', 'lastname': 'Basulto', 'birthyr': 1987},   
])
for instance in a_list_of_instances:
    print(instance)


print(str(david))


if david > martin:
    print('David is greater')
else:
    print('Martin is greater')
    
    
david == martin