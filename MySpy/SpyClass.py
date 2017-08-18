class Spy:
    def init(self):
        self.name=None
        self.age = None
        self.rating = None
        self.is_online = False

    def setDetail(self,name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True

    def showDetail(self):
        print "Name : {} \nAge : {} \nRating : {}".format(self.name,self.age,self.rating)



