from add_status import Add_message
from friends import Friends
from database import close
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
            Add_message.add_status()

        #making friends
        elif (choice == 2):
            Friends.add_friend(Friends())


        elif (choice == 3):
            Friends.send_secret_message()
        elif (choice == 4):
            Friends.read_secret_message()
        elif (choice == 5):
            pass

        # exiting app
        elif (choice == 6):
            close()
            exit(0)
        else:
            print "Wrong choice"


