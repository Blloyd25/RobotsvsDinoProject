from dinosaur import Dinosaur
from weapon import Weapon





class Robots:
    def __init__ (self,robo_name):
        self.name = robo_name
        self.robot_health = 100
        self.weapon = Weapon("knife")
       


    def robot_attack_move (self, dinosaur):
        dinosaur.dino_health -= self.weapon.attack_power  
        print(f'{dinosaur.name} was hit for {self.weapon.attack_power} damage!   {dinosaur.dino_health} health remaining')


# test_robot= Robots('bob')
# test_dino = Dinosaur('chappie', 30)
# test_robot.robot_attack_move(test_dino)  

    


       




