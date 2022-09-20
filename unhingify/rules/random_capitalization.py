from random import random
from ..rule import Rule


class RandomCapitalizationRule(Rule):
    def __init__(self, chance: float = 0.5):
        self.chance = chance

    def apply(self, text: str) -> str:
        # Split.
        words = text.split(" ")
        for index, word in enumerate(words):
            if random() > self.chance:
                words[index] = word[0].upper() + word[1:].lower()
            else:
                words[index] = word.lower()
        return " ".join(words)
