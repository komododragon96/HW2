
import math

pi=math.pi

class Sphere(object):
        
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def volume(self):
        return float((4/3) * pi * self.radius * self.radius * self.radius)   
     
    def surfacearea(self):
        return float(4 * pi * self.radius * self.radius) 
        
    def density(self):
        return float(self.mass/self.volume())
   
    
red = Sphere(1.7,0.25)

print dir(red)
print(red.volume())
print(red.surfacearea())
print(red.density())
