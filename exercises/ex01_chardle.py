"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730483498"

word: str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) < 1:
    print("Error: Character must be a single character.")
    exit()

if len(letter) > 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0

print("Searching for " + letter + " in " + word)

if letter == word[0]:
    print(letter + " found at index 0")
    count = count + 1

if letter == word[1]:
    print(letter + " found at index 1")
    count = count + 1 

if letter == word[2]:
    print(letter + " found at index 2")
    count = count + 1

if letter == word[3]:
    print(letter + " found at index 3")
    count = count + 1

if letter == word[4]:
    print(letter + " found at index 4")
    count = count + 1 

if count == 0:
    print("No instances of " + letter + " in " + word)

if count == 1:
    print("1 instance of " + letter + " found in " + word)

if count == 2:
    print("2 instances of " + letter + " found in " + word)

if count == 3: 
    print("3 instances of " + letter + " found in " + word)

if count == 4:
    print("4 instances of " + letter + " found in " + word)

if count == 5:
    print("4 instances of " + letter + " found in " + word)