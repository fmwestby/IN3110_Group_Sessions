class Dog:
    
    def __init__(self, name, sex):
        """Initialize a dog object.

        Args:
            name (str): The dogs name.
            sex (str): The dogs sex.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
        """
        
        self.name = name
        self.sex = sex
        
        #check if name is type str
        if not isinstance(self.name, str):
            raise TypeError(f"name must be a string, and not type {type(self.name)}")
        
        #check if sex is type str
        if not isinstance(self.sex, str):
            raise TypeError(f"name must be a string, and not type {type(self.sex)}")
        
    def __str__(self):
        """Returns a nicely printable string representation of the dog.

        Returns:
            str: A string representation of the dog.
        """
        return f"{self.name} is a {self.sex} dog."
        
def test_dog():
    """ Test for dog class"""
    dog = Dog("Pluto", "male")
    
    assert dog.name == "Pluto"
    assert isinstance(dog.sex, str)
    assert dog.__str__() == "Pluto is a male dog."
       
        
Daisy = Dog("Daisy", "female")
print(Daisy)