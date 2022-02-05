from robots import Robots




class Fleet:
    
        

    def create_fleet(self):
        self.fleet_list= []
        robot_one = Robots('R2-D2') 
        robot_two = Robots('Chappie' )
        robot_three = Robots('Octane')
        
        self.fleet_list.append(robot_one) 
        self.fleet_list.append(robot_two)
        self.fleet_list.append(robot_three)
        return(self.fleet_list)


    def find_good_robot (fleet):
        for f in fleet:
            if f.robot_health >= 1:
                
                return f
                break
        print('No More Robots Alive')
        return False
