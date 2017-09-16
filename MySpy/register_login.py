from database import register_db, login_db, connect, close
from re import search, match

#checking the password is strong or not
def get_pass_strength(password):
    # calculate password length
    pass_length = len(password) < 6

    # search for digit
    digit = search(r"\d", password) is None

    # search for upper case alphabet
    uppercase = search(r"[A-Z]", password) is None

    # search for lower case alphabet
    lowercase = search(r"[a-z]", password) is None

    # search for symbol
    symbol = search(r"[!@#$%&*()./[\\\]_{}|~" + r"]", password) is None

    # checking the password
    password_ok = not (pass_length or digit or uppercase or lowercase or symbol)
    return password_ok


#getting user data
def get_data():
    name = raw_input("Enter the User name")
    password = raw_input("Enter the password as Pa55W0rd_Must_3e@5tr0ng")
    if not match(r"[\w\s]{,20}", name):
        print " user name can have alphabet only "
        return
    if not get_pass_strength(password):
        print "Password must have Uppercase letter, Digit, Lowercase letter And Special symbol "
        return
    return (name, password)

#registring the user
def register():
    data = get_data()
    if data is None:
        print "Retry"
        return False
    register_db(data)
    return True

#login the user
def login():
    data = get_data()
    if data is None:
        print "Retry"
        return False
    result = login_db(data)
    return result


