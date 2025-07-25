from random import randint

secret_number = randint(1, 10)  # Generate once and reuse
attempt = 0

for i in range(1, 10):
    guess = int(input("Guess the number (1 to 10): "))
    attempt += 1

    if guess == secret_number:
        print("Yay! Your guess is correct!", "Attempts:", attempt)
        break
    elif guess < secret_number:
        print("Enter a higher value!")
    else:
        print("Enter a lower value!")
