from random import choice, random
from ..rule import Rule


class TyposRule(Rule):
    def __init__(self, chance: float = 0.5):
        self.chance = chance

        # Load typo dictionary.
        self.typo_dict = {}
        with open("data/typos.txt", "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line and line[0] != "#":
                    # Line is ___->___[, ___]
                    parts = line.split("->")
                    if len(parts) == 2:
                        correct = parts[0].strip()
                        typos = parts[1].strip().split(", ")
                        self.typo_dict[correct] = typos

    def apply(self, text: str) -> str:
        words = text.split()
        for index, word in enumerate(words):
            if random() < self.chance:
                if word in self.typo_dict:
                    words[index] = choice(self.typo_dict[word])
                elif word.lower() in self.typo_dict:
                    words[index] = choice(self.typo_dict[word.lower()])
        return " ".join(words)
