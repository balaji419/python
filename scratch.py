#welcome to my locker
import sys
import pyperclip
filename,user_name,website_name=sys.argv
with open ("passwords.txt",'a' ) as fileobj :
    passwords={}
    print ("It will collect details about username, website name, password")
    print("Give the username and password as an argument passed in filename")
    passwords['username']=[user_name]
    passwords['website_name']=[website_name]
    print (len((sys.argv)))
    if len(sys.argv)<4:
        password = pyperclip.paste()
        passwords['password']=password
    else:
        print("failure")

    for u,v in passwords.items():
        print(v)
