import os
import json

if(os.path.exists("contacts.json")):
    with open ("contacts.json","r")as contact:
        contacts = json.load(contact)

else:
    contacts = []
name = input("Enter your name : ")
num = input("Enter your number : ")
email = input("Enter your email : ")    
contact = {"name": name,"num":num,"email":email}
contacts.append(contact)
with open ("contacts.json","w")as f:
    json.dump(contacts,f)
print(contact)


