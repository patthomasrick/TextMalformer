from collections import defaultdict
from typing import Dict, List
from unhingify.rule import Rule


class Transformer:
    rules: Dict[int, List[Rule]]

    def __init__(self):
        self.rules = defaultdict(list)

    def add_rule(self, rule: Rule, priority: int = 0):
        self.rules[priority].append(rule)

    def apply(self, text: str) -> str:
        for priority in sorted(self.rules.keys()):
            for rule in self.rules[priority]:
                text = rule.apply(text)
        return text
