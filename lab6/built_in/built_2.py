
def upper_lower(string):
    counterup = 0
    counterlow = 0
    for i in string:
        if i.isupper():
            counterup+= 1
        if i.islower():
            counterlow+= 1
    print("Lowercase letters:", counterlow)
    print("Uppercase letters:", counterup)
string = input("enter string: ")
upper_lower(string)
