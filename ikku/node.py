import re

class Node:
    
    def __init__(self, surface, feature, stat):
        self.STAT_ID_FOR_NORMAL = 0
        self.STAT_ID_FOR_UNKNOWN = 1
        self.STAT_ID_FOR_BOS = 2
        self.STAT_ID_FOR_EOS = 3
        self.__surface = surface
        self.__feature = feature.split(',')
        self.__stat = stat

    def analyzable(self):
        return not self.bos() and not self.eos()

    def bos(self):
        return self.__stat == self.STAT_ID_FOR_BOS

    @property
    def conjugation1(self):
        return self.__feature[4]

    @property
    def conjugation2(self):
        return self.__feature[5]

    def eos(self):
        return self.__stat == self.STAT_ID_FOR_EOS

    def element_of_ikku(self):
        return self.normal()

    def first_of_ikku(self):
        if not self.first_of_phrase():
            return False
        if self.type == "記号" and not self.subtype1 in ["括弧開", "括弧閉"]:
            return False
        return True

    def first_of_phrase(self):
        if self.type in ["助詞", "助動詞"]:
            return False
        if self.subtype1 in ["非自立", "接尾"]:
            return False
        if self.subtype1 == "自立" and self.root_form in ["する", "できる"]:
            return False
        return True

    # def inspect
    #     to_s.inspect
    # end

    def last_of_ikku(self):
        if self.type in ["名詞接続", "格助詞", "係助詞", "連体化", "接続助詞", "並立助詞", "副詞化", "数接続", "連体詞"]:
            return False
        if self.conjugation2 == "連用タ接続":
            return False
        if self.conjugation1 == "サ変・スル" and self.conjugation2 == "連用形":
            return False
        if self.type == "動詞" and self.conjugation2 in ["仮定形", "未然形"]:
            return False
        if self.type == "名詞" and self.subtype1 == "非自立" and self.pronunciation == "ン":
            return False
        return True

    def last_of_phrase(self):
        return self.type != "接頭詞"

    def normal(self):
        return self.stat == self.STAT_ID_FOR_NORMAL

    @property
    def pronunciation(self):
        return self.__feature[8]

    def pronunciation_length(self):
        return len(self.pronunciation_mora())
        
    def pronunciation_mora(self):
        if not self.pronunciation == '':
            pronunciation = re.sub("[ぁ-ゔ]","[ァ-ヴ]",self.pronunciation)
            pronunciation = re.sub("[^アイウエオカ-モヤユヨラ-ロワヲンヴー]", "", pronunciation)
            return pronunciation
        else:
            return ''

    @property
    def root_form(self):
        return self.__feature[6]
 
    @property
    def stat(self):
        return self.__stat

    @property
    def subtype1(self):
        return self.__feature[1]

    @property
    def subtype2(self):
        return self.__feature[2]

    @property
    def subtype3(self):
        return self.__feature[3]

    @property
    def surface(self):
        return self.__surface

    @property
    def type(self):
        return self.__feature[0]
