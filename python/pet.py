class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def show_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger    : {self.hunger}/100")
        print(f"Energy    : {self.energy}/100")
        print(f"Happiness : {self.happiness}/100")

    def feed(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 20)
            self.happiness = min(100, self.happiness + 5)
            print(f"\nYou fed {self.name}.")
        else:
            print(f"\n{self.name} is already full!")

    def play(self):
        if self.energy >= 15:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 15
            self.hunger = min(100, self.hunger + 10)
            print(f"\nYou played with {self.name}!")
        else:
            print(f"\n{self.name} is too tired to play.")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)
        print(f"\n{self.name} had a nice nap.")

    def time_passes(self):
        self.hunger = min(100, self.hunger + 5)
        self.energy = max(0, self.energy - 5)
        self.happiness = max(0, self.happiness - 3)

    def is_alive(self):
        return self.hunger < 100 and self.happiness > 0


def main():
    print("=== Virtual Pet Simulator ===")
    pet_name = input("Name your pet: ")
    pet = VirtualPet(pet_name)

    while pet.is_alive():
        pet.show_status()

        print("\nChoose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Do Nothing")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            print(f"\nTime passes...")
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice.")

        pet.time_passes()

    if not pet.is_alive():
        print(f"\n💔 {pet.name} could not be cared for anymore.")
        print("Game Over!")


if __name__ == "__main__":
    main()