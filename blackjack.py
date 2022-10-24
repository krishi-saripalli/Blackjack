
from utils import Player,Deck,Card



player = Player("Player")
dealer = Player("Dealer")
deck = Deck()

def get_card_value(card:Card,p:Player):
    if isinstance(card.value,int):
        return card.value
    elif isinstance(card.value,str) and card.value != "A":
        return 10
    else:
        p.aces += 1
        return 11

    


def update_hand(p:Player,card:Card):
    p.sum += get_card_value(card,p)
    p.hand.append(card.value)
    ace_count = 0
    while p.sum > 21 and ace_count < p.aces:
        p.sum -= 10
        ace_count += 1
    if p.sum > 21:
        print(p.name + " busts with " + str(p.sum))
        exit()
        os.execv(sys.argv[0], sys.argv)
    elif p.sum == 21:
        print(p.name + " wins! Blackjack!")
        exit()
        os.execv(sys.argv[0], sys.argv)


def get_player_hand(p:Player):
    player_hand = ""
    for card_value in p.hand:
                player_hand += str(card_value) + " "
    return player_hand


def hit(d:Deck):
    return d.cards.pop()
def start_game():
    print("Welcome to the Casino! Today we are playing Blackjack!")
    player_card_one,player_card_two = hit(deck),hit(deck)
    dealer_card_one,dealer_card_two = hit(deck),hit(deck)

    update_hand(player,player_card_one)
    update_hand(player,player_card_two)
    update_hand(dealer,dealer_card_one)
    update_hand(dealer,dealer_card_two)

    player_hand = get_player_hand(player)

    print("Dealer has: " + str(dealer_card_one.value) + " ? = ?" )
    print("Player has: " + player_hand + " = " + str(player.sum))

def player_turn():
    start_game()
    turn = ""
    while turn != "S":
        print("Would you like to (H)it or (S)tand?")
        turn = input()
        if turn == "H":
            update_hand(player,hit(deck))
            print("Player Hits")
            player_hand = get_player_hand(player)
            print("Player has: " + player_hand + " = " + str(player.sum))
        elif turn != "S":
            print("Please enter a valid command")
    
def dealer_turn():
    print("Player Stands")
    print("")
    while dealer.sum < 17:
        update_hand(dealer,hit(deck))
        print("Dealer Hits")
        dealer_hand = get_player_hand(dealer)
        print("Dealer has: " + dealer_hand + " = " + str(dealer.sum))
    print("Dealer Stands")

    player_hand = get_player_hand(player)
    print("Player has: " + player_hand + " = " + str(player.sum))
    dealer_hand = get_player_hand(dealer)
    print("Dealer has: " + dealer_hand + " = " + str(dealer.sum))

    if dealer.sum > player.sum:
        print("Dealer Wins!")
    elif player.sum > dealer.sum:
        print("Player Wins!")
    else:
        print("Tie Game!")
        


player_turn()
dealer_turn()
        


        

        



