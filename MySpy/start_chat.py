from add_status import Add_message
from friends import Friends
from message import Message
from database import close,connect


# menu driven console app
def start_chat():
    while True:
        print """What do you want to do?
        1. Add a status update
        2. Add a friend
        3. Send a secret message
        4. Read a secret message 
        5. Read Chats from a user 
        6. Close Application \n"""

        choice = None
        # getting choice of user
        try:
            choice = int(raw_input())
        except:
            print "Enter a digit"
        # setting status
        if choice == 1:
            Add_message.add_status()

        # making friends
        elif choice == 2:
            Friends.add_friend(Friends())


        elif choice == 3:
            Message().send_secret_message()

        elif choice == 4:
            Message.read_secret_message()

        elif choice == 5:
            Message.get_history()

        # exiting app
        elif (choice == 6):
            close()
            exit(0)

        else:
            print "Wrong choice"

if __name__ == '__main__':
    connect()
    start_chat()