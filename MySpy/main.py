#importng modules

from user_data_function import getGuestInfo , getUserInfo
from spy import Spy
from start_chat import start_chat
from database import connect
from register_login import register,login
# only call by main
if __name__ == "__main__":
    connect()
    ("log = False\n"
     "    while not log:\n"
     "        print \"1.To Register \"\n"
     "        print \"2. To Login\"\n"
     "        choice = int(raw_input(\"Enter your choice\"))\n"
     "        if choice is 1:\n"
     "            log = register()\n"
     "        elif choice is 2:\n"
     "            log = login()\n"
     "        else:\n"
     "            print \"Wrong choice\"\n"
     "            ")




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

    # sending to start chat for further execution
    start_chat()

