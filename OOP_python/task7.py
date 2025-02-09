class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name and
                self.age == other.age)
               
               
person1 = Person('John', 25)
person2 = Person('Andrey', 30)

print("Are they equal? - ", person1.__eq__(person2))
print("Are they equal? - ", person2 == person1)