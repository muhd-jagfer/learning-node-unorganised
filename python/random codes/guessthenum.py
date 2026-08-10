def computer_guess():
    low = 1
    high = 100

    print("Think of a number between 1 and 100.")
    print("I'll try to guess it!")
    print()

    guesses = 0

    while True:
        guess = (low + high) // 2
        guesses += 1

        response = input(
            f"Is your number {guess}? "
            "(h = too high, l = too low, c = correct): "
        ).strip().lower()

        if response == "c":
            print(f"\nI guessed your number in {guesses} guesses!")
            break

        elif response == "h":
            high = guess - 1

        elif response == "l":
            low = guess + 1

        else:
            print("Please enter h, l, or c.")
            continue

        if low > high:
            print("\nHmm... your answers are inconsistent!")
            break


if __name__ == "__main__":
    computer_guess()