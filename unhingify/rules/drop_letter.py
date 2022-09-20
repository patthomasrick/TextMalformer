from random import random, randint
from ..rule import Rule


class DropLetterRule(Rule):
    def __init__(self, chance: float = 0.1):
        self.chance = chance

    def apply(self, text: str) -> str:
        words = text.split()
        for index, word in enumerate(words):
            if random() < self.chance:
                # Drop a random letter in the word.
                to_drop = randint(0, len(word) - 1)
                words[index] = word[:to_drop] + word[to_drop + 1 :]
        return " ".join(words)
