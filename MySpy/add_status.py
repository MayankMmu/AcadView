import re


class Add_message:

    status = None

    old_status = ["My name is Bond, James Bond", "Shaken, not stirred.", "Keeping the British end up, Sir"]

    @staticmethod
    def add_status():

        # checking previous status
        if Add_message.status is not None:
            print 'Your current status message is {} \n'.format(Add_message.status)

        else:
            print "You don't have any status message currently\n "

        # want to user choice about the status
        choice = raw_input("Do you want to select from the older status (y/n)? : ")
        if choice == "y" or choice == "Y":

            # showing pervious save status
            for i in range(len(Add_message.old_status)):
                print "{}. {}".format(i + 1, Add_message.old_status[i])

            ch = int(raw_input("\nChoose from the above messages. \n"))

            if ch > len(Add_message.old_status) or ch < 1:
                print "Invalid choice. Try again."

            else:
                Add_message.status = Add_message.old_status[ch - 1]
                print 'Your updated status message is: {}'.format(Add_message.status)

        elif choice == "N" or choice == "n":
            # getting new status
            new_message = raw_input("What status message do you want to set?:\n")

            # validating users input.
            if re.match(r"^.+$", new_message):
                # adding new status message to the list.
                Add_message.old_status.append(new_message)
                # setting the new sataus message
                Add_message.status = new_message
                print 'Your updated status message is: {}'.format(Add_message.status)
            else:
                print "You did not provided any status message. Try again."

        else:
            # wrong input
            print 'The option you chose is not valid! Press either y or n.'
