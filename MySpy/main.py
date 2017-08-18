#importng modules

from function import getGuestInfo , getUserInfo
from SpyClass import Spy
from globalDetail import spy,friends
from start_chat import start_chat

# only call by main
if __name__ == "__main__":
    print "Let's get started"
    #want to know user choice about login
    choice = raw_input('You want to start as guest Y/N : ')

    obj = Spy()

    if(choice == "y" or choice=="Y"):
        #getting guest user data
        name,age,rating = getGuestInfo()
        #setting user data
        obj.setDetail(name,age,rating)

    elif(choice=="n" or choice == "N"):
        # getting user data
        info = getUserInfo("your")
        #checking for error
        if(info == None):
            exit(-1)
        else:
            name,age,rating = info
            # setting user data
            obj.setDetail(name, age, rating)

    else:
        print "Wrong Input"
        exit(-1)

    print "Authentication complete. Welcome"
    obj.showDetail()
    print "Proud to have you onboard"

    spy=obj
    # sending to start chat for further execution
    start_chat()

