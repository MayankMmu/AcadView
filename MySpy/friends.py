from spy import Spy


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

        if len(Friends.friends) == 0:
            print "You don't have friends "
            return None

        for i in range(len(Friends.friends)):
            print "{}.{} ".format(i + 1, Friends.friends[i].name)

        choice = int(raw_input("Enter the Friend No."))

        if choice <= 0 or choice > len(Friends.friends):
            print "The input is not correct"
            return None
        return Friends.friends[choice - 1]

    @property
    def get_name(self):
        return self.name
