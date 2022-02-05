
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
   

    def welcome_greeting ():
        print(f'welcome to the fighting field!')
        pass
      

    def start_of_battle(good_robot, good_dino,herd,fleet):
        print(good_robot.name + " is your robot contender")
        print(good_dino.name + " is your dino contender with " + str(good_dino.dino_health) + " Health points")
               
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
           

    welcome_greeting()
    pass
    start_of_battle(good_robot, good_dino,herd, fleet)

    pass

    print('congradulations for ocatne he is the ultimate fighting champion')   


      
       
       
       
       
       
      

        