# Asks user to input a number
userNumber = int(input("Input a number - "))

# Makes counter to the start of the number range desired
counter = 10

# Multiplies the usrs number from numbers 10-20
while counter <=20:
    print(str(counter) + "*" + str(userNumber) + "=" + str(counter*userNumber))
    counter = counter + 1