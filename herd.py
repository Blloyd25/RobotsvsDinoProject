
from dinosaur import Dinosaur

class Herd:
    
        
        
    def create_herd(self):  
        self.dino=[]
        dino_one = Dinosaur("T-Rex", 30)
        dino_two  = Dinosaur("Barney", 30)
        dino_three = Dinosaur("George", 30)


        self.dino.append(dino_one)
        self.dino.append(dino_two)
        self.dino.append(dino_three)
        return(self.dino)

    def find_good_dino(herd):
        for d in herd:
            if d.dino_health >= 1:
               
                return d
                break
        print('No More Dinos Alive')
        print('Congrats for Octane he is the Ultimate Fighting Champion') 
        return False
    