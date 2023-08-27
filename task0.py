#!/usr/bin/python3
##################################################
# login system
users={
    "Ahmed":1394,
    "Ali":6078,
    "Amr":9345
}
usernam=input("please enter user name: ")
password=int(input("enter password"))
if usernam in users and users[usernam]==password :
    print("Welcome")
else :
    print("incorrect")