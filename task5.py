print("Welcome to my real estate average price calculator!")

print("Enter the neighborhood name: ")
neighborhood = input()

print("Would you like to add the price of a house? y-(yes) or n-(no)")
answer = input()

count = 0
allHousePrice = 0

while answer == 'y':
    print("Enter house price:")
    housePrice = int(input())
    allHousePrice += housePrice
    count += 1

    print("Would you like to add the price of one more house?")
    answer = input()

avgHousePrice = allHousePrice / count

print(f"The average house price in {neighborhood} is {avgHousePrice}")