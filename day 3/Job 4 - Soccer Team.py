class Player():
    def __init__(self, firstname, number, position, goal=0, assist=0, yellow_card=0, red_card=0):
        self.firstname = firstname
        self.number = number
        self.position = position
        self.goal = goal
        self.assist = assist
        self.yellow_card = yellow_card
        self.red_card = red_card

    def score_a_goal(self):
        self.goal += 1

    def make_an_assist(self):
        self.assist += 1

    def set_yellow_card(self):
        self.yellow_card += 1

    def set_red_card(self):
        self.red_card += 1
    
    def display_statistics(self):
        return f"Le joueur {self.firstname} n°{self.number}:\
            \nBut(s) : {self.goal}\
            \nPasse(s) décisive(s) : {self.assist}\
            \nCarton(s) jaune : {self.yellow_card}\
            \nCarton(s) rouge : {self.red_card}"

class SoccerTeam():
    def __init__(self, name):
        self.name = name
        self.player_list = []

    def add_player(self, player):
        if player not in self.player_list:
            self.player_list.append(player)
        else:
            print("vous ne pouvez pas ajouter un joueur qui est déjà dans l'équipe")

    def get_players_statistics(self):
        for player in self.player_list:
            print(f"{player.display_statistics()}\n")

    def update_player_statistics(self):
        pass

a_player = Player("John", 9, "avant-centre", 0, 0, 0, 0)

# print(a_player.display_statistics())
a_player.score_a_goal()
a_player.score_a_goal()
a_player.score_a_goal()
a_player.score_a_goal()
a_player.score_a_goal()
a_player.make_an_assist()
a_player.make_an_assist()
a_player.make_an_assist()
a_player.set_yellow_card()
a_player.set_red_card()
a_player.set_yellow_card()
# print(a_player.display_statistics())

player_2 = Player("Bill", 11, "2ème attaquant", 0, 0, 0, 0)
player_3 = Player("Dean", 8, "millieu offensif", 0, 0, 0, 0)
player_4 = Player("Sam", 10, "millieu offensif", 0, 0, 0, 0)

team = SoccerTeam("Florence")
team.add_player(a_player)
team.add_player(player_2)
team.add_player(player_2)
team.add_player(player_3)
team.add_player(player_4)


player_2.score_a_goal()
player_2.score_a_goal()
player_2.make_an_assist()
player_2.score_a_goal()
player_2.make_an_assist()
player_2.make_an_assist()
player_2.make_an_assist()
player_2.make_an_assist()
player_2.set_yellow_card()
player_2.set_red_card()


player_3.score_a_goal()
player_3.score_a_goal()
player_3.score_a_goal()
player_3.make_an_assist()
player_3.make_an_assist()
player_3.make_an_assist()
player_3.set_red_card()
player_3.set_yellow_card()

player_4.set_red_card()
player_4.set_red_card()
player_4.set_red_card()
team.get_players_statistics()


