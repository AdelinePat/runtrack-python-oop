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
    pass


a_player = Player("John", 9, "avant-centre", 0, 0, 0, 0)

print(a_player.display_statistics())
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
print(a_player.display_statistics())