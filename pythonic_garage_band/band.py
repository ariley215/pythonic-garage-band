
class Guitarist():
    
    def __init__(self, name="Joan Jett"):
       self.name = name
      
    
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return "Guitarist instance. Name = Joan Jett"