def fight():
    print("<<<<< Fighting Now >>>>>")


def attack():
    print("<<<< Attacking Now >>>>>>")

def fly():
    print("<<<<<< Flying Now >>>>>>>")


print(__name__)  # notice this function carefully. agr ye function es file se chalayngy tou "main" lekha aayga ,
                 # But agr ye function otherFile se chalyga tou ifNameModule lekha aayga.
 
fly()

if __name__ == '__main__':   #agr tumhe appne banye huye modules ke function ki testing krni hai(esi file se ), then use use functions below this line.
    fight()                  #otherwise when u use this module/file in other file , this fly() function will run itself without our consent.
    print(__name__)



