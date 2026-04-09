# class Sample():
#     pass


# x = Sample()

# print(type(x))

class Dog():

    # Class level attributes
    species = "Canine"
    def __init__(self,breed,name="unknow"): # default parameter used.
        self.breed = breed 
        self.name = name

    
x = Dog('Husky')
# print(type(x.breed))
print(x.breed)

d1 = Dog("Lab","pebby")

print(d1.name)

print(x.species)
print(d1.species)