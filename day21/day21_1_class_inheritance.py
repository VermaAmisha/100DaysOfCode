
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):     
        super().__init__()   # to inherit methods of different class 
# the call to super() in the initializer is recommended, but not strictly required

    def breathe(self):
        super().breathe()
        print("doint this underwater")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)    # methods of different class need not printed
# print(nemo.swim)      # need not print the methods of same class
# print(nemo.breathe)
