from random import random
from ..rule import Rule


class ToLowerRule(Rule):
    def __init__(self, chance: float = 1.0):
        self.chance = chance

    def apply(self, text: str) -> str:
        # Split.
        words = text.split(" ")
        for index, word in enumerate(words):
            if random() < self.chance:
                words[index] = word.lower()
        return " ".join(words)
