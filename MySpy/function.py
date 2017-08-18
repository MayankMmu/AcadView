from random import randint,random
from hashlib import md5

def getGuestInfo():
    string = str(md5(str(random()*10000)).hexdigest())
    string = string[:11]

    name = "Guest"+string
    age = randint(15,35)

    rating = 3 + random() * 2
    rating *= 10
    rating = int(rating)
    rating = float(rating)
    rating /=10;

    return [name,age,rating];

def getUserInfo(string):
        name = raw_input("Provide {} name here : ".format(string))

        if (not name.isalpha()):
            print "Invalid Name . Provide correct details."
            return None;

        salutation = raw_input(" Mr. or Ms.?: :")
        age = int(raw_input("Enter {} age : ".format(string)))

        if (age <= 12 or age >= 50):
            print "Invalid age .Provide correct details."
            return None;

        rating = float(raw_input("What {} rating ? : ".format(string)))

        if (rating < 0 or rating > 5):
            print "Invalid rating .Provide correct details."
            return None;

        name = salutation +" "+ name

        return [name,age,rating];

