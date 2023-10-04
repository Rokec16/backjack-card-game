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

    def add_card(self, card: Card):
        """Adds a card to the hand and adjusts hands value."""

        self.cards.append(card)
        self.value += card.value


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
        hand : Hand
            Cards the player holds.
        """

        self.name: str = name
        self.chips: int = chips
        self.hand: Hand = Hand()

    def take_bet(self):
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
                    return bet
            else:
                print("Please enter a number.")

    def hit_or_stand(self) -> bool:
        """Asks the player if they want to hit or stand."""

        input_validated = False

        while not input_validated:
            user_input = input("Hit or stand? ")
            if user_input == "hit":
                input_validated = True
                return True
            elif user_input == "stand":
                input_validated = True
                return False
            else:
                print("Please enter 'hit' or 'stand'.")

    def replay(self) -> bool:
        """Asks the player if they want to play the game again."""

        input_validated = False

        while not input_validated:
            user_input = input("Do you want to play another round? ")
            if user_input == "yes":
                input_validated = True
                return True
            elif user_input == "no":
                input_validated = True
                return False
            else:
                print("Please enter 'yes' or 'no'.")