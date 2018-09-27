"""
扑克牌的正确叫法应该是英美游戏牌（Anglo-American Playing Card）
或是法国牌组（French Deck），扑克（Poker）只是其中一种玩法，
由于进入中国时这种玩法最为流行，也连带着把这种纸牌称作扑克牌。
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    #__len__ 和__getitem__ 方法使FrenchDeck类似于Python自有的数据序列
    def __len__(self):
        return len(self._cards)

    #仅实现__getitem__方法，就可使对象可迭代
    def __getitem__(self, position):
        return self._cards[position]
