import random

# A list of words are created

li = ['java', 'python', 'html', 'ruby', 'selenium', 'matlab', 'perl', 'cobol', 'pascal', 'able', 'about', 'account',
      'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement',
      'air', 'all',
      'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'answer', 'ant', 'any',
      'any', 'apparatus', 'apple', 'approval']


class Hangman:
    def __init__(self, tries=6, li=li):
        self.tries = tries
        self.li = li

    # Function for the Hangman game

    def play(self):
        # A random word from the list is selected
        word = random.choice(self.li)
        guess = list('_') * len(word)
        used_letters = ''
        tries = self.tries

        # While loop to check if the input letter is there in the word
        while tries:
            print(f'\nYou have {tries} tries left.' if tries > 1 else '\nYou have 1 try left.')
            print('Used letters:', *used_letters)
            print('Word:', *guess)
            letter = input('Guess a letter: ').lower()

            if letter in used_letters:
                print("Letter has been already used")
                continue

            used_letters += letter
            self.updateguesslist(guess, letter, word, tries)  # Guess list is being updated

            # checking to see if the word has been guessed or not
            guess_word = ''.join(guess)
            if guess_word.find(letter) > -1:
                if guess_word == word:
                    print(f'\nYou guessed the word {word} !')
                    break
            else:
                tries -= 1

        if guess_word != word:
            print("\nSorry! out of chances.Word is :", word)

    # Function to update the guess list
    def updateguesslist(self, guess, letter, word, tries):
        i = word.find(letter)
        while i != -1:
            guess[i] = letter
            i = word.find(letter, i + 1)
    

# Class object is created and called
game = Hangman()
game.play()

"""
1) For the project we use the randon library so that a random word is chosen from a list (line 1).
2) First we create a list with some words (line 4).
3) The Hangman class is defined (line 7).
4) The class constructor takes two arguments: "tries" (number of attempts available to the player) and "li" (list of words).
5) The "play" method is created which will choose a word from "li", (word=random.choice(self.li)). Then a "guess" list is created with empty underscores for each letter of the word and the length of "guess" is equal to the length of the chosen word.
An empty str "used_letters" is created that stores the letters that the player enters and are in the selected word (word).
6) The variable "tries" is initialized with the number of tries that the player has (previously defined in the constructor).
7) While loop repeats the number of times defined in "tries".
8) With each cycle, the number of attempts the player has left, the letters he has guessed and the position of each letter in "guess" are printed.
9) With an if conditional, it is checked that the letter that the player enters is in "used_letters". If so, a message is printed informing that the letter has already been used. If the letter has not been entered it is added to "used_letters".
10) The "guess" list is updated with the letter entered with the "updateguesslist" method. This method loops through the word and replaces the underscores if applicable.
11) With an if conditional, if the player enters the letters correctly, a message is printed on the screen. Otherwise the message "Sorry! out of chances.Word is: " and the word are printed.


Carl Archemetre	                cvrlix@gmail.com
David Guillermo Guzmán Garzón	dgguzmangr@gmail.com
Sony Johnson Kunnathuparambil	sonyjhnsn@gmail.com


"""
