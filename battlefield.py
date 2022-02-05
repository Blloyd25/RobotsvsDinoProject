
from hashlib import new
from multiprocessing import Condition
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robots import Robots



class Battlefield:
    fleet = Fleet()
    herd = Herd()
    fleet = fleet.create_fleet()
    herd = herd.create_herd()
    good_robot = Fleet.find_good_robot(fleet)
    good_dino = Herd.find_good_dino(herd)





    def __init__ ():
        fleet = Fleet()
        herd = Herd()
        print(herd)
        fleet = fleet.create_fleet()
        herd = herd.create_herd()
        # print(herd[0].name)
        # [print(x.weapon.name)for x in fleet]



    def welcome_greeting ():
        print(f'welcome to the fighting field!')
        pass
    
    
    

  

    def start_of_battle(good_robot, good_dino,herd,fleet):
        print(good_robot.name + " is your robot contender")
        print(good_dino.name + " is your dino contender with " + str(good_dino.dino_health) + " Health points")
        # for good_dino, good_robot in        
        while True:
            if good_dino.dino_health < 1:
                print("your dino died")
                good_dino = Herd.find_good_dino(herd)
            elif good_dino.dino_health >= 1:
                Robots.robot_attack_move(good_robot,good_dino)
                if good_dino.dino_health < 1:
                    print("your dino died")
                    good_dino = Herd.find_good_dino(herd)



            if good_robot.robot_health < 1:
                print("your robot died ")
                good_robot = Fleet.find_good_robot(fleet)
            elif good_robot.robot_health >= 1:
                Dinosaur.attack(good_dino,good_robot)
            if good_robot.robot_health < 1:
                print("your robot died ")
                good_robot = Fleet.find_good_robot(fleet)
            
            
            if not Condition:
                break

                   



    # def robot_attack(good_dino, good_robot, herd):

    # def dino_attack(good_robot, good_dino, fleet):
        







 
    welcome_greeting()
    start_of_battle(good_robot, good_dino,herd, fleet)
    # def dino_turn(herd):
    #     for dino in herd:
    #         print(dino)
    def dino_turn ():

    # call attack
    
    # def robots_turn():
    
        pass
 
    #call attack
    
    def start_match(self): # this will be the first funciton to run, its getting called on main.py
    
        pass
  
    
       
        


    def start_of_battle(self): # while herd list and fleet list lenght is greater than 0 
        pass
   


    def show_dino_options(self): # use to show user attack options, may only get used in dino turn()
       
        pass
                                                                                          
    def show_robots_options(self):
       
        pass

    def champion(self):

        if Dinosaur.dino_health <= 0:
            print('the dinosaurs lose')
        elif Robots.robo_health <=0:
            print('the robots lose by a landslide')
        elif Robots.robo_health >= 1:
            print('robots win')
        elif Dinosaur.dino_Health >= 1:
            print('dinos win')
       
       
       
       
       
        pass

        