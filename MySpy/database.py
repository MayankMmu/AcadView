import MySQLdb

db = None
cursor = None

#Connecting to data base
def connect():
    global db, cursor
    db = MySQLdb.Connect("localhost", "root", "Password", "spychat")
    cursor = db.cursor()

#register the user
def register_db(data):
    global cursor, db
    try:
        sql = "INSERT INTO login(`uname`,`pass`)VALUES(\"{}\",\"{}\")".format(data[0], data[1])
        cursor.execute(sql)
        db.commit()
    #in case an error occurred
    except:
        db.rollback()
        print "Sql error"

#login the user
def login_db(data):
    global cursor, db
    try:
        sql = "SELECT * FROM login WHERE uname = \"{}\" and pass=\"{}\"".format(data[0], data[1])
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return True
    # in case an error occurred
    except:
        print "Sql error"
    return False

#inserting the spy data
def insertSpy(name, age, rating, isonline):
    global cursor, db
    if "Guest" in name:
        return
    try:
        sql = "INSERT INTO `spychat`.`spydata`(`name`,`age`,`rating`,`isonline`)VALUES(\"{}\",{},{},{})".format(name,
                                                                                                                age,
                                                                                                                rating,
                                                                                                                isonline)
        cursor.execute(sql)
        db.commit()
    # in case an error occurred
    except:
        db.rollback()
        print "Sql error"

#getting the spy data
def getSpy():
    global cursor, db
    try:
        sql = "SELECT * FROM spydata"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    # in case an error occurred
    except:
        print "Sql error"


#closing the connection
def close():
    global db,cursor
    try:
        #changing the online status
        cursor.execute("UPDATE spydata SET isonline={} Where isonline = {}".format(False,True))
        db.commit()
    # in case an error occurred
    except:
        db.rollback()
    db.close()

