print("Welcome to the airline! What membership do you have?\n-Velociraptor\n-Stegosaurus\n-Triceratops\n-T-Rex\n-Brachiosaurus\n-None")
membership = input()

dinoMemberships = {
    "Velociraptor": .05,
    "Stegosaurus": .10,
    "Triceratops": .15,
    "T-Rex": .30,
    "Brachiosaurus": .50
}

ticketPrice = 500
isValidInput = False

while isValidInput == False:
    if membership == 'Velociraptor':
        discount = ticketPrice - (ticketPrice * dinoMemberships['Velociraptor'])
        isValidInput = True
    elif membership == 'Stegosaurus':
        discount = ticketPrice - (ticketPrice * dinoMemberships['Stegosaurus'])
        isValidInput = True
    elif membership == 'Triceratops':
        discount = ticketPrice - (ticketPrice * dinoMemberships['Triceratops'])
        isValidInput = True
    elif membership == 'T-Rex':
        discount = ticketPrice - (ticketPrice * dinoMemberships['T-Rex'])
        isValidInput = True
    elif membership == 'Brachiosaurus':
        discount = ticketPrice - (ticketPrice * dinoMemberships['Brachiosaurus'])
        isValidInput = True
    elif membership == 'None':
        discount = ticketPrice
    else:
        print("Invalid input try again.", end=" ")
        membership = input()

print(f"Your discount is: {int(dinoMemberships[membership] * 100)}% and your ticket price is: {discount}")