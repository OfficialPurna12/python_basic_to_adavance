class students:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def show_name(self):
        print(f" My name is : {self.name} and My marks : {self.__marks}")

persona = students("Purna bahadur Khatru", 98)
persona.show_name()