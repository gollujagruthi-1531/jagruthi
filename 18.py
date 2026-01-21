secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

print("You guessed correctly")
