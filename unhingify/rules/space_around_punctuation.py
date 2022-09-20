from random import random
from ..rule import Rule


class SpaceAroundPunctuationRule(Rule):
    def __init__(self, chance: float = 0.5):
        self.chance = chance

    def apply(self, text: str) -> str:
        to_find = [".", ",", "?", "!", ":", ";"]
        pos = 0
        while pos < len(text):
            if text[pos] in to_find and random() > self.chance:
                text = text[:pos] + " " + text[pos:]
                pos += 1
            pos += 1
        return text
