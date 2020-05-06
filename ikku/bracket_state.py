import itertools

class BracketState:
    BRACKETS_TABLE = {
        "‘" : "’",
        "“" : "”",
        "（" : "）",
        "(" : ")",
        "［" : "］",
        "[" : "]",
        "{" : "}",
        "｛" : "｝",
        "〈" : "〉",
        "《" : "》",
        "「" : "」",
        "『" : "』",
        "【" : "】",
        "〔" : "〕",
        "<" : ">",
        "＜" : "＞",
    }

    def __init__(self):
        self.__stack = []
        self.__brackets_index = {v:True for v in list(itertools.chain.from_iterable(self.BRACKETS_TABLE.items()))}
        self.__inverted_brackets_table = {v:k for k,v in self.BRACKETS_TABLE.items()}

    def consume_all(self, surfaces):
        for surface in surfaces:
            self.__consume(surface)

    def odd(self):
        return not self.__even()

    def __consume(self, surface):
        if not self.__stack == [] and surface in self.__inverted_brackets_table and self.__inverted_brackets_table[surface] ==  self.__stack[-1]:
            self.__stack.pop()
        elif surface in self.__brackets_index:
            self.__stack.append(surface)

    def __even(self):
        return self.__stack == []
