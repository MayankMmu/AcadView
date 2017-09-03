#created for function sepration
# reusablity of code


from random import randint,random
from hashlib import md5
import re

#creating guest user data
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

#getting user input and sending back
def getUserInfo(string):
        name = raw_input("Provide {} Name here : ".format(string))

        if not re.match(r"^[a-zA-Z ]+$",name):
            print "Invalid Name . Provide correct details."
            return None;

        salutation = raw_input(" Mr. or Ms.?: :")
        if salutation.capitalize()=="Mr" or salutation.capitalize()=="Ms":
            salutation = salutation+"."
        elif salutation.capitalize() == "Mr." or salutation.capitalize() == "Ms.":
            pass
        else:
            print "Enter correct salutation "
            return None

        age = raw_input("Enter {} Age : ".format(string))

        if not re.match(r"^[2-4]\d|1[2-9]|50$", age):
            print "Invalid age .Provide correct details."
            return None;
        age = int(age)

        rating = raw_input("What {} Rating ? : ".format(string))

        if not re.match("^[1-4]\.\d*|[0]\.[1-9]*|5\.0*|[1-5]$",rating) :
            print "Invalid rating .Provide correct details."
            return None;
        rating = float(rating)
        name = name.capitalize()
        salutation = salutation.capitalize()
        name = salutation +" "+ name

        return [name,age,rating];

