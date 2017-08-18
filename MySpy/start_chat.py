from add_status import add_status
from globalDetail import status

#menu driven console app
def start_chat():
    while(True):
        print """What do you want to do?
        1. Add a status update
        2. Add a friend
        3. Send a secret message
        4. Read a secret message 
        5. Read Chats from a user 
        6. Close Application \n"""

        # getting choice of user
        choice = int(raw_input())

        # setting status
        if(choice == 1):
            global status
            status=add_status(status)

        #making friends
        elif (choice == 2):
            from function import getUserInfo
            from SpyClass import Spy
            from globalDetail import friends

            name,age,rating = getUserInfo("friend")
            obj = Spy()
            obj.setDetail(name,age,rating)
            friends.append(obj)
            print "You have {} friends".format(len(friends))


        elif (choice == 3):
            pass
        elif (choice == 4):
            pass
        elif (choice == 5):
            pass

        # exiting app
        elif (choice == 6):
            exit(0)
        else:
            print "Wrong choice"


