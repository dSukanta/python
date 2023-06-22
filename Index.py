import mysql.connector
import sys

arguments= sys.argv

# print(arguments)





# print("Hello world!")


# def isEven(number):
#     if number%2 == 0:
#         print("Even!")
#     else:
#         print("Not even!")

# isEven(10)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="test"
)

# print(mydb)

mycursor= mydb.cursor()
# mycursor.execute("CREATE TABLE students (st_id int NOT NULL AUTO_INCREMENT,l_name varchar(255) NOT NULL,f_name varchar(255),PRIMARY KEY (st_id))")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)


def addStudent(f_name=None,l_name=None):
    if f_name==None:
        print("Please provide a Student First Name")
    elif l_name==None:
        print("Please Provide Student Last Name")
    else:
        query= "INSERT INTO students (l_name,f_name) VALUES (%s,%s)" 
        value= (l_name,f_name)
        mycursor.execute(query,value)
        mydb.commit()
        print(mycursor.rowcount,"record inserted successfully")


# addStudent(f_name="abc",l_name="xyz")


def logIn(username=None,password=None):
    if username==None or password==None:
        print("All fields are mandatory")
    else:
        query= "SELECT * FROM students WHERE f_name=%s"
        value= (username,)
        mycursor.execute(query,value)
        myresult= mycursor.fetchall()
        mydb.commit()
        # print(len(myresult),"find successfully")
        if len(myresult)<1:
            print("username is not valid.")
        else:
            # findpass= "select l_name from students where f_name=%s"
            # passvalue=(password,)
            # mycursor.execute(findpass,passvalue)
            # myres= mycursor.fetchall()
            # mydb.commit
            # print(len(myres))
            # print(myresult[0][1]) 
            if myresult[0][1]==password:
                print("Login Successfull")
            else:
              print("password is invalid.")
        

# logIn(username='sukanta',password="dolai") 

def resetPassword(username=None,oldpassword=None,newpassword=None):
    if username==None or oldpassword==None or newpassword==None:
        print("Please Confirm that you have enter username, current password and old password are correct.")
    else:
        query= "SELECT * FROM students WHERE f_name=%s"
        value= (username,)
        mycursor.execute(query,value)
        myresult= mycursor.fetchall()
        mydb.commit()
        if len(myresult)>0:
            if myresult[0][1]==oldpassword:
                query="UPDATE students SET l_name=%s WHERE f_name=%s"
                value=(newpassword,username)
                mycursor.execute(query,value)
                myresult= mycursor.fetchall()
                # print(myresult)
                mydb.commit()
                try:
                    print("Successfully password changed")
                except:
                    print("Something went wrong.")

            else:
                print("Invalid Password")
        else:
            print("Username not found. Regsiter instead")

def delUser(username=None, password=None):
    if username==None or password==None:
        print("invalid credentials")
    else:
        query= "SELECT * FROM students WHERE f_name=%s"
        value= (username,)
        mycursor.execute(query,value)
        myresult= mycursor.fetchall()
        mydb.commit()
        if len(myresult)>0:
            query="DELETE FROM students WHERE l_name=%s"
            value= (password,)
            mycursor.execute(query,value)
            myresult= mycursor.fetchall()
            mydb.commit()
            try:
                print("user deleted successfully")
            except:
                print("Something went wrong")

# if len(arguments)<=1:
#     print("Welcome !!!!")
# elif len(arguments)==2:
#     method=arguments[1]

#     print("Please enter your username")
# elif len(arguments)==3:
#     print("Please enter your password")
# elif len(arguments)>=4:
#     method=arguments[1]
#     email= arguments[2] or None
#     password= arguments[3] or None
#     newpassword= arguments[4]
#     if method=='login':
#         logIn(email,password)
#     elif method=='register':
#         addStudent(email,password)
#     elif method =='resetp':
#         resetPassword(email,password,newpassword)
#     elif method=='deluser':
#         delUser(email,password)
# else:
#     print("Not a valid method")
