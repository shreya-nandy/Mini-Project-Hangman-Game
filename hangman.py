import random

# ------------------ WORD BANK ------------------
categories = {
    "1": ("Food", ["rice", "momo", "pizza", "phuchka", "pastry", "burger", "biryani", "butter chicken", "chana masala", "dal makhani", "rogan josh", "tandoori chicken", "masala dosa", "rasam", "sambar", "vindaloo", "kadhi chawal", "aloo paratha", "rajma chawal", "chole bhature"]),
    "2": ("Animals", ["panda", "cat", "dog", "lion", "tiger", "elephant", "giraffe", "bear", "rabbit", "monkey", "horse"]),
    "3": ("Birds", ["crow", "eagle", "peacock", "sparrow", "parrot","penguin", "owl", "duck", "flamingo"]),
    "4": ("Programming Languages", ["python", "java", "javascript", "c plus plus", "c sharp", "ruby", "php", "go", "swift", "kotlin"])
}

# ------------------ GAME START ------------------
print("🎮 Welcome to Hangman Game\n")
print("Choose a Category:")

for key, value in categories.items():
    print(f"{key}. {value[0]}")

choice = input("\nEnter your choice: ")

if choice not in categories:
    print("❌ Invalid choice! Exiting...")
    exit()

word = random.choice(categories[choice][1]).lower()

# Pre-fill spaces automatically
guessed_word = [" " if ch == " " else "_" for ch in word]

max_attempts = 8
attempts = max_attempts
guessed_letters = set()

print("\n🎯 Game Started! Guess the word")

# ------------------ GAME LOOP ------------------
while attempts > 0:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    # Validation
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Enter a single alphabet letter only!")
        continue

    if guess in guessed_letters:
        print("⛔ Already guessed!")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i, ch in enumerate(word):
            if ch == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")

    # WIN CONDITION
    if "_" not in guessed_word:
        attempts_used = max_attempts - attempts
        print("\n🎉 YOU WIN!")
        print(f"The word was: {word.capitalize()}")
        print(f"Attempts used: {attempts_used}/{max_attempts}")
        break

# ------------------ GAME OVER ------------------
if attempts == 0:
    print("\n💀 GAME OVER!")
    print(f"The word was: {word.capitalize()}")
    print(f"Attempts used: {max_attempts}/{max_attempts}")
