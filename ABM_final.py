# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:12:20 2021

@author: james
"""
#import statements
import random
import matplotlib
matplotlib.use ('TkAgg')
import tkinter
import matplotlib.pyplot
import matplotlib.animation
import time
import agentframework
import csv
import requests
from bs4 import BeautifulSoup

#Variable and Command Line Argument creation
#Initial variable set up
num_of_agents = 0
num_of_iterations = 0
neighbours = 0
#Print statement to show
#Timing start
print ("Program start", '\n')
start = time.time ()
print ("Please enter program inputs as intsructed.", '\n')
#Agent number user input set up
print ("Please enter an Agent integer between 1 and 25")
while True:
    try:
        num_of_agents = int (input ('Enter Agents: ') or "10")
        assert 0 < num_of_agents < 26
    except (ValueError, AssertionError):
        print ("Please see variable restrictions above")
    else:
        break
print ('\n',"Agents: ", num_of_agents)
    
#Iteration number user input set up
print ('\n', "PLease enter an Iteration integer between 1 and 100")
while True:
    try:
        num_of_iterations = int (input ('Enter Iterations: ') or "100")
        assert 0 < num_of_iterations < 101
    except (ValueError, AssertionError):
        print ("Please see variable restrictions above")
    else:
        break
print ('\n', 'Iterations: ', num_of_iterations)
#Neighbourhood number user input set up
print ('\n', "Please enter a Neighbourhood integer betweeen 1 and 20")
while True:
    try:
        neighbourhood = int (input ('Enter Neighbourhood: ') or "20")
        assert 0 < neighbourhood < 21
    except (ValueError, AssertionError):
        print ("Please see variable restrictions above")
    else:
        break
print ('\n', "Neighbourhood: ", neighbourhood)

#Downloading web data
url = 'https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get(url)
content = r.text
print ("Web data downloaded")
#Check status code - looking for 200
print ("Status code = " + str(r.status_code))
if r.status_code == 200:
    print ("Download pass")
else:
    print ("Download fail")
#Scraping web data
print ("Scraping data")
soup = BeautifulSoup (content, 'html.parser')
#Find table
table = soup.find(id="yxz")
#Create x and y attribute lists
y_attr = []
x_attr = []
#Find x and y data
y_attr = soup.find_all (attrs={"class" : "y"})
x_attr = soup.find_all (attrs={"class" : "x"})
#Remove tags from data
no_tags_y = str(y_attr)
clean_y = BeautifulSoup (no_tags_y, "lxml").get_text ()
no_tags_x = str(x_attr)
clean_x = BeautifulSoup (no_tags_x, "lxml").get_text ()
#Check y and x attribute data
#print (y_attr)
#print (x_attr)
#Check clean y and x attribute data
#print (clean_y)
#print (clean_x)
#Write data out to a file
print ("Writing data to WebData.txt")
with open ('WebData.txt', 'w') as F:
    F.write ("y=" + str (clean_y))
    F.write ('\n')
    F.write ("x=" + str (clean_x))
    F.write ('\n')
print ("Scraping complete")

#Set the seed - constant Agent values for testing
#random.seed (0)
#random.seed (4)

#List creation
environment = []
agents = []

#Reading csv data, linking environment to the agents
print ("Reading in environment data")
with open ('environment.txt', newline = '') as F2:
    reader = csv.reader (F2, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        environment.append (rowlist)
        for value in row:
            rowlist.append (value)
#Linking agents to each agent
for row in agents:
    rowlist = []
    agents.append (agents)
    for value in row:
        rowlist.append (value)
#print (agents)

#Set up plot for animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes ([0, 0, 1, 1]) 

#Set up agents using web data
for i in range (num_of_agents):
    y = int (y_attr[i % len(y_attr)].text)
    x = int (x_attr[i % len(x_attr)].text)
    agents.append (agentframework.
                   Agent(i, environment,agents, y, x, \
                         random.randint (0,10)))

'''
#Test module move function
a = agentframework.Agent\
    (1,environment,random.randint(0,99),random.randint(0,99))
print (a.y, a.x)
a.move()
print (a.y, a.x)
'''

#Print initial agent details
for a in agents:
    print ("Initial details: " + str(a))
    
#Timing-1 end
end1 = time.time ()
print ("Time to Animation = " + str (end1 - start))

#Animation function declaration 
carry_on = True
def update (frame_number):
    '''
    Defines how the contents of each frame within the final animation change.

    Parameters
    ----------
    frame_number : int
        Frame number within the animation

    Returns
    -------
    None.

    '''
    fig.clear ()
    global carry_on
    #random.shuffle (agents)
    #print ("Agents moving")
    for a in agents:
        a.move()
    #print ("Agents eating")
    for a in agents:
        a.eat()
    #print ("Agents preparing to share")
    #Create lists for each agent with ids of agents within distance
    for a in agents:
        a.nstore = 0
        a.shared_with = []
        a.neighbours = []
        #Call distance function
        for b in agents:
            if (a.i != b.i):
                distance = a.distance_between (b)
                #Check distance
                #print ("Distance = " + str(distance))
                if distance <= neighbourhood:
                    a.neighbours.append (b)
    #Calculate share amount for agents that are going to share
    #print ("Agents calculating share amount")
    for a in agents:
        if (len(a.neighbours) == 0):
            a.nstore = a.store
        else:
            a.share_amount = a.store/ len (a.neighbours)
    #print ("Agents share")
    for a in agents:
        a.share_with_neighbours (neighbourhood)
    #print ("Agents finish share")
    for a in agents:
        a.store = a.nstore
    #Stopping condition set up
    if a.store >= 750:
        carry_on = False
        print ("Stopping Condition Met")
        for i in range (num_of_agents):
            print ("Final details: " + str(agents[i]))
    #Setting up plot
    matplotlib.pyplot.xlim (0,99)
    matplotlib.pyplot.ylim (0,99)
    #Linking environment to plot
    matplotlib.pyplot.imshow (environment)
    #Linking agents to plot
    for i in range (num_of_agents):
        matplotlib.pyplot.scatter (agents [i].x, agents [i].y)
#Generation function declaration
def gen_function (b = [0]):
    '''
    Determines animation lasts long enough for all iterations to have been
    passed through.

    Parameters
    ----------
    b : int
        Initial iteration number. The default is [0].

    Yields
    ------
    a : int
        Current iteration number being animated

    '''
    a = 0
    global carry_on
    #Limit number of frames to 100
    while (a < 100) & (carry_on):
        #print (a)
        yield a
        print ("Agent Analysis, Frame: " + str(a))
        a = a + 1

#Writing out total amount stored by agents to agentstore.txt
#Defining total store
total = 0
for a in agents:
    total = total + a.store
print ("Total Store = " + str(total))
#Writing store per agent and total stored to a text file
with open ('agentstore.txt', 'w', newline = '') as F3:
    #Total for each agent
    for a in agents:
        F3.write (str(a))
        F3.write ('\n')
        #print (str(a))
    #Total for all agents
    F3.write ("total store = " + str(total))
    F3.write ('\n')
    #print (str(total))

#Function to run model
print ("Begin Agent Analysis")
def run ():
    '''
    Displays animation of agents moving around and eating the environment.

    Returns
    -------
    None.

    '''
    animation = matplotlib.animation\
               .FuncAnimation (fig, update, frames=gen_function, repeat=False)
    #canvas.show ()
    canvas.draw ()
    return

#Building program window
root = tkinter.Tk ()
root.wm_title ("Model")
canvas = matplotlib.backends.backend_tkagg\
         .FigureCanvasTkAgg (fig, master=root)
canvas._tkcanvas.pack (side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#Making a menu
menu_bar = tkinter.Menu (root)
root.config (menu=menu_bar)
model_menu = tkinter.Menu (menu_bar)
#Making sub-menu
menu_bar.add_cascade (label = "Model", menu = model_menu)
#Linking run command
model_menu.add_command (label = "Run model", command = run)
tkinter.mainloop ()
    
#Timing-2 end
end2 = time.time ()
#Time to completion dependant on speed of animation closure
print ("Time to Completion = " + str (end2 - start))
print ("Program End")
