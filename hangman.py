import random

food = ["rice", "momo", "pizza", "phuchka", "pastry", "burger", "biryani", "butter chicken", "chana masala", "dal makhani","rogan josh", "tandoori chicken", "masala dosa", "rasam", "sambar", "vindaloo", "kadhi chawal", "aloo paratha","rajma chawal", "korma", "saag", "pakora", "chaat", "vada pav", "samosa", "pav bhaji", "aloo tikki", "idli","dosa", "chole bhature", "gulab jamun", "barfi", "jalebi", "kulfi", "ras malai", "kheer", "lassi", "payasam"]

animals = ["panda", "cat", "dog", "lion", "tiger", "elephant", "giraffe", "bear", "rabbit", "monkey", "horse"]

birds = ["bluebird", "crow", "cuckoo", "dove", "duck", "eagle", "emu", "falcon", "finch", "flamingo", "goose", "hawk","hummingbird", "kingfisher", "macaw", "myna", "nightingale", "ostrich", "owl", "parrot", "peacock", "penguin","pigeon", "robin", "seagull", "sparrow", "swan", "swallow", "turkey", "woodpecker"]

programming_language = ["python", "java", "javascript", "c++", "c#", "ruby", "php", "go", "swift", "kotlin","typescript", "sql", "perl", "r", "rust", "scala", "dart", "objective-c", "html", "css","c", "assembly", "vb.net", "matlab", "delphi", "lua", "bash", "fortran", "ada", "cobol","lisp", "shell", "node.js", "corona"]

print("Welcome to the Hangman Game")
print("Choose a Category:")

choice = input("Enter your choice :\n1. Food  2. Animals  3. Birds  4. Programming Language: ")

if choice == '1':
    word_bank = food
elif choice == '2':
    word_bank = animals
elif choice == '3':
    word_bank = birds
elif choice == '4':
    word_bank = programming_language
else:
    print("Invalid choice! Exiting game...")
    exit()

word = random.choice(word_bank).lower()
guessedWord = ["_"] * len(word)
attempts = 10
guessed_letters = set()

print("\nLet's start! Guess the word")

while attempts > 0:
    print("\nWord:", " ".join(guessedWord))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Enter a single valid alphabet letter!")
        continue

    if guess in guessed_letters:
        print("⛔ Already guessed this letter!")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("🎯 Great guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")

    if "_" not in guessedWord:
        print("\n✨ Congratulations!! You guessed the word:", word.upper(), "🎉")
        break

if attempts == 0 and "_" in guessedWord:
    print("\n💀 Game Over! The word was:", word.upper())
