import json

try:
    with open("password.json","r") as file:
        data = json.load(file)
except:
    data = {}

if "passwords" not in data:
    data["passwords"]= []

if not data["passwords"]:
    print("No passwords found.")    
    
def save_data(data):
    with open("password.json","w") as file:
        json.dump(data,file,indent=4)

def user_input():
    print("for add password ->1")
    print("Search password by object->2")
    print("for show all passwords->3")
    choice = int(input("(1/2/3) => "))
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    elif choice == 3:
        return 3
    else:
        print("Invalid Input.")

def add_pass():
    obj = input("Enter Object:")
    pas = input("Enter Password:")

    entry = {
        "Object": obj,
        "password": pas
    }
    data["passwords"].append(entry)
    save_data(data)

def searchh():
    obj = input("Enter Object:").lower()
    found = False
    for i in data["passwords"]:
        if i["Object"] == obj:
            print("*"*40)
            print(f"Password for {obj} is {i['password']}")
            print("*"*40)
            found = True
            break
    if not found:
        print("Object not found.")

def show_all():
    for i in data["passwords"]:
        print("*"*40)
        print(f"{i['Object']} :: {i['password']}")

def main():
    while True: 
        a = user_input()
        if a == 1:
            add_pass()
        elif a == 2:
            searchh()
        elif a == 3:
            show_all()
        else:     
            break
    

main()