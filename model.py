import random

from move import Move

RULES = {Move.ROCK: Move.SCISSORS, Move.PAPER: Move.ROCK, Move.SCISSORS: Move.PAPER}
COUNTER = {Move.ROCK: Move.PAPER, Move.PAPER: Move.SCISSORS, Move.SCISSORS: Move.ROCK}


def calculate_computer_move(player_move: Move, strength=0.5) -> Move:
    """
    Calculate the computer move based on the player move and the strength of the computer.
    The strength is a float between 0 and 1, where 0 means the computer will play a random move
    and 1 means the computer will always play the move that beats the player move.
    Any strength in between changes the likelihood of the computer countering the player.
    :param player_move: the player move
    :param strength: the strength of the computer
    :return: the move the computer uses against the player
    """

    if random.random() < strength:
        return COUNTER[player_move]
    return Move(random.randint(1, 3))


class RPS:
    """
    A rock-paper-scissors game.
    """

    game_round = 0
    score = [0, 0]

    @classmethod
    def check_move(cls, player_move: Move, computer_move: Move) -> int:
        """
        Check the move of the player and the computer and return who won (1 -> player, -1 -> computer) or a 0 indicating
        a draw.
        :param player_move: the move of the player
        :param computer_move: the move of the computer
        :return: 1 if the player won, -1 if the computer won, 0 if it was a draw
        """

        if player_move == computer_move:
            return 0
        elif RULES[player_move] == computer_move:
            return 1
        else:
            return -1

    def play_round(self, player_move: Move, computer_move: Move) -> int:
        """
        Play a round of rock-paper-scissors. The difference between this method and the check_move method is that this
        method also updates the score and the round number.
        :param player_move: the move of the player
        :param computer_move: the move of the computer
        :return: 1 if the player won, -1 if the computer won, 0 if it was a draw
        """

        self.game_round += 1
        result = self.check_move(player_move, computer_move)
        if result == 1:
            self.score[0] += 1
        elif result == -1:
            self.score[1] += 1
        return result

    def reset(self) -> None:
        """
        Reset the game (round number and score).
        """

        self.game_round = 0
        self.score = [0, 0]
