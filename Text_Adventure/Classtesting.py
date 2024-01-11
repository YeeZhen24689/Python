import random
from random import randint

class Test():

    def __init__(self):
        self.name = randint(1,5)
        

def function():
    Test1 = Test()
    print(Test1.name)

for i in range (10):
    function()