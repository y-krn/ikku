# require "ikku/bracket_state"
from .scanner import Scanner
from .bracket_state import BracketState
import itertools

class Song:

    DEFAULT_RULE = [5, 7, 5]

    def __init__(self, nodes, exactly = False, rule = []):
        self.exactly = exactly
        self.__nodes = nodes
        self.__rule = rule or self.DEFAULT_RULE
        self.__phrases = self.scan()
        self.__bracket_state = BracketState()

    @property
    def phrases(self):
        results = []
        for n in range(len(self.__phrases)):
            results.append([s.surface for s in self.__phrases[n]])
        return results

    def valid(self):
        if not self.__phrases:
            return False
        elif self.has_odd_parentheses():
            return False
        else:
            return True

    def has_odd_parentheses(self):
        self.__bracket_state.consume_all(self.surfaces)
        return self.__bracket_state.odd()

    @property
    def nodes(self):
        return [s.surface for s in list(itertools.chain.from_iterable(self.__phrases))]

    @property
    def rule(self):
        return self.__rule

    def scan(self):
        return Scanner(self.exactly, self.__nodes, self.rule).scan()

    @property
    def surfaces(self):
        return self.nodes
