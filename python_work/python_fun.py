class Bad_Name(Exception):
    pass

class Wrong_Type(Exception):
    pass

name_list = ["austin","brandon","carl","david","emily","frank","gary","henry"]
count = 3
while count > 0:
    name = input("Enter a name: ")
    try:
        if name.lower() in name_list:
            print("What a great name!")
            break
        elif name[0].lower() in ["y","q","z"]:
            raise Wrong_Type
        else:
            raise Bad_Name
    except Bad_Name:
        print("That's a bad name!")
        count -= 1
        if count == 0:
            print("You suck at picking names! Ending...")
    except Wrong_Type:
        print("What kind of name starts with a",name[0] + "?!?")
        count -= 1
        if count == 0:
            print("You suck at picking names! Ending...")