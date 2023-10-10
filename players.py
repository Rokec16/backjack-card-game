from cards import Card


class Hand:
    """Represents the cards that the player currently holds."""

    def __init__(self) -> None:
        """
        Parameters
        ----------
        cards : list
            List of all cards currently in the hand.
        value : int
            Value of the whole hand, all cards included.
        """

        self.cards: list = []
        self.value: int = 0
        self.aces: int = 0

    def add_card(self, card: Card):
        """Adds a card to the hand and adjusts hands value."""

        self.cards.append(card)
        self.value += card.value

        if card.rank.lower() == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        """Adjusts the hands value for aces held in that hand.

        Ace can have a value of either 1 or 11, depending on the total sum
        of card values currently held in the hand. If total value of the hand
        exceeds 21, then ace can be adjusted to be worth 1 instead of 11.
        """

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Player:
    """Representing a player of the card game."""

    def __init__(self, name: str, chips: int = 0) -> None:
        """
        Parameters:
        ----------
        name : str
            Name of the player.
        chips : int
            Amount of chips the player holds.
        bet : int
            Amount of chips the players placed as as bet.
        hand : Hand
            Cards the player holds.
        """

        self.name: str = name
        self.chips: int = chips
        self.bet: int = 0
        self.hand: Hand = Hand()

    def __str__(self):
        return self.name

    def take_bet(self) -> None:
        """Takes a value of the bet from the player."""

        input_validated = False

        while not input_validated:
            user_input = input("Enter your bet: ")
            if user_input.isnumeric():
                bet = int(user_input)
                if bet > self.chips:
                    print("You don't have enough chips!")
                else:
                    input_validated = True
                    self.chips -= bet
                    self.bet = bet
            else:
                print("Please enter a number.")

    def hit_or_stand(self) -> bool:
        """Asks the player if they want to hit or stand."""

        input_validated = False

        while not input_validated:
            user_input = input("Hit or stand? ")
            if user_input == "h":
                input_validated = True
                return True
            elif user_input == "s":
                input_validated = True
                return False
            else:
                print("Please enter 'h' for hit or 's' for stand.")

    def replay(self) -> bool:
        """Asks the player if they want to play the game again."""

        input_validated = False

        while not input_validated:
            user_input = input("Do you want to play another round? ")
            if user_input == "y":
                input_validated = True
                return True
            elif user_input == "n":
                input_validated = True
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
