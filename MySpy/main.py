from function import getGuestInfo , getUserInfo
from SpyClass import Spy
from globalDetail import spy,friends
from start_chat import start_chat
if __name__ == "__main__":
    print "Let's get started"
    choice = raw_input('You want to start as guest Y/N : ')

    obj = Spy()

    if(choice == "y" or choice=="Y"):
        name,age,rating = getGuestInfo()
        obj.setDetail(name,age,rating)

    elif(choice=="n" or choice == "N"):
        info = getUserInfo("your")
        if(info == None):
            exit(-1)
        else:
            name,age,rating = info
            obj.setDetail(name, age, rating)

    else:
        print "Wrong Input"
        exit(-1)

    print "Authentication complete. Welcome"
    obj.showDetail()
    print "Proud to have you onboard"

    spy=obj

    start_chat()

