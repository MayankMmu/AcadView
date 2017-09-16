from spy import Spy

#class for the spy friends inherit the spy
class Friends(Spy):
    #friend list
    friends = []
    no = 1

    def __init__(self):
        self.messages = []

    #adding a friend
    def add_friend(self):
        from user_data_function import getUserInfo

        info = getUserInfo("friend")
        #checking the info of friend
        if info is None:
            return
        #setting the data
        name, age, rating = info
        self.setDetail(name, age, rating)
        Friends.friends.append(self)
        print "You have {} friends".format(len(Friends.friends))

    #showing the friend data
    @staticmethod
    def show_friends():
        if len(Friends.friends)==0:
            print "You don't have friends"
            return
        print "Friend :"
        for friend in Friends.friends:
            friend.showDetail()
            print ""

    #select a friend from the list
    @staticmethod
    def select_a_friend():
        #if u don't have friend
        if len(Friends.friends) == 0:
            print "You don't have friends "
            return None
        #printing the friend name
        for i in range(len(Friends.friends)):
            print "{}.{} ".format(i + 1, Friends.friends[i].name)

        #choosing a friend
        choice = int(raw_input("Enter the Friend No."))

        #checking the choice is right
        if choice <= 0 or choice > len(Friends.friends):
            print "The input is not correct"
            return None
        return Friends.friends[choice - 1]

    @property
    def get_name(self):
        return self.name
