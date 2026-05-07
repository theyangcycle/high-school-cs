num = int(input("Enter the correct number for the game:\n"))
print("Guess the number between 1 and 100.")
while True:
    try:
        guess = float(input())
        if guess == num:
            print('You got it!')
            break
        elif guess > num:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
    except:
        print("Invalid input. Please enter a number.")