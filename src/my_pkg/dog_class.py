class Dog:
    def __init__(self, breed, height, color):
        self.breed = breed
        self.height = height/2.45
        self.color = color

mydog = Dog('Pug',40,'brown')

print(mydog.height)