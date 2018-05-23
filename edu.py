from random import randint
from time import sleep

class Game:

    def __init__(self):
        self.day = 1
        self.level = 1
        self.money = 5

    def learn(self):
        print("\nLearning......")
        self.level += 1
        self.money -=1
        self.day +=1

    def work(self):
        print("\nWorking......")
        self.money += self.level
        self.day += 1

    def rolldice(self):
        print('\n......Dice rolling......')
        sleep(2)
        dice = [randint(1, 6), randint(1, 6), randint(1, 6)]
        print('\nResult:', dice)
        print('\nSum:', sum(dice), end='')
        if (sum(dice) >= 11):
            print(' (Big)')
            return 'Big'
        else:
            print(' (Small)')
            return 'Small'

    def gamble(self):
        print('\nGambling......(Dice Game)')
        while True:
            bet = input('\nYour Bet (Max:{})'.format(self.money))
            try:
                bet = int(bet)
            except ValueError:
                print('\nPlease enter a valid number')
                continue
            # exceed the assets
            if bet > self.money:
                print('\nYou dont have enough money ')
                continue
            guess = input('\nYour Guess! [B]Big, [S]Small')
            if len(guess) < 1:  # check prevents a crash when indexing to 1st character
                continue
            guess = guess[0]
            if guess in ['b', 'B']:
                print('\nYou bet $', bet, ', and your choose is Big')
                guess = "Big"
            elif guess in ['s', 'S']:
                print('\nYou bet $', bet, ', and your choose is Small')
                guess = 'Small'
            else:
                print('\nInvalid Input!')
                continue

            truth = self.rolldice()

            if (guess == truth):
                self.money = self.money + bet * self.level
                self.day += 1
                print('\nYou win the game and earn $', bet * self.level)
                break
            else:
                self.money = self.money - bet
                self.day += 1
                print('\nYou lose the game and lose $', bet)
                break


if __name__ == '__main__':

    print('Welcome to the self exploration game!\n')

    name = input('Please type your name and press Enter.\n')
    print('\nHi,', name, 'Welcome to the game of education.')

    game = Game()
    while game.day <= 5 and game.money > 0:
        print('\n================================================================\n')
        print('| Day', game.day, '| Level', game.level, '| Money $', game.money, '|')

        print('\nThis is what you can do [1]Learn, [2]Work, [3]Gamble, [Q]Quit')
        command = input('\nType your choice and press Enter.')

        if len(command) < 1:  # check prevents a crash when indexing to 1st character
            continue
        command = command[0]
        if command in ['q', 'Q']:
            break  # exit the loop, which will quit the program
        elif command in ['1', 'l', 'L']:
            game.learn()
        elif command in ['2', 'w', 'W']:
            game.work()
        elif command in ['3', 'g', 'G']:
            game.gamble()
        else:
            print("\nInvalid Input!")

    print('\n================================================================')
    print('\nThank you for playing the game!')
    if game.money == 0:
        print('\nUnfortunately, you are broken :(')
    else:
        print('\nYour total money is', game.money)