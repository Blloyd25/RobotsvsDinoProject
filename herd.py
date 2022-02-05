
from dinosaur import Dinosaur

class Herd:
    
        
        
    def create_herd(self):  
        self.dino=[]
        dino_one = Dinosaur("T-Rex", 30)
        dino_two  = Dinosaur("barney", 30)
        dino_three = Dinosaur("george", 30)


        self.dino.append(dino_one)
        self.dino.append(dino_two)
        self.dino.append(dino_three)
        return(self.dino)

    def find_good_dino(herd):
        for d in herd:
            if d.dino_health >= 1:
               
                return d
                break
        print('no more dinos alive')
        print('congrats for ocatane he is the ultimate fighting champion') 
        return False
    