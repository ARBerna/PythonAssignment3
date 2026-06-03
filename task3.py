print("What is your favorite fictional character's name?")
ficChar = input()

print("What is your name?")
yourName = input()

if len(ficChar) == len(yourName):
    print("length is the same, coincidence? I think not!")
if ficChar[0] == yourName[0]:
    print("same first letter, coincidence? I think not!")