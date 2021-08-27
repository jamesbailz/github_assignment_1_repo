# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:50:46 2021

Module that initialises arbitrary agents (y, x), manipulates them and 
calculates values from them.

Module classes:
    Agent

Module functions:
    __init__
    str 
    move 
    eat
    distance_between
    share_with_neighbours
    get_y
    get_x
    set_y
    set_x
"""
#import statements
import random

#Variable set up
rando = random.random

#Set up Agent class
class Agent ():
    #set up Agent class methods
    #Initialise Agents
    def __init__ (self, i, environment, agents, y, x, store):
        '''
        Initial Agent set up

        Parameters
        ----------
        i : int
            Assigns each agent with a unique i.d.
        environment : float
            Environment with which the agents interact
        agents : int
            Full co-ordinates of the agents
        y : int
            y value of the agents co-ordinate
        x : int
            x value of the agents co-ordinate
        store : int
            Value of the amount stored within an agent

        Returns
        -------
        None.

        '''
        self.i = i
        self.environment = environment
        self.agents = agents
        self.store = store
        self.nstore = 0
        self.neighbours = []
        self.shared_with = []
        self.shared_amount = 0
        self._y = y
        self._x = x
      
    #Agent description
    def __str__ (self):
        '''
        Taking and conversion of numbers to strings, 
        for input into an agent description 

        Returns
        -------
        string
            Agent: i.d.; y value; x value; store value

        '''
        return ("i = " + str(self.i) + ", y = " + str(self._y) \
                + ", x = " + str(self._x) + ", store = " + str(self.store))
    
    #Move agents
    def move (self):
        '''
        Moves the agents around the environment,
        based on random number generation.
        If random number < 0.5, agent moves positively in given direction.
        If random number > 0.5, agent moves negatively in given direction.

        Returns
        -------
        None.
        
        '''            
        if rando () <0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        if rando () <0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100                
    #Agents eat the environment
    def eat (self):
        '''
        Determines if an agent will 'eat' the environment and,
        add value to its store.
        If agent > 10, environment will be eaten by a value of 10,
        and this will be added to the agents store.

        Returns
        -------
        None.

        '''
        if self.environment [self._y][self._x] > 10:
            self.environment [self._y][self._x] -= 10
            self.store += 10
    
    '''
    #Initial distance between points function dec.
    def distance_between (agents_row_a, agents_row_b):
    """
    Given two arbitrary agents, return the distance between them

    agents_row_a : int
    agents_row_b : int
    return : float

    >>> a = agentframework.Agent(0,environment,agents,random.randint(0,99),random.randint(0,99))
    >>> a.x = 1
    >>> a.y = 2
    >>> b = agentframework.Agent(1,environment,agents,random.randint(0,99),random.randint(0,99))
    >>> b.x = 4
    >>> b.y = 6
    >>> distance_between(a,b)
    5.0

    """
    return (((agents_row_a.y - agents_row_b.y)**2) 
            + ((agents_row_a.x - agents_row_b.x)**2))**0.5
    '''        
    #Final distance between agents
    def distance_between (self, agents):
        '''
        Given two agents (self and agent), return the distance between them.

        Parameters
        ----------
        agents : int
            Full co-ordinates of the agents

        Returns
        -------
        float
            Distance between self and agent co-ordinates
        
        '''
        return (((self._y - agents._y)**2) + ((self._x - agents._x)**2))**0.5
    
    #Agents search for close neighbours and share resources
    def share_with_neighbours (self, neighbourhood):
        '''
        Determines if an agent is within the neighbourhood of another agent.
        If they are, calculates store amount agent 1 will share with agent 2.
        Note, agents will not share if they have done so already.

        Parameters
        ----------
        neighbourhood : int
            A value used to determine whether or not an agent is proximal
            to another agent. 

        Returns
        -------
        None.

        '''
        #print (type(self.neighbours))
        for agent in self.neighbours:
            #Check not already shared with the agent
            if (self.i not in agent.shared_with):
                total = self.share_amount + agent.share_amount
                average = total / 2
                self.nstore = self.nstore + average
                agent.nstore = agent.nstore + average
                self.shared_with.append (agent.i) 
                # print ("i=" + str(self.i) + ", store: " + str(self.store) +\
                #        " shares with i = " + str(agent.i) + ", store: " +\
                #            str(agent.store) + ": avg = " + str(average))
                               
    #getter method
    def get_y(self):
        '''
        Function to get an attribute value for y

        Returns
        -------
        int
            y value

        '''
        return self._y
    
    def get_x(self):
        '''
        Function to get an attribute value for x

        Returns
        -------
        int
            x value

        '''
        return self._x
    
    #setter method
    def set_y(self, value):
        '''
        Function to set an attribute value for y

        Parameters
        ----------
        value : int
            y value

        Returns
        -------
        None.

        '''
        self._y = value
        
    def set_x(self, value):
        '''
        Function to set an attribute value for x

        Parameters
        ----------
        value : int
            x value

        Returns
        -------
        None.

        '''
        self._x = value
    
    #Property object creation
    y = property (get_y, set_y)
    x = property (get_x, set_x)

#Call doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod ()
