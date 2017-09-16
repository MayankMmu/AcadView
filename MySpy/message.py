import re
from datetime import datetime

from steganography.steganography import Steganography

from friends import Friends

from termcolor import colored


class Message:
    def __init__(self):
        self._message = ""
        self.time = None
        self.sendto = None
        self.output_file = None

    def send_secret_message(self):
        self.time = datetime.now()
        friend = Friends.select_a_friend()
        if friend is None:
            return
        self.sendto = friend.name
        if friend is None:
            return
        while len(self._message) == 0:
            self._message = raw_input("Enter the message\n")
        if len(self._message) > 100:
            print "You talk to much .\n From now I am not your friend"
            Friends.friends.remove(friend)
        else:
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

            Steganography.encode("D:\pycharm\Acadview\MySpy\image\galaxy.jpg", self.output_file, self._message)
            friend.messages.append(self)

    @staticmethod
    def read_secret_message():
        friend = Friends.select_a_friend()
        if friend is None:
            return
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
