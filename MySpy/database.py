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
        sql = "SELECT * FROM login WHERE uname = \"{}\"".format(data[0])
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return True
    except:
        print "Sql error"
    return False


def insertSpy(name, age, rating, isonline):
    global cursor, db
    try:
        cursor.execute("DELETE FROM spydata")
        db.commit()

        sql = "INSERT INTO `spychat`.`spydata`(`name`,`age`,`rating`,`isonline`)VALUES(\"{}\",{},{},{})".format(name,
                                                                                                                age,
                                                                                                                rating,
                                                                                                                isonline)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "Sql error"
        return


def close():
    global db
    db.close()


if __name__ == "__main__":
    connect()
    close()
