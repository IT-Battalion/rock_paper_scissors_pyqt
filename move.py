from enum import IntEnum, unique, auto


@unique
class Move(IntEnum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
