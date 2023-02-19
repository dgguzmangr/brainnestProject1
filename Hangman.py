import random
# A list of words are created

li = ['java','python','html','ruby','selenium','matlab','perl','cobol','pascal','able','about','account','acid','across','act','addition','adjustment','advertisement','after','again','against','agreement','air','all',
        'almost','among','amount','amusement','and','angle','angry','animal','answer','answer','ant','any','any','apparatus','apple','approval']

class Hangman:
    def __init__(self, tries=6, li=li):
        self.tries = tries
        self.li = li
#Function for the Hangman game

    def play(self):
        # A random word from the list is selected
        word = random.choice(self.li)
        guess = list('_')*len(word)
        used_letters = ''
        tries = self.tries

        #While loop to check if the input letter is there in the word
        while tries:
            print(f'\nYou have {tries} tries left.' if tries>1 else '\nYou have 1 try left.')
            print('Used letters:', *used_letters)
            print('Word:', *guess)
            letter = input('Guess a letter: ').lower()
            
            if letter in used_letters:
                print("Letter has been already used")
                continue
            
            used_letters += letter
            self.updateguesslist(guess,letter,word) #Guess list is being updated

            # checking to see if the word has been guessed or not
            guess_word=''.join(guess)
            if guess_word.find(letter)>-1:
                if guess_word == word:
                    print(f'\nYou guessed the word {word} !')
                    break
            else:
                tries -= 1

        if guess_word != word:
            print("\nSorry! out of chances.Word is :",word)

#Function to update the guess list
    def updateguesslist(self, guess, letter, word):
        i = word.find(letter)
        while i!=-1:
               guess[i] = letter
               i = word.find(letter, i+1)



#Class object is created and called
game = Hangman()
game.play()