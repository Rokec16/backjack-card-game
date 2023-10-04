import random


CARD_SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

CARD_RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
              'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

CARD_VALUES = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
               'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
               'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}


class Card:
    """A class representing a playing card.

    Attributes
    ----------
    suit : str
        the suit of cards that the card belongs to
    rank : str
        the rank of the card
    """

    def __init__(self, suit: str, rank: str) -> None:
        """
        Parameters:
        ----------
        suit : str
            the suit of cards that the card belongs to
        rank : str
            the rank of the card
        """

        self.suit = suit
        self.rank = rank
        self.value = CARD_VALUES[rank.lower()]

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    """A class representing a deck of playing cards.

    Attributes
    ----------
    cards : list
        A list of all playing cards in the deck, consisting of
        52 instances of the Card class.

    Methods
    ----------
    shuffle_cards : None
        Randomly shuffles cards in the deck.
    deal_one_card : Card
        Removes one card from the deck an returns it.
    """

    def __init__(self) -> None:
        """The deck is populated with 52 playing cards upon creation."""

        self.cards: list = []
        for suit in CARD_SUITS:
            for rank in CARD_RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self) -> str:
        return f'A deck of {self.__len__()} playing cards.'

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle_cards(self) -> None:
        """Randomly shuffles cards in the deck."""

        random.shuffle(self.cards)

    def deal_one_card(self) -> Card:
        """Removes one card from the deck an returns it."""

        return self.cards.pop()


if __name__ == "__main__":

    card = Card("Hearts", "Queen")
    print(card)

    deck = Deck()
    for card in deck.cards:
        print(card)

    print()

    player_card = deck.deal_one_card()
    print(player_card)

    print()

    deck.shuffle_cards()
    for card in deck.cards:
        print(card)
