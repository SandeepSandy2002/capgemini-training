from abc import ABC, abstractmethod
# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        """Abstract method with no implementation"""
        pass
# Child class implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Bark"
class Cat(Animal):
    def make_soundS(self):
        return "Bark"
    
# Creating an instance of Dog
dog = Dog()
cat=Cat()
print(dog.make_sound())  # Output: Bark