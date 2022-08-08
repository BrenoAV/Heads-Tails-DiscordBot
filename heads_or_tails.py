import random


class HeadsOrTails:
    """Control the game Heads or Tails, the players' names, your guesses, and the result of the game.
    """

    GUESSES = ('Heads', 'Tails')

    def __init__(self) -> None:
        self.name_player1 = None
        self.guess_player1 = None
        self.name_player2 = None
        self.guess_player2 = None
    
    def new_game(self) -> None:
        """Reset the game
        """
        self.name_player1 = None
        self.name_player2 = None
        self.guess_player1 = None
        self.guess_player2 = None

    def set_player1(self, name:str=None, guess:str=None) -> None:
        self.name_player1 = name
        self.guess_player1 = guess
    
    def get_player1(self):
        return self.name_player1, self.guess_player1

    def set_player2(self, name:str=None, guess:str=None) -> None:
        self.name_player2 = name
        self.guess_player2 = guess
    
    def get_player2(self):
        return self.name_player2, self.guess_player2

    def play(self):
        """Play a game after the players are set.

        Returns:
            tuple: 
            [0] - it is the result (HEADS or TAILS)
            [1] - it is the winning player
            [2] - it is a message to print on channel 
        """
        choice = random.choice(HeadsOrTails.GUESSES)
        
        if self.get_player1()[1] == choice:
            return (choice, 1, f'The **Player {self.get_player1()[0]}** wins \N{THUMBS UP SIGN} !')
        else:
            return (choice, 2, f'The **Player {self.get_player2()[0]}** wins \N{THUMBS UP SIGN} !')
        
            