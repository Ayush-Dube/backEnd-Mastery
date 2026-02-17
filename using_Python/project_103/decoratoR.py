def decorateMe(xyz):
    def wrapper(a,b):
        res = xyz(a,b)
        print(f"the result of {xyz.__name__} operation is {res}.")
    
    return wrapper


@decorateMe
def add(a,b):
    return a+b


add(2,3)

## Another way of making a decorator

def multiply(x,y):
    return x*y


newMulti = decorateMe(multiply)
newMulti(2,5)

# Since we enhance the function and not 
multiply = decorateMe(multiply)
multiply(3,5)

# You do the same thing using @ symbol

@decorateMe
def diff(x,y):
    return abs(x-y)

diff(2,9)
