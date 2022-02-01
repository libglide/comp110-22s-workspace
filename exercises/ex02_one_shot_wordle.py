"""EX02_One shot Wordle."""

__author__ = "730483498"

secret: str = "python"  

response: str = input(f"What is your {len(secret)} guess? ") 

WHITE_BOX: str = "\U00002B1C"

GREEN_BOX: str = "\U0001F7E9"

YELLOW_BOX: str = "\U0001F7E8"

i: int = 0

e: str = ""

while len(secret) != len(response):
    response = input(f"That was not {len(secret)} letters! Try again: ")
# above the program is testing if the length of the guess is the same as the length of the secret word
while i < len(secret): 
    # If the length of the word is 6, so 5 indices this step is ensuring that we stay in the bounds of the index to avoid an infinite loop
    if response[i] == secret[i]:
        e = e + GREEN_BOX 
    else:
        f: bool = False
        ai: int = 0 
        while not f and ai < len(secret):
            # This loop is testing to see if there is a letter in the secret that matches any character in the response
            if secret[ai] == response[i]:
                f = True 
            else:
                ai = ai + 1 
        if f is True:
            e = e + YELLOW_BOX
        else: 
            e = e + WHITE_BOX

    i = i + 1

if response == secret:
    print(e)
    print("Woo! You got it!")
else:
    print(e)
    print("Not quite. Play again soon!")
