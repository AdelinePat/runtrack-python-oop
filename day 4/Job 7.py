import random
class Card():
    def __init__(self, color, value, figure=""):
        self.color = color
        self.value = value
        self.figure = figure
    
    def __str__(self):
        return f"{self.value} {self.figure} - {self.color}"

class Game():
    def __init__(self):
        self.deck = self.create_deck()

    def create_color(self, color):
        cards = []
        for index in range(2,15):
            if index >= 11:
                match index:
                    case 11:
                        card = Card(color, 11, "ACE")
                    case 12:
                        card = Card(color, 10, "JACK")
                    case 13:
                        card = Card(color, 10, "QUEEN")
                    case 14:
                        card = Card(color, 10, "KING")                   
            else:
                card = Card(color, index)
            cards.append(card)
        return cards

    def create_deck(self):
        self.deck = []
        for color in ["♠ Spades", "♥ Heart", "♣ Club", "♦ Diamond"]:
            self.deck += self.create_color(color)
        
        random.shuffle(self.deck)
        return self.deck

a_game = Game()

for each_card in a_game.deck:
    print(each_card)

# print(a_game.deck)

        