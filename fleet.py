from robots import Robots




class Fleet:
    
        

    def create_fleet(self):
        self.fleet_list= []
        robot_one = Robots('R2-D2') 
        robot_two = Robots('chappie' )
        robot_three = Robots('octane')
        
        self.fleet_list.append(robot_one) 
        self.fleet_list.append(robot_two)
        self.fleet_list.append(robot_three)
        return(self.fleet_list)


    def find_good_robot (fleet):
        for f in fleet:
            if f.robot_health >= 1:
                print(f.name + " is your next fighter" )
                return f
                break
        print('no more robots alive')
        return False
