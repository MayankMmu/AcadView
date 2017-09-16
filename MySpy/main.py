# importng modules

from user_data_function import getGuestInfo, getUserInfo,get_old_user
from spy import Spy
from start_chat import start_chat
from database import connect
from register_login import register, login

# only call by main
if __name__ == "__main__":
    connect()
    log = False
    while not log:
        print "1.To Register "
        print "2. To Login"
        choice = raw_input("Enter your choice")
        if choice == "1":
            log = register()
        elif choice == "2":
            log = login()
        else:
            print "Wrong choice"

    print "Let's get started"
    # want to know user choice about login
    choice = raw_input('You want to start as guest Y/N : ')

    obj = Spy()

    if choice == "y" or choice == "Y":
        # getting guest user data
        name, age, rating = getGuestInfo()
        # setting user data
        obj.setDetail(name, age, rating)

    elif choice == "n" or choice == "N":
        choice = raw_input("Are you old user Y/N")
        if choice == "y" or choice =='Y':
            #getting old user data
            info = get_old_user()
        elif choice == "n" or choice == "N":
            # getting user data
            info = getUserInfo("your")
        # checking for error
        if info is None:
            print "Error in getting spy detail"
            exit(-1)

        name, age, rating = info
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
