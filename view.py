from PyQt6.QtWidgets import *
from PyQt6 import uic

from move import Move

LABELS = {Move.ROCK: "rock", Move.PAPER: "paper", Move.SCISSORS: "scissors"}


class View(QMainWindow):
    l_round: QLabel
    l_score_player: QLabel
    l_score_computer: QLabel
    l_move_player: QLabel
    l_move_computer: QLabel

    rb_move_rock: QRadioButton
    rb_move_paper: QRadioButton
    rb_move_scissors: QRadioButton

    pb_play_move: QPushButton

    action_quit: QWidgetAction
    action_reset: QWidgetAction

    statusbar: QStatusBar

    def __init__(self, c):
        super().__init__()
        uic.loadUi("RockPaperScissors.ui", self)
        self.reset()
        self.pb_play_move.clicked.connect(c.play_move)
        self.action_reset.triggered.connect(c.reset)

    def reset(self) -> None:
        self.l_round.setText("0")
        self.l_score_player.setText("0")
        self.l_score_computer.setText("0")
        self.l_move_player.setText("last move")
        self.l_move_computer.setText("last move")
        self.rb_move_rock.setChecked(True)
        self.statusbar.showMessage(
            "Please choose a move and click play move to play against the computer.")

    def display_move(self, player_move: Move, computer_move: Move) -> None:
        self.l_move_player.setText(LABELS[player_move])
        self.l_move_computer.setText(LABELS[computer_move])

    def display_result(self, result: int) -> None:
        if result == 0:
            self.statusbar.showMessage("Draw!")
        elif result == 1:
            self.statusbar.showMessage("Player wins!")
        elif result == -1:
            self.statusbar.showMessage("Computer wins!")

    def display_score(self, score_player: int, score_computer: int) -> None:
        self.l_score_player.setText(str(score_player))
        self.l_score_computer.setText(str(score_computer))

    def display_round(self, game_round: int) -> None:
        self.l_round.setText(str(game_round))

    def get_player_move(self) -> Move:
        if self.rb_move_rock.isChecked():
            return Move.ROCK
        elif self.rb_move_paper.isChecked():
            return Move.PAPER
        elif self.rb_move_scissors.isChecked():
            return Move.SCISSORS


if __name__ == '__main__':
    import sys

    app = QApplication([])
    v = View()
    v.show()
    sys.exit(app.exec())
