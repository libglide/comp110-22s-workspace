"""EX03_Structured Wordle."""

__author__ = "730483498"


def contains_char(guess: str, character: str) -> bool:
    """Gives True for a correct letter at any index and False for the letter not being in the string."""
    assert len(character) == 1    # makes sure that the character string is 1 

    i: int = 0 
        
    while i < len(guess):
        if guess[i] == character:
            return True 
        else: 
            i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Gives string of emojis based on appearances of characters from secret word in guess."""
    assert len(guess) == len(secret)   # makes sure that the length of the guess is equal to the length of the secret word

    WHITE_BOX: str = "\U00002B1C"

    GREEN_BOX: str = "\U0001F7E9"

    YELLOW_BOX: str = "\U0001F7E8"

    e: str = ""
    i: int = 0
    while i < len(secret):  
        if guess[i] == secret[i]:
            e = e + GREEN_BOX   
        else:
            if contains_char(secret, guess[i]) is True:
                e = e + YELLOW_BOX
            else:
                e = e + WHITE_BOX 
        i = i + 1
    return e


def input_guess(length: int) -> str:
    """Prompts the user for a guess of the correct length of the secret."""
    response: str = input(f"Enter a {length} character word: ") 
    while length != len(response):
        response = input(f"That wasn't {length} chars! Try again: ")
    
    return response 


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    win: bool = False
    while turn <= 6 and not win:   # this will ensure that the program goes into the while loop while the turn is less than or equal to 6 and exits the loop when the user is past turn 6
        print(f"=== Turn {turn}/6 ===")
        response: str = input_guess(len(secret))  # calls the input guess function and prompts the user for a guess 
        print(emojified(response, secret))   # prints the emoji string
        if response == secret:
            win = True
        else:
            turn = turn + 1    # if the response does not equal secret then the program will add 1 to the turn in order to show the number of turn that the user is on 
    if win is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
        

if __name__ == "__main__":
    main()
