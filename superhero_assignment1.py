# Superhero class
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def intro(self):
        return f"{self.name} has the power of {self.power} but is vulnerable to {self.weakness}."

    # polymorphism example
    def fight(self):
        return f"{self.name} is fighting with all his might!"


# Sidekick class, inheriting from Superhero
class Sidekick(Superhero):
    def __init__(self, name, power, weakness, master):
        super().__init__(name, power, weakness)  # Call the constructor of the Superhero class
        self.master = master

    # Sidekick specific method
    def assist(self):
        return f"{self.name} is assisting {self.master} in the battle!"

    # Overriding the fight method to showcase polymorphism
    def fight(self):
        return f"{self.name} is fighting alongside {self.master}!"


# Creating Superhero and Sidekick objects
superman = Superhero("Superman", "Flight and Strength", "Kryptonite")
batman_sidekick = Sidekick("Robin", "Gadgets and Acrobatics", "Fear of Failure", "Batman")

print(superman.intro())  
print(batman_sidekick.intro())   
print(superman.fight())   
print(batman_sidekick.fight())   
print(batman_sidekick.assist())   

# Polymorphism in action:
heroes = [superman, batman_sidekick]
for hero in heroes:
    print(hero.fight())  # Outputs will vary based on the hero's class implementation of the fight method