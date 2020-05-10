from natto import MeCab
from .node import Node
import os

class Parser:
    def parse(self, text):
        m = MeCab()
        results = []
        for n in m.parse(text, as_nodes=True):
            tmp = Node(n.surface, n.feature, n.stat)
            if tmp.analyzable():
                results.append(tmp)
        return results
