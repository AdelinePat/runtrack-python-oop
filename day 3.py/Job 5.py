class Character():
    def __init__(self, name, life_count):
        self.name = name
        self.life_count = life_count
    
    def attack(self, ennemy, game):
        if not game.is_game_over() and ennemy.life_count > 0:
            ennemy.life_count -= 1
            print(self)
        if game.is_game_over():
            game.game_over_message()
    
    def get_health(self):
        return self.life_count
    
    def __str__(self):
        return f"Nom : {self.name}\
            \nVie : {self.get_health()}\n"

class Game():
    def __init__(self):
        self.difficulty = self.set_difficulty()
        self.player, self.ennemy = self.start_game()
        self.game_status = self.is_game_over()

    def set_difficulty(self):
        difficulty = input("Entrez votre niveu de difficulté : Facile, Normal, Difficile").lower()
        if difficulty in ["facile", "normal", "difficile"]:
            self.difficulty = difficulty
        else:
            print("Vous devez choisir la difficulté entre FACILE - NORMAL - DIFFICILE")
            return self.set_difficulty()
        
    def set_life_count(self):
        if self.difficulty == "facile":
            life_count = 10
        elif self.difficulty == "normal":
            life_count = 5
        else:
            life_count = 3
        return life_count
    
    def start_game(self):
        player_name = input("Votre nom de joueur : ").capitalize()
        player = Character(player_name, self.set_life_count())
        ennemy = Character("Le méchant, très méchant", self.set_life_count())
        return player, ennemy
    
    # def in_game(self):
    #     if not self.is_game_over():
    #         self.player.attack(self.ennemy)

    def is_game_over(self):
        if self.player.life_count == 0 or self.ennemy.life_count == 0:
            return True
        else:
            return False
        
    def game_over_message(self):
        print("Le jeu est terminé")
        if self.player.life_count > self.ennemy.life_count:
            print(f"{self.player.name} a gagné !")
        else:
            print(f"{self.ennemy.name} a gagné !")

new_game = Game()
print(new_game.ennemy)
new_game.player.attack(new_game.ennemy, new_game)
new_game.player.attack(new_game.ennemy, new_game)
new_game.ennemy.attack(new_game.player, new_game)

# print(new_game.ennemy)
# print(new_game.player)
new_game.player.attack(new_game.ennemy, new_game)
# print(new_game.ennemy)
# print(new_game.player)
# new_game.player.attack(new_game.ennemy, new_game)
# new_game.ennemy.attack(new_game.player, new_game)
# print(new_game.ennemy)
# print(new_game.player)