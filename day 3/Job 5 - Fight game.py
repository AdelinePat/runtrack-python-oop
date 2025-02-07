import random
class Character():
    def __init__(self, name, life_count):
        self.name = name
        self.life_count = life_count
    
    def attack(self, ennemy, is_game_over):
        if not is_game_over and ennemy.life_count > 0:
            luck = random.randrange(0, 100)
            if luck > 60:
                ennemy.life_count -= 1
                print(f"L'attaque de {self.name.upper()} sur {ennemy.name.upper()} a réussi !")
            elif luck > 95:
                ennemy.life_count -= 2
                print(f"L'attaque de {self.name.upper()} sur {ennemy.name.upper()} a réussi !")
            else:
                print(f"L'attaque de {self.name.upper()} sur {ennemy.name.upper()} a échoué")
            print(self)

    def heal(self):
        if self.life_count <= 1:
            if random.randrange(0,100) > 50:
                self.life_count += 1
                print(f"{self.name} a pris une potion de soin et récupère 1PV")

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
            return difficulty

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
        ennemy = Character("♫♪ Le méchant, très méchant ♪♫", self.set_life_count())
        return player, ennemy

    def is_game_over(self):
        if self.player.life_count == 0 or self.ennemy.life_count == 0:
            return True
        else:
            return False
        
    def game_over_message(self):
        print("Le jeu est terminé")
        if self.ennemy.life_count == 0:
            print(f"{self.player.name} a gagné !")
        else:
            print(f"{self.ennemy.name} a gagné !")

    def player_turn(self):
        player_choice = input("1. Attaquer\n2. Se soigner")
        if player_choice not in ["1","2"]:
            return self.player_turn()
        else:
            return player_choice
        
    def game_loop(self):
        is_game_over  = self.is_game_over()
        round = 1
        while is_game_over == False:
            print(f"TOUR N°{round}")
            round += 1
            choice = self.player_turn()
            if choice == "1":
                self.player.attack(self.ennemy, is_game_over)
                is_game_over  = self.is_game_over()
            else:
                self.player.heal()
            self.ennemy.attack(self.player, is_game_over)
            self.ennemy.heal()
            is_game_over  = self.is_game_over()

            if is_game_over:
                self.game_over_message()


new_game = Game()
# print(new_game.ennemy)
# new_game.player.attack(new_game.ennemy, new_game)
# new_game.player.attack(new_game.ennemy, new_game)
# new_game.ennemy.attack(new_game.player, new_game)
# new_game.player.attack(new_game.ennemy, new_game)

new_game.game_loop()