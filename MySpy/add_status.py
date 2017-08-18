
def add_status(status):
    from globalDetail import old_status

    if(status != None):
        print 'Your current status message is {} \n'.format(status)

    else:
        print "You don't have any status message currently\n "

    choice = raw_input("Do you want to select from the older status (y/n)? : ")
    if choice =="y" or choice == "Y":

        for i in range(len(old_status)):
            print "{}. {}".format(i+1,old_status[i])

        ch = int(raw_input("\nChoose from the above messages. \n"))

        if ch > len(old_status) or ch < 1:
            print "Invalid choice. Try again."

        else:
            status = old_status[ch-1]
            print 'Your updated status message is: {}'.format(status)

    elif choice == "N" or choice == "n":
        new_message = raw_input("What status message do you want to set?:\n")

        # validating users input.
        if not new_message.isalpha():
            # adding new status message to the list.
            old_status.append(new_message)
            status = new_message
            print 'Your updated status message is: {}'.format(status)
        else:
            print "You did not provided any status message. Try again."

    else:
        print 'The option you chose is not valid! Press either y or n.'

    return status;