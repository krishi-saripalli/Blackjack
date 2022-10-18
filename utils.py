import random


class Card:
    def __init__(self,value) -> None:
        self.value = value

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.add_cards()
        self.shuffle_deck()
        
    def add_cards(self):
        #add cards numbered 2-10
        number_cards = [Card(str(i)) for i in range(2,11)]
        all_cards = number_cards + [Card("A"),Card("K"),Card("Q"),Card("J")]
        all_cards = 4*all_cards
        self.cards += all_cards
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

d = Deck()
print([card.value for card in d.cards])


