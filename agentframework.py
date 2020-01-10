import random


#define Agent class
class Sheep():# use the __init__ function  to initialise the object parameters

    '''
    A sheep that walks around randomly,eat grass, interact with neighbors 
 
    '''  
    #self is the initial parameter label in object
    def __init__ (self, x, y, environment,agents, neighbourhood):
        
        self.x = x #x,y are the parameter of coordinates
        self.y = y
        self.environment = environment #environment parameter is the 
        self.store = 0
        self.agents = agents #agents are list
        self.neighbourhood = neighbourhood
        self.energy= 5
        
        
        if x == None:
            self.x = random.randint(0,300) #use the function randint from random to create a set of random int from 0 to 300
        else:
            self.x = x   
        if y == None:
            self.y = random.randint(0,300)
        else:
            self.y = y
            
    def move(self):#move agents based on a random number
         if random.random() < 0.5:
            self.x = (self.x + 1) % 300
         else:
            self.x = (self.x - 1) % 300

         if random.random() < 0.5:
            self.y = (self.y + 1) % 300
         else:
            self.y = (self.y - 1) % 300
            
    def eat(self): #make the sheep eat "grass"
         if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    def hungry(self):
        if self.store < 50:
            self.energy -= 1
            print("h")#(print to test)
        if self.store > 50:
            self.energy += 1
            print("f")
    
    def eaten(self):
        if self.energy <= 0:
            self.remove
            #print("d")
            
    def remove(self, agent):
        
        #Remove all instances of a given agent 
    
        while agent in self.agents:
            self.agents.remove(agent)

        agent_class = type(agent)
        while agent in self.agents[agent_class]:
            self.agents[agent_class].remove(agent)
            #print("r")
 
       
    #find the nerest agent and share with it
    def share_with_neighbours(self,neighbourhood):
        
        for agent in self.agents:
            dist = self.distance_between(agent) # calls the function of distance_between
            if dist <= self.neighbourhood: #If distance is less than or equal to the neighbourhood
               sum = self.store + agent.store
               ave = sum /2
               self.store = ave #store the value in self.store
               agent.store = ave
               
               print("sharing " + str(dist) + " " + str(ave))#to test sharing 
              
     #calculate distance between self and agent
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

   













       
               