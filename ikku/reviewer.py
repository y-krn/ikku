from .parser import Parser
from .song import Song

class Reviewer:
    def __init__(self, rule = []):
        self.__parser = Parser()
        self.__rule = rule

    # Find one valid song from given text.
    # @return [Ikku::Song]
    def find(self, text):
        nodes = self.__parser.parse(text)
        for i in range(len(nodes)):
            song = Song(nodes[i:], exactly = False, rule = self.__rule)
            if song.valid():
                return song
        return None

    # Judge if given text is valid song or not.
    # @return [true, false]
    def judge(self, text):
        return Song(self.__parser.parse(text), exactly = True, rule = self.__rule).valid()

    # Search all valid songs from given text.
    # @return [Array<Array>]
    def search(self, text):
        nodes = self.__parser.parse(text)
        results = []
        for i in range(len(nodes)):
            song = Song(nodes[i:], exactly = False, rule = self.__rule)
            if song.valid():
                results.append(song)
        return results
