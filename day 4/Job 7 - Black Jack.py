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
        self.players = self.create_player_list()
        self.croupier = Croupier()
    
    def create_player_list(self):
        player_list = []
        for index in range(4):
            player = Player(f"joueur n°{index+1}")
            player_list.append(player)
        return player_list

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
    
    def game_loop(self):
        for player in self.players:
            player.draw_card(self.deck)
            player.draw_card(self.deck)
            print(f"Valeur de la main : {player._calculate_hand_value()}\n")
        
        is_game_over = self.croupier.create_hand(self.deck)
        
        if not is_game_over:
            for player in self.players:
                player.create_hand(self.deck, self.croupier._calculate_hand_value())

    def create_deck(self):
        self.deck = []
        for color in ["♠ Spades", "♥ Heart", "♣ Club", "♦ Diamond"]:
            self.deck += self.create_color(color)
        
        random.shuffle(self.deck)
        return self.deck

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = self._calculate_hand_value()

    def draw_card(self, deck):
        print(f"{self.name} a tiré {deck[-1]}")
        self.hand.append(deck[-1])
        deck.pop(-1)
    
    def create_hand(self, deck, croupier_hand_value):
        if len(self.hand) == 0:
            self.draw_card()

        total_value = self._calculate_hand_value()
        while total_value < croupier_hand_value:
            self.draw_card(deck)
            total_value = self._calculate_hand_value()

        if total_value > croupier_hand_value and total_value <= 21:
            print(f"Le joueur {self.name} a gagné")
        elif total_value > 21:
            print(f"Le joueur {self.name} a perdu")
        
        print(f"Valeur de la main : {self._calculate_hand_value()}\n")
    
    def _calculate_hand_value(self):
        total_value = 0
        for card in self.hand:
            total_value += card.value

        return total_value

class Croupier(Player):
    def __init__(self, name="Croupier"):
        super().__init__(name)

    def create_hand(self, deck):
        is_game_over = False
        if len(self.hand) == 0:
            self.draw_card(deck)

        total_value = self._calculate_hand_value()
        while total_value < 17:
            self.draw_card(deck)
            total_value = self._calculate_hand_value()

        # self.display_hand()
        if total_value > 21:
            print(f"Le {self.name} a perdu")
            is_game_over = True
        
        print(f"Valeur de la main : {self._calculate_hand_value()}\n")

        return is_game_over

a_game = Game()

a_game.game_loop()
