# Create your Game class logic in here.
import random
import phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []
        

    def create_phrases(self):
        return [phrase.Phrase('just do it'),
                phrase.Phrase('try not do or do not there is no try'),
                phrase.Phrase('any thing'),
                phrase.Phrase('break a leg'),
                phrase.Phrase('say hello to my little friend')]
        

    def get_random_phrase(self):
        
        return random.choice(self.phrases)
        

    def reset_the_game(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        

    def get_guess(self):
        get_answer = input("\nEnter a Letter: ").lower()
        if get_answer == 'quit':
            return exit()
        elif get_answer.isnumeric():
            print('\nPLEASE TYPE A LETTER\n')
            return Game.start(self)
        elif len(get_answer) > 1:
            print('\nPLEASE TYPE ONLY 1 LETTER\n')
            return Game.start(self)
        else:
            return get_answer


    def welcome(self):
        print('Welcome to PhraseHunters\nPlease guess a letter to finish the phrase\ntype "Quit" to exit\n')
        

    def start(self):
        self.welcome()
        wanna_play = input('Would you like to play?  ').lower()
        while True:
            self.active_phrase.check_complete(self.guesses)

            if wanna_play == 'y' or wanna_play == 'yes':
                print(f'Number Missed: {self.missed}')
                self.active_phrase.display(self.guesses)
                user_guess = self.get_guess()
                self.guesses.append(' ')
                self.guesses.append(user_guess)

            elif wanna_play == 'n' or wanna_play == 'no':
                exit()
            else:
                print('Please type yes or no')
                return Game.start(self)

            if not self.active_phrase.check_phrase(user_guess):
                self.missed = self.missed + 1

            if self.game_over():
                get_input = input("Would you like to start a new game?(y,n) : ")

                if get_input == 'y':
                    self.reset_the_game()
                else:
                    print("Hope you had FUN!!")
                    return exit()
    
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print("\nYou won!")
            if self.missed == 0:
                print('PERFECT!')
            else:
                print(f'Missed Attempts: {self.missed}')
            return True
        elif self.missed == 5:
            print("You lost!")
            return True
        else:
            return False        