import random



class wolf(object):# create a class of wolf
    '''
    A wolf that walks around, and eats sheep. 
   
    '''
    grid = None


    def __init__(self, x,y, wolves):
        
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.wolves =wolves
    
    
        
    def random_move(self):#move agents based on a random number
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300   

'''    
    def random_kill(self,Agent):
         for agent in s.Agent.agents:
            dist = self.distance_between(agent) # calls the function of distance_between
            if dist <= 0:
                s.Agent.energy -= 1
                return('killed')
'''
    




































       
               