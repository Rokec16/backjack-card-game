from cards import Deck
from players import Player


def hit(player: Player, deck: Deck):
    """Add a card to players hand and adjust for aces."""

    player.hand.add_card(deck.deal_one_card())
    player.hand.adjust_for_ace()


def show_players_cards(player: Player, dealer: Player):

    print('Players cards are: ', *player.hand.cards, sep='\n')

    print('--------------------')

    print('Dealers cards are:')
    print('Hidden card.')
    for card in dealer.hand.cards[1:]:
        print(card)

    print()


def show_all_cards(player: Player, dealer: Player):
    print('Players cards are:')
    for card in player.hand.cards:
        print(card)

    print('--------------------')

    print('Dealers cards are:')
    for card in dealer.hand.cards:
        print(card)

    print(f'Value of players cards is: {player.hand.value}')
    print(f'Value of dealers cards is: {dealer.hand.value}')

    print()


def main():

    print('Welcome to the game of Console Blackjack. Good luck!')

    while True:

        deck_of_cards = Deck()
        deck_of_cards.shuffle_cards()

        player = Player('Player1', 100)
        dealer = Player('Dealer')

        player.hand.add_card(deck_of_cards.deal_one_card())
        dealer.hand.add_card(deck_of_cards.deal_one_card())

        player.hand.add_card(deck_of_cards.deal_one_card())
        dealer.hand.add_card(deck_of_cards.deal_one_card())

        player_bet = player.take_bet()
        print(f'Players bets {player_bet} chips.')
        print()

        show_players_cards(player, dealer)

        while True:

            if player.hit_or_stand():
                hit(player, deck_of_cards)
            else:
                print(f'Player {player} decided to stand.')

            if player.hand.value > 21:
                break

            if dealer.hand.value < 17:
                hit(dealer, deck_of_cards)
            else:
                break

            show_players_cards(player, dealer)

        show_all_cards(player, dealer)

        if dealer.hand.value > 21:
            print('Dealer busts!')
            player.chips += player_bet
        elif player.hand.value > 21:
            print('Player busts!')
        elif player.hand.value > dealer.hand.value:
            print('Player wins!')
            player.chips += player_bet
        else:
            print('Dealer wins!')

        if player.replay():
            print('Good luck!')
        else:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
