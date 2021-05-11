#A gent-based modeling

project summary


A simple model consists of two types agents: sheep and wolf, where sheep has function of eat, move and share with neighbours. When run , the model displays a animation with the change of agents and environments .The data of agents are imported from website and the environment(grass) data is imported from file 'in.txt'.

The model is tests and demonstrates several features:

- writing a model consists of multiple files

- build agents in a space

- reads in environmental data and initialise data from the web

- get agents to interact with each other (share with neighbors)

- gets agents interact with environment ('sheep' eat 'grass')

- display the model as an animation

- contained within a GUI



## how to run
import files w.py and agentframework.py 
run model in Spyder(python3.7)


## Files
agentframework.py This defines 'sheep' agent, which implements the behaviour of moving randomly across axes, based on random number, eat grass from 'environment’, interact with each other in a certain distance.

w.py This defines 'wolf' agent, with behaviour of moves randomly.

model.py This defines the model itself, including initialising the parameters and use matplotlib packages to draw scatterplot of agents, including the animation of each change through iterations. In the model, sheep are represented by white scatters and wolf with black color.
## known issues
The two objects are lack of interactions, certain function need further change to run effectively.
