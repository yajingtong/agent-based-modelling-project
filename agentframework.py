import random

#define Agent class
class Agent():# use the __init__ function  to initialise the parameters
   
    #self is the initial parameter label in object
    def __init__ (self, x, y, environment, agents, neighbourhood):
        
        self.x = x#x,y are the parameter of coordinates
        self.y = y
        self.environment = environment #environment parameter is the 
        self.store = 0
        self.neighbourhood = neighbourhood
        self.agents = agents #agents are list
        
        if x == None:
            self.x = random.randint(0,300) #use the function randint from random to create a set of random int from 0 to 300
        else:
            self.x = x   
        if y == None:
            self.y = random.randint(0,300)
        else:
            self.y = y
            
    def move(self):#move agents based on a random number
         if random.random() < 0.5:# half the posibility <0.5
            self.x = (self.x + 1) % 300
         else:
            self.x = (self.x - 1) % 300

         if random.random() < 0.5:
            self.y = (self.y + 1) % 300
         else:
            self.y = (self.y - 1) % 300
            
    def eat(self): 
         if self.environment[self.y][self.x] > 10:#two dimension agents and coordinates
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    #find the nerest agent and share with it
    def share_with_neighbours(self):
        
        for agent in self.agents:
            dist = self.distance_between(agent) # calls the function of distance_between
            if dist <= self.neighbourhood: #If distance is less than or equal to the neighbourhood
               sum = self.store + agent.store
               ave = sum /2
               self.store = ave #store the value in self.store
               agent.store = ave
               
               print("sharing " + str(dist) + " " + str(ave))
               
     #calculate distance between self and agent
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5           
               