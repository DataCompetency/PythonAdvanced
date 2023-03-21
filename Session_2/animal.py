# define a class with two attributes: name and species
# and one method that prints a sound 
class Animal:
    # constructor of class Animal, it is always 
    # called when creating an object of the class,
    # it is used to initialize the class' attributes
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self):
        print(f"{self._name} makes a sound.")
        
    def name(self):
        return f"Hi, my name is {self._name}."
    
    def species(self):
        return f"I'm a {self._species}!"
        

class PolarBear(Animal):
    """PolarBear class inherited from Animal"""
    
    def __init__(self, name, weight):
        """Constructor sets name and weight"""
        super().__init__(name, "Polar bear")
        self._weight = weight
        
        # progress for finding food for winter
        # 0 - not prepared, 1 - ready for winter 
        self._hibernation_preparation = 0.0
        
    def __str__(self):
        return f"{self._name} ({self._species}), weight: {self._weight}kg"

    def found_food(self, amount):
        """Eat food to gain weight and to prepare for hibernation"""
        self._weight += 0.7 * amount / 100
        self._hibernation_preparation += 0.3 * amount / 1000
        
    def __del__(self):
        """Destructor, is called when an object is deleted"""
        print(f"Please don't... {self._name} is crying.")