import random
from enum import Enum

from card import Card, CardRank, CardSuit


class DeckSetup(Enum):
    ACESLOW = 0
    ACESHIGH = 1


class Deck:
    def __init__(self, setup: DeckSetup = DeckSetup.ACESLOW):
        self.setup(setup)

    def setup(self, setup: DeckSetup) -> None:
        self._cards: list[Card] = []
        match setup:
            case DeckSetup.ACESLOW:
                for val, rank in enumerate(CardRank):
                    self._cards.extend(
                        [Card(rank, suit, val) for suit in CardSuit]
                    )
            case DeckSetup.ACESHIGH:
                ranks = [rank for rank in CardRank]
                ranks.append(ranks.pop(0))
                for val, rank in enumerate(ranks):
                    self._cards.extend(
                        [Card(rank, suit, val) for suit in CardSuit]
                    )
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)
    
    def draw(self) -> Card:
        return self._cards.pop(0)
        

if __name__ == '__main__':
    deck = Deck(DeckSetup.ACESHIGH)
    for card in deck._cards:
        print(card, card._value)
    
    deck.shuffle()

    for card in deck._cards:
        print(card, card._value)
    