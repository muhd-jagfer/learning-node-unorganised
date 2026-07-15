import string

print("=" * 40)
print("🔐 Password Strength Checker")
print("=" * 40)

while True:
    password = input("\nEnter a password (or type 'quit'): ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("• Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("• Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("• Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("• Add special characters.")

    print("\nResult:")

    if score == 5:
        print("🟢 Very Strong")
    elif score == 4:
        print("🟡 Strong")
    elif score == 3:
        print("🟠 Medium")
    else:
        print("🔴 Weak")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(item)