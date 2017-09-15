from database import register_db,login_db,connect,close
from re import search,match
def get_pass_strength(password):
    #calculate password length
    pass_length = len(password)<6

    #search for digit
    digit = search(r"\d",password) is None

    #search for upper case alphabet
    uppercase = search(r"[A-Z]",password) is None

    # search for lower case alphabet
    lowercase = search(r"[a-z]",password)is None

    # search for symbol
    symbol = search(r"[!@#$%&*()./[\\\]_{}|~"+r"]",password) is None

    #checking the password
    password_ok = not(pass_length or digit or uppercase or lowercase or symbol)
    return password_ok

def get_data():
    name = raw_input("Enter the User name")
    password = raw_input("Enter the password as Pa55W0rd_Must_3e@5tr0ng")
    if not match(r"[\w\s]{,20}",name):
        print " user name can have alphabet only "
        return
    if not get_pass_strength(password):
        print "Password don't have uppercase letter or digit or lower case letter or spcial symbol "
        return
    return (name,password)

def register():
    data = get_data()
    if data is None:
        print "Retry"
        return False
    register_db(data)
    return True

def login():
    data = get_data()
    if data is None:
        print "Retry"
        return False
    result = login_db(data)
    return result


if __name__ == "__main__":
    connect()
    #register()
    login()
    close()