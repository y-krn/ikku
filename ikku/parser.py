import MeCab
from .node import Node
import os

class Parser:
    def parse(self, text):
        m = MeCab.Tagger()
        m.parse("")
        n = m.parseToNode(text)
        results = []
        while n:
            tmp = Node(n.surface, n.feature, n.stat)
            if tmp.analyzable():
                results.append(tmp)
            n = n.next 
        return results
