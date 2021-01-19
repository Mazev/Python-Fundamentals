class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'My name is {self.name}')

    def get_age(self):
        return 40


stefan = Person('Stefan')

print(stefan.get_age())
