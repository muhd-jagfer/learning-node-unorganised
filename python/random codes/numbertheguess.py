import random

LOW = 1
HIGH = 100

secret = random.randint(LOW, HIGH)
attempts = 0
previous_distance = None

print("🎯 Number Guessing Game")
print(f"I'm thinking of a number between {LOW} and {HIGH}.")

while True:
    try:
        guess = int(input("\nYour guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess == secret:
        print(f"\n🎉 Correct! The number was {secret}.")
        print(f"You guessed it in {attempts} attempts.")
        break

    distance = abs(secret - guess)

    if guess < secret:
        print("📈 Too low!")
    else:
        print("📉 Too high!")

    if previous_distance is not None:
        if distance < previous_distance:
            print("🔥 Warmer!")
        elif distance > previous_distance:
            print("🧊 Colder!")
        else:
            print("😐 Same distance.")

    previous_distance = distance