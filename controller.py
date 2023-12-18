import model
import view


class Controller:
    def __init__(self):
        self.model = model.RPS()
        self.view = view.View(self)

    def reset(self) -> None:
        self.model.reset()
        self.view.reset()

    def play_move(self) -> None:
        player_move = self.view.get_player_move()
        computer_move = model.calculate_computer_move(player_move)
        result = self.model.play_round(player_move, computer_move)

        self.view.display_round(self.model.game_round)
        self.view.display_score(self.model.score[0], self.model.score[1])
        self.view.display_move(player_move, computer_move)
        self.view.display_result(result)
