
from abc import ABC, abstractmethod 

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass 

class circle(Shapes):
    def area(self):
        return 3.14 * 5 * 5

c = circle()
print(c.area())

