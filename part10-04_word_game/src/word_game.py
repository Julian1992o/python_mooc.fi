# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)
                    
    

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")



class LongestWord(WordGame):
        def __init__(self, rounds):
            super().__init__(rounds)

        def round_winner(self, player1_word, player2_word):
            if len(player1_word) > len(player2_word):
                return 1
            elif len(player2_word) > len(player1_word):
                return 2
            else:
                return 0
            
class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
            
        a = 0
        b = 0

        for i in player1_word:
            if i in "aoueiAOUEI":
                a += 1

        for i in player2_word:
            if i in "aoueiAOUEI":
                b += 1
        
        if a > b:
            return 1
        elif b > a:
            return 2
        else:
            return 0
        
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid = ["rock", "paper", "scissors"]

        # beide ungültig → unentschieden
        if player1_word not in valid and player2_word not in valid:
            return 0
        # einer ungültig → der andere gewinnt
        if player1_word not in valid:
            return 2
        if player2_word not in valid:
            return 1

        # Regeln
        if player1_word == player2_word:
            return 0
        if (player1_word == "rock" and player2_word == "scissors") \
           or (player1_word == "scissors" and player2_word == "paper") \
           or (player1_word == "paper" and player2_word == "rock"):
            return 1
        else:
            return 2


if __name__ == "__main__":
    p = MostVowels(3)
    p.play()

