class Pet:
    def __init__(self):
        self.name = "John"  # Default pet name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
    
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")
    
    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
    
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage
john = Pet()  # Creates John as the pet
john.get_status()  # Displays John's current attributes
john.train("jump")  # Teaches John to jump
john.train("run around")  # Teaches John to run around
john.show_tricks()  # Shows all tricks learned by John
