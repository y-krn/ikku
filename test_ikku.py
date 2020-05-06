# encoding: utf8
from __future__ import unicode_literals
import unittest
from ikku.reviewer import Reviewer
from ikku.song import Song

class TestIkku(unittest.TestCase):

    def test_find_judge(self):
        reviewer = Reviewer()

        text = '古池や蛙飛び込む水の音'

        # with invalid song
        self.assertIsNone(reviewer.find('test'))

        # with valid song
        self.assertIsInstance(reviewer.find(text), Song)

        # with text including song
        self.assertIsInstance(reviewer.find('ああ' + text + 'ああ'), Song)

        # with text including song ending with 連用タ接続
        self.assertIsNone(reviewer.find('リビングでコーヒー飲んでだめになってる'))

        # with song ending with 仮定形
        self.assertIsNone(reviewer.find('その人に金をあげたい人がいれば'))

        # with song ending with 未然形 (い)
        self.assertIsNone(reviewer.find('学会に多分ネイティブほとんどいない'))

        # with song ending with ん as 非自立名詞
        self.assertIsNone(reviewer.find('古池や蛙飛び込むかかったんだ'))

    def test_reviewer_judge(self):
        reviewer = Reviewer()

        text = '古池や蛙飛び込む水の音'
        
        # with rule option and valid song
        self.assertTrue(reviewer.judge(text))

        # with rule option and invalid song
        self.assertFalse(reviewer.judge(text + 'ああ'))
        self.assertFalse(reviewer.judge('test'))

        # with phrase starting with independent verb (歩く)
        self.assertTrue(reviewer.judge('なぜ鳩は頭を振って歩くのか'))

        # with phrase including English
        self.assertFalse(reviewer.judge('Apple' + text))

        # with phrase ending with 接頭詞
        self.assertFalse(reviewer.judge('レバーのお汁飲んだので元気出た'))

        # with song starting with symbol
        self.assertFalse(reviewer.judge('、' + text))

        # with song ending with 連用タ接続 (撮っ)
        self.assertFalse(reviewer.judge('新宿の桜と庭の写真撮っ'))

        # with song including even parentheses
        self.assertTrue(reviewer.judge('古池や「蛙＜飛び込む＞」水の音'))

        # with song including odd parentheses
        self.assertFalse(reviewer.judge('古池や「蛙＜飛び込む」＞水の音'))

        # with song starting with parenthesis
        self.assertTrue(reviewer.judge('「' + text + '」'))

        # with song ending with サ変・スル in 連用形 (-し)
        self.assertFalse(reviewer.judge('炊きつけて画面眺めて満足し'))

        reviewer = Reviewer([4,3,5])

        # with rule option and valid song
        self.assertTrue(reviewer.judge('すもももももももものうち'))

        # with rule option and invalid song
        self.assertFalse(reviewer.judge(text))
 
    def test_reviewer_search(self):
        reviewer = Reviewer()

        text = '古池や蛙飛び込む水の音'

        # without song
        self.assertIsInstance(reviewer.search('test'), list)

        # with valid song
        self.assertIsInstance(reviewer.search(text), list)

        # with text including song
        self.assertIsInstance(reviewer.search('ああ' + text + 'ああ'), list)

if __name__ == '__main__':
    unittest.main()
