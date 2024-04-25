#! python3

"""
 Have the user enter a username 
 If the username is not "admin" then tell them it is an "invalid user", 
 but if it is, then ask them for a password 
 If they get the password correct (password is 12345password) 
 then display the message "Access granted"
 remember to use .strip() when retrieving strings or you will
 include hidden characters (the carriage return) that will
 not match
 1 marks

 Example:
 Enter username: admin
 Enter password: 12345password
 Access granted

 Enter username: notadmin
 invalid user

 Enter username: admin
 Enter password: password
 Access denied
"""

user = "admin"
password = "12345password"
userIn = str(input("Enter username: "))
if user == userIn:
    passwordIn = str(input("Enter password: "))
    if passwordIn == password:
        print("login sucsess")
        print("Wellcome to TempleOS x86_128!")
    else:
        print('error: incorrect password for user "admin"')
else:
    print("error: user does not exist.")