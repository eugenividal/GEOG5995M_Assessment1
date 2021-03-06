# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:31:34 2017
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni Vidal
"""
import random

# Define an Agent class.
class Agent():
    def __init__(self, environment, agents):
        self.agents = agents
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)

# Method to move.
# % is a torus boundary in order to keep the agents inside the defined environment.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

# Method to eat. 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
 
# Method to search for close neighbours and share resources with them.          
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
                #print("sharing" + str(dist)+" " + str(ave))

#Work out the distance between agents (Pythagoras' theorem)
    def distance_between (self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5