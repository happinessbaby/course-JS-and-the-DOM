#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.computer_move = my_move
        self.human_move = their_move
        pass

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if (self.p1.beats(move1, move2)):
            print(f"Player 1 wins\n")
            self.count1 += 1
        elif (self.p2.beats(move2, move1)):
            print(f"Player 2 wins\n")
            self.count2 += 1
        else:
            print(f"It's a tie\n")
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        if self.count1 > self.count2:
            print("Player 1 wins the game!")
        elif self.count2 > self.count1:
            print("Player 2 wins the game!")
        else:
            print("Player 1 and Player 2 tied!")
        print("\n\n Game over! \n\n")


class RandomPlayer(Player):
    def __init___(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        human_move = input("rock, paper, or scissors? \n")
        if human_move in moves:
            return human_move
        else:
            self.move()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.human_move = ""

    def move(self):
        if self.human_move == "":
            player = RandomPlayer()
            return player.move()
        else:
            return self.human_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.computer_move = ""

    def move(self):
        other_moves = [val for val in moves if val != self.computer_move]
        return random.choice(other_moves)


if __name__ == '__main__':
    while True:
        choice = input("Enter 1 to play with a computer\n" +
                       "Enter 2 for computer to play itself\n" +
                       "Enter 3 to enter the reflect mode\n" +
                       "Enter 4 to enter the cycle mode\n" +
                       "Enter quit to exit\n\n")
        if choice == "1":
            print("\nYou'll be Player 1\n")
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
        elif choice == "2":
            game = Game(RandomPlayer(), RandomPlayer())
            game.play_game()
        elif choice == "3":
            print("\nYou'll be Player 1\n")
            game = Game(RandomPlayer(), ReflectPlayer())
            game.play_game()
        elif choice == "4":
            print("\nYou'll be Player 1\n")
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
        elif choice == "quit":
            quit()
