def blackjack():

    import random
    import IPython

    suits = ('Hearts','Diamonds','Spades','Clubs')
    ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
    values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

    class Card:
        def __init__(self,suit,rank):
            self.suit = suit
            self.rank = rank
        def __str__(self):
            return f'{self.rank} of {self.suit}'

    class Deck(Card):
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit,rank))
        def __str__(self):
            return f'{self.deck}'
        def shuffle(self):
            random.shuffle(self.deck)

    class Hand(Deck):
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0
        def __str__(self):
            return f'{self.cards}'
        def add_card(self,deck):
            card = deck.deck.pop()
            self.cards.append(card)
            if card.rank == 'Ace':
                self.aces += 1
            self.value += values[card.rank]
            if self.value > 21:
                self.value = self.value - (self.aces*10)

    class Chips:
        def __init__(self, total):
            self.total = total
            self.bet = 0
        def win_bet(self):
            self.total += self.bet
            print(f"You won {self.bet} chips.")
        def lose_bet(self):
            self.total -= self.bet
            print(f"You lost {self.bet} chips.")

    def take_bet(chips):
        while True:
            try:
                bet = -1
                while bet < 0 or bet > chips.total:
                    bet = int(input('Place a bet from your total.'))
                return bet
            except:
                print('Enter chips as an integer.')
            else:
                break

    def hit_or_stand(deck,hand):
        nonlocal playing
        move = input('Hit or Stand?')
        while move.lower() != 'hit' and move.lower() != 'stand':
            move = input('Please enter Hit or Stand.')
        if move.lower() == 'hit':
            hand.add_card(deck)
            if hand.value >= 21:
                playing = False
        elif move.lower() == 'stand':
            playing = False

    def show_some(player,dealer):
        IPython.display.clear_output()
        print('The table looks like this:')
        print("    Player's hand:")
        for card in player.cards:
            print(f"        {card}")
        print(f"    Value of player's hand: {player.value}")
        print("    Dealer's hand:")
        for card in dealer.cards[1:]:
            print(f"        {card}")

    def show_all(player, dealer):
        IPython.display.clear_output()
        print('The final hands are:')
        print("    Player's hand:")
        for card in player.cards:
            print(f"        {card}")
        print(f"    Value of player's hand: {player.value}")
        print("    Dealer's hand:")
        for card in dealer.cards:
            print(f"    {card}")
        print(f"    Value of dealer's hand: {dealer.value}")

    def player_blackjack(player,chips):
        if player.value == 21:
            print('BLACKJACK! Player has won.')
            chips.win_bet()

    def player_busts(player,chips):
        if player.value > 21:
            print('Player bust! Dealer has won.')
            chips.lose_bet()

    def dealer_busts(dealer,chips):
        if dealer.value > 21:
            print('Dealer bust! Player has won.')
            chips.win_bet()

    def player_wins(player,dealer,chips):
        if player.value > dealer.value:
            print('Congratulations! Player has won!')
            chips.win_bet()

    def dealer_wins(player,dealer):
        if dealer.value < 21 and player.value < dealer.value:
            print('Dealer wins. Too bad, player. Better luck next time.')
            chips.lose_bet()

    def draw(player,dealer):
        if player.value == dealer.value:
            print("It's a draw! try your luck next time.")

    def replay():
        replay = input('Would you like to play again? (Yes/No)')
        while replay.lower() != 'yes' and replay.lower() != 'no':
            replay = input('Please enter Yes or No.')
        return replay.lower() == 'no'

    print("Welcome to the Dark Jack Casino!\nLet's play Blackjack.")

    while True:
        try:
            total = int(input('How many chips do you have?'))
        except:
            print('Enter chips as an integer.')
        else:
            break

    chips = Chips(total)

    while True:

        IPython.display.clear_output()

        playing = True

        deck = Deck()
        deck.shuffle()

        player = Hand()
        dealer = Hand()

        player.add_card(deck)
        dealer.add_card(deck)
        player.add_card(deck)
        dealer.add_card(deck)

        print(f"You currently have {chips.total} chips with you.")

        chips.bet = take_bet(chips)
        print(f"You have bet {chips.bet} chips.")

        while playing:
            show_some(player,dealer)
            hit_or_stand(deck,player)

        if player.value > 21:
            show_all(player,dealer)
            player_busts(player,chips)
        elif player.value == 21:
            show_all(player,dealer)
            player_blackjack(player,chips)
        else:
            while dealer.value < 17:
                dealer.add_card(deck)
            show_all(player,dealer)
            dealer_busts(dealer,chips)
            player_wins(player,dealer,chips)
            dealer_wins(player,dealer)
            draw(player,dealer)

        print(f"You currently have {chips.total} chips with you.")

        if replay():
            break

    IPython.display.clear_output()
    print('Thank you for visiting the Dark Jack Casino.\nHope to see you here again soon.')
