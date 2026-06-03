print("Enter a statement you want me to repeat!")
message = input()

print("Enter how many times you want me to print it?")
timesToPrint = int(input())

timesPrinted = 0

while timesPrinted != timesToPrint:
    print(message)
    timesPrinted += 1