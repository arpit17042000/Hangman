import random
import string
from words import words

def find_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=find_valid_word(words)
    word_letters=set(word)
    alphabets=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    
    while len(word_letters)>0 and lives>0:
        print("You have ", lives , "lives left and You have guessed these characters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word", ' '.join(word_list))
        #get user input
        user_letter=input("Enter a Character; ").upper()
        if user_letter in alphabets-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print("letter is not in the word")

        elif user_letter in used_letters:
            print("You have already guessed the character. Please try again")
    
        else:
            print("Invalid Character. Please try again")
    if(lives>0):
        print("Yay you have guessed the word correctly i.e., ", word)
    else:
        print("Sorry you werent able to guess the word ", word)
hangman()