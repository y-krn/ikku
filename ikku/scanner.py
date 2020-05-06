class Scanner:
    def __init__(self, exactly, nodes, rule):
        self.__exactly = exactly
        self.__nodes = nodes
        self.__rule = rule
        self.__count = 0
        self.__phrases = [[] for i in range(len(rule))]

    def scan(self):
        if self.has_valid_first_node():
            for node in self.__nodes:
                if self.consume(node):
                    if self.satisfied():
                        if not self.__exactly:
                            return self.__phrases
                else:
                    return
        if self.satisfied():
            return self.__phrases
        else:
            return

    def consume(self, node):
        if not node.element_of_ikku():
            return False
        if node.pronunciation_length() > self.max_consumable_length():
            return False
        if self.first_of_phrase() and not node.first_of_phrase():
            return False
        if node.pronunciation_length() == self.max_consumable_length() and not node.last_of_phrase():
            return False
        else:
            self.__phrases[self.phrase_index()].append(node)
            self.__count += node.pronunciation_length()
            return True

    def first_of_phrase(self):
        return self.__count in [sum(self.__rule[:i+1]) for i in range(len(self.__rule))]
    
    def has_full_count(self):
        return self.__count == sum(self.__rule)

    def has_valid_first_node(self):
        return self.__nodes[0].first_of_ikku()

    def has_valid_last_node(self):
        return self.__phrases[-1][-1].last_of_ikku()

    def max_consumable_length(self):
        return sum(self.__rule[:self.phrase_index()+1]) - self.__count

    def phrase_index(self):
        for i in range(len(self.__rule)):
            if self.__count < sum(self.__rule[:i+1]):
                return i
        return len(self.__rule) - 1

    def satisfied(self):
        return self.has_full_count() and self.has_valid_last_node()
