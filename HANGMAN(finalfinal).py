import random
import colorama
from colorama import Fore,Back,Style


#IS_GAME_FINISHED = False

def hangmanGame():
    words_list = ["DEATH","HUMAN","EARTH","CAMERA","DOMAIN","ATTACK","AIRPORT","CLIMATE","GALLERY","PROGRAM",
              "CALENDAR","CHAMPION","PEACEFUL","UMBRELLA","PAINTING","VIOLENCE", "SPEED", "MOMENTUM",
              "CRIMINAL","ROMANTIC","SUSPECT","NETWORK","ELEMENT","ADVANCE","BLOOD","YIELD","YOUTH",
              "VITAL","ROUTE","RIVAL","QUEEN","TANGIBLE","SOFTWARE","FUNCTION","UNION","SMOKE"]
    
    #INITIALIZATIONS
    RAND_WORD = random.choice(words_list)
    MAX_GUESS = 8
    user_guessed_letters = ""
    valid_inputs = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #print(f"This prints valid input {valid_inputs}")
    while True:
        picked_rand_word = ""

        for RAND_LETTER in RAND_WORD:
            if RAND_LETTER in user_guessed_letters:
                picked_rand_word += RAND_LETTER
            else:
                picked_rand_word += "_ "


        if picked_rand_word == RAND_WORD:
            print(f"\n\nCongratulations! The hidden word is {Fore.GREEN}{picked_rand_word}{Fore.RESET}")
            print("You guessed the correct word, You saved a man!\n\n")
            print("      Thank you for saving me!....... Now I will commit great crime ( ͡° ͜ʖ ͡°).")
            print("    \O\n     |\ \n    / \ \n")
            break


        print("Guess the word: ", picked_rand_word)
        user_guess = input().upper()
        if user_guess in valid_inputs:
            user_guessed_letters += user_guess
        else:
            #print("Please enter a valid letter: ")
            print("That is not a valid letter, Use only letters found in the English alphabet.")
            user_guess = input().upper()


        if user_guess not in RAND_WORD:
            MAX_GUESS -= 1
            if MAX_GUESS == 7:
                #adds the pole
                print("7 Guesses left")
                print("----------\n|     \n|\n|\n|")
                #adds the head
            if MAX_GUESS == 6:
                print("6 Guesses left")
                print("----------\n|     O\n|\n|\n|")
            if MAX_GUESS == 5:
                #adds the body
                print("5 Guesses left")
                print("----------\n|     O\n|     |\n|\n|")
            if MAX_GUESS == 4:
                #adds the first arm
                print("4 Guesses left")
                print("----------\n|     O\n|    /|\n|     \n|")
            if MAX_GUESS == 3:
                #adds the first leg
                print("3 GUESSES LEFT")
                print("----------\n|     O\n|    /|\n|    /\n|")
            if MAX_GUESS == 2:
                #adds the second arm
                print("2 GUESSES LEFT")
                print("----------\n|     O\n|    /|\ \n|    /  \n|")
            if MAX_GUESS == 1:
                #adds the third leg
                print("LAST GUESS")
                print("----------\n|     O\n|    /|\ \n|    / \ \n|")
            if MAX_GUESS == 0:
                #death of hangman
                print(f"\n\nThe hidden word was {Fore.RED}{RAND_WORD}{Fore.RESET}\n\n  D E A T H befalls the hanged man\n   May he find peace in the afterlife")
                print("----------\n|   |_O   oh im die\n|    /|\ \n|    / \ \n|")
                break
                #print("Would you like to play again?")
    


print("-----------------------------------")
print(f"           {Fore.RED}{Back.RED}{Style.DIM}H A N G M A N{Style.RESET_ALL}           ")
print("-----------------------------------")

USER_INPUT = input("Enter your name: ").title()
print()

print(f"Hello {Fore.CYAN}{USER_INPUT}{Fore.RESET}.\n  I'm feeling a bit...  spicy\n   Let's play a game of {Fore.RED}Hangman{Fore.RESET}.\n    Okay I have chosen a random word for you to guess\n     Good luck!\n")
hangmanGame()