from spy import Spy
from steganography.steganography import Steganography
import re


class Friends(Spy):
    friends = []
    no = 1

    def __init__(self):
        self.messages = []

    def add_friend(self):
        from user_data_function import getUserInfo

        name, age, rating = getUserInfo("friend")
        self.setDetail(name, age, rating)
        Friends.friends.append(self)
        print "You have {} friends".format(len(Friends.friends))

    @staticmethod
    def show_friends():
        for friend in Friends.friends:
            super.showDetail(friend)

    @staticmethod
    def select_a_friend():

        if (len(Friends.friends) == 0):
            print "You don't have friends "
            return None

        for i in range(len(Friends.friends)):
            print "{}.{} ".format(i + 1, Friends.friends[i].name)

        choice = int(raw_input("Enter the Friend No."))

        if choice <= 0 or choice > len(Friends.friends):
            print "The input is not correct"
            return None
        return Friends.friends[choice - 1]

    @staticmethod
    def send_secret_message():
        friend = Friends.select_a_friend()
        if friend is None:
            return
        message = raw_input("Enter the message\n")
        if not re.match(r".{1,100}", message):
            print "Enter the message upto 100 letters"
        else:
            Friends.no += 1
            outputFile = "D:\pycharm\Acadview\MySpy\EncreptedImage\Output" + str(Friends.no) + ".jpg"

            Steganography.encode("D:\pycharm\Acadview\MySpy\image\galaxy.jpg", outputFile, message)
            Friends.add_message(friend, outputFile)

    @staticmethod
    def read_secret_message():
        friend = Friends.select_a_friend()
        if friend is None:
            return
        if len(friend.messages) <= 0:
            print "No message"
            return
        for i in range(len(friend.messages)):
            print "Message {}".format(i+1)
        no = int(raw_input("Enter the Message no. to read"))
        if no<=0 or no>len(friend.messages):
            print "Wrong input"
            return
        message = Steganography.decode(friend.messages[no-1])
        print "The message is : {}".format(message)


    def add_message(self, image):
        self.messages.append(image)
