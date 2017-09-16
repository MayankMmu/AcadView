import MySQLdb

db = None
cursor = None


def connect():
    global db, cursor
    db = MySQLdb.Connect("localhost", "root", "Mayank.80", "spychat")
    cursor = db.cursor()


def register_db(data):
    global cursor, db
    try:
        sql = "INSERT INTO login(`uname`,`pass`)VALUES(\"{}\",\"{}\")".format(data[0], data[1])
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "Sql error"


def login_db(data):
    global cursor, db
    try:
        sql = "SELECT * FROM login WHERE uname = \"{}\" and pass=\"{}\"".format(data[0], data[1])
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return True
    except:
        print "Sql error"
    return False


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
    except:
        db.rollback()
        print "Sql error"


def getSpy():
    global cursor, db
    try:
        sql = "SELECT * FROM spydata"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except:
        print "Sql error"


def close():
    global db,cursor
    try:
        cursor.execute("UPDATE spydata SET isonline={} Where isonline = {}".format(False,True))
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == "__main__":
    connect()
    close()
