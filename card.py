from enum import Enum


class CardRank(Enum):
    ACE = 'ace'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    SEVEN = 'seven'
    EIGHT = 'eight'
    NINE = 'nine'
    TEN = 'ten'
    JACK = 'jack'
    QUEEN = 'queen'
    KING = 'king'


class CardSuit(Enum):
    HEARTS = 'hearts'
    SPADES = 'spades'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'


class Card:
    def __init__(self, rank: CardRank, suit: CardSuit, value: int):
        self._rank = rank
        self._suit = suit
        self._value = value
    
    @property
    def rank(self) -> CardRank:
        return self._rank
    
    @property
    def suit(self) -> CardSuit:
        return self._suit
    
    @property
    def value(self) -> int:
        return self._value

    def __str__(self):
        return f'{self.rank.value} of {self.suit.value}'
    

if __name__ == '__main__':
    for rank in CardRank:
        print(rank)
    card = Card(CardRank.ACE, CardSuit.HEARTS, 0)
    print(card)