from utils import Player,Deck,Card


player = Player()
dealer = Player()
deck = Deck()

def get_card_value(card:Card,p:Player):
    if isinstance(card.value,int):
        return card.value
    elif isinstance(card.value,str) and card.value != "A":
        return 10
    else:
        if p.sum + 11 <= 21:
            return 11
        elif p.sum + 1 <= 21:
            return 1
        else:
            return 1

    


def update_hand(p:Player,card:Card):
    p.sum += get_card_value(p,card)
    p.hand.append(card)


def start_game():
    print("Welcome to the Casino! Today we are playing Blackjack!")
    player_card_one,player_card_two = deck.cards.pop(),deck.cards.pop()
    dealer_card_one,dealer_card_two = deck.cards.pop(),deck.cards.pop()

    update_hand(player,player_card_one)
    update_hand(player,player_card_two)
    update_hand(dealer,dealer_card_one)
    update_hand(dealer,dealer_card_two)


    print("Dealer has:" + str(dealer_card_one.value) + " ? = ?" )
    print("You have:" + str(player_card_one.value) + " " + str(player_card_two.value) + " = " + str(player.sum))

def play_game():
    start_game()
    # while player.sum <= 21 and dealer.sum <= 21:

play_game()
        


        

        



