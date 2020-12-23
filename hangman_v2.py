import random
import string

default_words = ['python', 'java', 'kotlin', 'javascript']


class Hangman:
    """
    Classic Hangman game
    """

    def __init__(self, words=None, lives=8, autostart=True):
        """
        Setup class
        :param words: iterable object of string. If not given, defaults will be used.
        :param lives: Initial count of lives.
        :param autostart: Enter the menu after instantiation.
        """

        if words:
            self.words = set(words)
        else:
            self.words = set(default_words)

        self.lives = lives

        print('H A N G M A N')

        if autostart:
            self.menu()

    def menu(self):
        """
        Menu in a loop.
        Asks for play or exit
        :return: None
        """
        while True:
            user_choice = input('Type "play" to play the game, "exit" to quit: ').lower()

            if user_choice == 'exit':
                break

            if user_choice == 'play':
                self.play()

    def play(self):
        """
        A single game round.
        :return: None
        """

        lives = self.lives
        correct_answer = list(random.choice(list(self.words)))
        guess_status = ['-'] * len(correct_answer)
        guessed_chars = set()

        while lives > 0:
            print('\n' + ''.join(guess_status))
            print(f'You have {lives} lives remaining.')

            char = input('Input a letter: ').lower()

            if char == 'exit':
                break

            if len(char) != 1:
                print('You should input a single letter')

            elif char not in string.ascii_lowercase:
                print('It is not an ASCII lowercase letter')

            elif char in guessed_chars:
                print('You already typed this letter')

            elif char not in correct_answer:
                print('No such letter in the word')
                lives -= 1
                guessed_chars.add(char)

            else:
                for j in range(len(correct_answer)):
                    if correct_answer[j] == char:
                        guess_status[j] = char
                        guessed_chars.add(char)

            if guess_status == correct_answer:
                print('You guessed the word!\nYou survived!')
                break

        else:
            print('You are hanged!\n')


if __name__ == "__main__":
    # Gleich starten, wenn die Datei direkt ausgeführt wird.
    h = Hangman()
 
