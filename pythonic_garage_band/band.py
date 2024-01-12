
class Guitarist():
    
    def __init__(self, name="Joan Jett"):
       self.name = name
      
    
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    

class Drummer():
       
    def __init__(self, name="Sheila E."):
       self.name = name
      
    
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
class Bassist():
    def __init__(self, name="Meshell Nsegeocello"):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"