import sqlite3
from django.contrib.auth import authenticate

try:
    con = sqlite3.connect(
        'C:/Users/ansh0/AppData/Local/Programs/Python/Python38/Lib/site-packages/django/Online_class/mydb.sqlite3', check_same_thread=False)
    print("success")
except:
    pass

db = con.cursor()
#db.execute("CREATE TABLE teacher(name text , password text, email varchar,number INTEGER PRIMARY KEY,admin BOOLEAN CHECK (admin IN (0, 1)))")
#db.execute("CREATE TABLE student(name text , password text, email varchar,number INTEGER PRIMARY KEY,groupid text);")
#db.execute("CREATE TABLE groupS(groupname text, groupdesc text, groupid INTEGER PRIMARY KEY ,time text,day text CHECK(day IN('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')));")
#db.execute("SELECT *,rowid FROM student")


def register_teacher(name, password, email, admin):
    statement = """INSERT INTO teacher
                          (name, password, email,admin) 
                          VALUES (?, ?, ?,?);"""

    data_tuple = (name, password, email, admin)
    db.execute(statement, data_tuple)
    con.commit()
    print("success")

# register_teacher('Aksh','Aksh1234','aksh@gmail.com')
# register_teacher('Himani','Himani1234','himani.bhatnagar@gmail.com',1)


def register_student(name, password, email, number, groupid):
    statement = """INSERT INTO student
                          (name, password, email,number,groupid) 
                          VALUES (?, ?, ?,?,?);"""

    data_tuple = (name, password, email, number, groupid)
    db.execute(statement, data_tuple)
    con.commit()
    print("success")
# register_student('Himani','Himani1234','himani.bhatnagar@gmail.com',8105077771,None)


def check_name(name):
    statement = f"SELECT name FROM student WHERE name='{name}';"
    db.execute(statement)
    confirm = (db.fetchall())
    print(confirm)
    if not confirm:
        return False
    else:
        return True
    con.commit()


def check_number(number):
    statement = f"SELECT number FROM student WHERE number={number};"
    db.execute(statement)
    confirm = (db.fetchall())
    print(confirm)
    if not confirm:
        return False
    else:
        return True
    con.commit()


def check_email(email):
    statement = f"SELECT email FROM student WHERE email='{email}';"
    db.execute(statement)
    confirm = (db.fetchall())
    print(confirm)
    if not confirm:
        return False
    else:
        return True
    con.commit()


# register_student('Ansh','Ansh1234','ansh@gmail.com')
# register_student('Aksh','Aksh1234','aksh@gmail.com')


def login_student(password, email):
    statement = f"SELECT password FROM student WHERE email='{email}';"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
    if new_string == password:
        return True
    else:
        return False
    con.commit()


def login_teacher(password, email):
    statement = f"SELECT password FROM teacher WHERE email='{email}';"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
    if new_string == password:
        return True
    else:
        return False
    con.commit()


def create_group(name, desc, time, day):
    statement = """INSERT INTO groupS
                          (groupname,groupdesc,time,day) 
                          VALUES (?, ?,?,?);"""
    data_tuple = (name, desc, time, day)
    db.execute(statement, data_tuple)
    con.commit()
    print("success")


def group_name():
    statement = f"SELECT groupname from groupS;"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    # print(new_string)
    li = list(new_string.split(" "))
    return li


def group_desc():
    statement = f"SELECT groupdesc from groupS;"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    # print(new_string)
    li = list(new_string.split(" "))
    return li


def group_id():
    statement = f"SELECT groupid from groupS;"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    # print(new_string)
    li = list(new_string.split(" "))
    return li


def group_time():
    statement = f"SELECT time from groupS;"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
    li = list(new_string.split(" "))
    return li


def group_day():
    statement = f"SELECT day from groupS;"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
    li = list(new_string.split(" "))
    return li


def get_students_from_group(groupid):
    statement = f"SELECT name from student WHERE groupid='{groupid}';"
    db.execute(statement)
    confirm = str(db.fetchall())
    characters_to_remove = "[('',)]"
    new_string = confirm
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    li = list(new_string.split(" "))
    return(li)


def check_group(groupname):
    statement = f"SELECT * FROM groupS WHERE groupname='{groupname}';"
    db.execute(statement)
    confirm = (db.fetchall())
    print(confirm)
    if not confirm:
        return False
    else:
        return True


def traverse(given_list):
    for i in given_list:
        return i


def update_student():
    pass


def update_teacher():
    pass


class Information:
    def __init__(self, name, email, password, phone, group):
        self.name = name
        self.email = email
        self.phone - phone
        self.password = password
        self.group = group

    def name(email):
        statement = f"SELECT name FROM student WHERE email='{email}';"
        db.execute(statement)
        db.execute(statement)
        confirm = str(db.fetchall())
        characters_to_remove = "[('',)]"
        new_string = confirm
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")
        li = list(new_string.split(" "))
        return(li)

    def password(email):
        statement = f"SELECT password FROM student WHERE email='{email}';"
        db.execute(statement)
        db.execute(statement)
        confirm = str(db.fetchall())
        characters_to_remove = "[('',)]"
        new_string = confirm
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")
        li = list(new_string.split(" "))
        return(li)

    def phone(email):
        statement = f"SELECT number FROM student WHERE email='{email}';"
        db.execute(statement)
        db.execute(statement)
        confirm = str(db.fetchall())
        characters_to_remove = "[('',)]"
        new_string = confirm
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")
        li = list(new_string.split(" "))
        return(li)

    def group(email):
        statement = f"SELECT groupid FROM student WHERE email='{email}';"
        db.execute(statement)
        db.execute(statement)
        confirm = str(db.fetchall())
        characters_to_remove = "[('',)]"
        new_string = confirm
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")
        li = list(new_string.split(" "))
        return(li)
