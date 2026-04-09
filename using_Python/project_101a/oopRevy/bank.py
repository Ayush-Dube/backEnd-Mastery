


# owner
# balance 


# deposit
# withdrawl 


# withrdrw cant be more then available balance 

class Account():

    self.store = 0

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance 
        self.store = balance

    def add(self,amount):

        self.store = self.store + amount

    def sub(self,amount):

        if self.store >= amount:
            self.store = self.store - amount 
        
        else:
            print("u dont have enough balance")


    def avBl():
        return self.store

    def __repr__(self):
        return f"{self.name} has {self.store} Rupees"

p1 = Account("sam",1000)

print(p1)

p1.add(500)

print(p1)

p1.sub(3000)

print(p1)
print(p1.name)

p1.add(200)
p1.sub(400)
p1.add(999)
p1.sub(50)
print(p1.store)