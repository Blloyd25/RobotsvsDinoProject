


class Dinosaur:
    def __init__ (self,dino_name, attack_power):
        self.name = dino_name
        self.attack_power = attack_power
        self.dino_health= 100

    

    def attack(self, robots): 
        robots.robot_health -= self.attack_power 
        print(f'{self.name} smashes {robots.name} for {self.attack_power} damage! {robots.name} has {robots.robot_health}  health remaining')








# test_robot= Robots('bob')
# test_dino = Dinosaur('george', 20)
# test_dino.attack(test_robot)       
       
       
       
        