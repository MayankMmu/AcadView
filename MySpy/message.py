import re
from datetime import datetime

from steganography.steganography import Steganography

from friends import Friends

from termcolor import colored

#Message passing b/w friend
class Message:
    #mata data of message
    def __init__(self):
        self._message = ""
        self.time = None
        self.sendto = None
        self.output_file = None

    #send message
    def send_secret_message(self):
        self.time = datetime.now()
        #calling method to get friend
        friend = Friends.select_a_friend()

        if friend is None:
            return
        self.sendto = friend.name

        #getting message in any cost
        while len(self._message) == 0:
            self._message = raw_input("Enter the message\n")
        #checking length
        if len(self._message) > 100:
            print "You talk to much .\n From now I am not your friend"
            Friends.friends.remove(friend)
        else:
            #message for specific words
            if self._message.upper() == "SOS":
                print "I will save you"
            elif self._message.upper() == "SAVE ME":
                print "You will be saved"
            elif self._message.upper() == "HELP":
                print "I will help "
            elif self._message.upper() == "HELLO":
                print "how you doin"

            Friends.no += 1
            self.output_file = "D:\pycharm\Acadview\MySpy\EncreptedImage\Output" + str(Friends.no) + ".jpg"

            #encrypting the message
            Steganography.encode("D:\pycharm\Acadview\MySpy\image\galaxy.jpg", self.output_file, self._message)
            #adding to message list
            friend.messages.append(self)

    #read message
    @staticmethod
    def read_secret_message():
        #getting the friend
        friend = Friends.select_a_friend()
        if friend is None:
            return
        #chrcking  message
        if len(friend.messages) <= 0:
            print "No message"
            return
        for i in range(len(friend.messages)):
            print "Message {}".format(i + 1)
        no = int(raw_input("Enter the Message no. to read"))
        if no <= 0 or no > len(friend.messages):
            print "Wrong input"
            return
        message = Steganography.decode(friend.messages[no - 1].output_file)
        print "The message is : {}".format(message)

    #printing message meta data
    @staticmethod
    def get_history():
        friend = Friends.select_a_friend()
        if friend is None:
            return
        if len(friend.messages) <= 0:
            print "No message"
            return
        for data in friend.messages:
            print colored(data.sendto, "red")
            print colored(data.time, "blue")
            print data._message
