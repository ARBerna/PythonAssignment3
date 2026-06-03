import random

print("How many people are in your household?")
numPeople = int(input())

randPerson = random.randint(1, numPeople)

print(f"Alright! today it is the turn of Person {randPerson} to do the dishes!")