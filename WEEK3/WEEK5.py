class Dog:
     def speak(self):
          return"woof"

class Cat:
     def speak(self):
          return"Meow"

#Polymorphism in action
for animal in [Dog(, Cat())]:
    print(animal.speak())