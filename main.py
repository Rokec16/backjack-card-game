from cards import Deck
from players import Player


def hit(player: Player, deck: Deck) -> None:
    """Add a card to the selected players hand and adjust for aces."""

    player.hand.add_card(deck.deal_one_card())
    player.hand.adjust_for_ace()


def show_players_cards(player: Player, hide_one: bool = False) -> None:
    """Displays playing cards currently held in the selected players hand.

    Parameters:
    -----------
        player : Player
            Instance of the Player which cards to display.
        hide_one : bool, optional
            Determines if first card of the hand is hidden. Defaults to False.
    """

    if hide_one:
        print(f'{player.name}s cards are: ')
        print('Hidden card.')
        for card in player.hand.cards[1:]:
            print(card)
    else:
        print(f'{player.name}s cards are: ', *player.hand.cards, sep='\n')

    print('--------------------')


def setup_the_game(player_name: str,
                   player_chips: int) -> (Deck, Player, Player):
    """Creates a shuffled deck of cards, setups two players holding two cards.

    Parameters:
    ----------
    player_name : str
        Name of the player.
    player_chips: int
        Amount of chips that the players holds at the start of the game.

    Returns:
    --------
        tuple: Holding objects of deck, player, dealer.
    """

    deck = Deck()
    deck.shuffle_cards()

    player = Player(player_name, player_chips)
    dealer = Player('Dealer')

    player.hand.add_card(deck.deal_one_card())
    dealer.hand.add_card(deck.deal_one_card())

    player.hand.add_card(deck.deal_one_card())
    dealer.hand.add_card(deck.deal_one_card())

    return deck, player, dealer


def play_the_game(deck: Deck, player: Player, dealer: Player) -> None:
    """Adds cards to players and dealers hands according to rules of Blackjack.

    First comes the players turn. Player decides to hit or stand and receives
    a new card if he chooses hit. Players turn ends if he decides to stand
    or value of his cards surpasses 21.
    Dealer hits until his score surpasses 17.

    Parameters:
    -----------
        deck : Deck
            Instance of the deck of cards.
        player : Player
            Instance of the Player class representing the player.
        dealer : Player
            Instance of the Player class representing the dealer.
    """

    # Players turn.
    while True:

        if player.hit_or_stand():
            hit(player, deck)
            show_players_cards(player)
        else:
            print(f'Player {player.name} decided to stand.')
            break

        # If players hand value reaches 21, he has lost.
        if player.hand.value > 21:
            break

    # Dealers turn
    if player.hand.value > 21:
        # There is no need to play dealers part if player has already lost.
        pass
    else:
        while dealer.hand.value < 17:
            hit(dealer, deck)


def check_results(player: Player, dealer: Player):
    """Checks the victory conditions and distributes the chips accordingly.

    Parameters:
    -----------
        player : Player
            Instance of the Player class representing the player.
        dealer : Player
            Instance of the Player class representing the dealer.
    """

    if dealer.hand.value > 21:
        print(f'Dealer busts. {player.name} wins!')
        player.chips += player.bet * 2
    elif player.hand.value > 21:
        print('Player busts!')
    elif player.hand.value == dealer.hand.value:
        print('Tie!')
    elif player.hand.value > dealer.hand.value:
        print(f'{player.name} wins!')
        player.chips += player.bet * 2
    else:
        print('Dealer wins!')


def game():

    print('Welcome to the game of Console Blackjack. Good luck!')

    while True:

        deck_of_cards, player, dealer = setup_the_game('Player 1', 100)

        player.take_bet()
        print(f'Players bets {player.bet} chips.')

        show_players_cards(player)
        show_players_cards(dealer, hide_one=True)

        play_the_game(deck_of_cards, player, dealer)

        show_players_cards(player)
        show_players_cards(dealer)

        print(f'Value of players cards is: {player.hand.value}')
        print(f'Value of dealers cards is: {dealer.hand.value}')

        check_results(player, dealer)

        print(f'\nPlayer holds {player.chips} chips.')

        if player.replay():
            print('Good luck!')
        else:
            print('Goodbye!')
            break


if __name__ == "__main__":
    game()
