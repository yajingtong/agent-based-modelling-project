# project sumarry

GEOG5990 project

A simple model consists of two types agents: sheep and wolf, where sheep has fuction of eat ,move and share with neibors.
the data of agents are imported from website and the environment(grass) data is imported from file 'in.txt'.

The model is tests and demonstrates several features:

writting a model consists of multipule files

bulid agents in a space

reads in environmental data and initialise data from the web

get agents to interact with each other (share with neighbors)

gets agents interact with environment ('sheep' eat 'grass')

display the model as an animation

contained with in a GUI



## how to run
import files w.py agentframework.py
run in spyder(python3.7)


## Files
agentframework.py This defines 'sheep' agent,which implements the behavior of moving randomly across axes, based on random number,eat grass from 'environment',interact with each other in a cerntain distance.

w.py this defines 'wolf' agent, with behavior of moves ramdomly.

model.py This defines the model itself, including initialising the parameters and use matplotlib pakages to draw sactterplot of agents, including the animation of each change through iterations.
