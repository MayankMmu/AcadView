# creating class to store spy data
class Spy:
    def init(self):
        self.name=None
        self.age = None
        self.rating = None
        self.is_online = False

    #setter method
    def setDetail(self,name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True

    # showing data to user
    def showDetail(self):
        print "Name : {} \nAge : {} \nRating : {}".format(self.name,self.age,self.rating)



