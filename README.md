# Assignment_1 GitHib README
## Contents
1. ABM_final.py: Python file - the main model associated with this assignment and is the program to be run.         
2. agentframework.py: Python file - associated module containing the class and functions relevant to the program.        
3. WebData.txt: Text file - downloadable (X, Y) data for input and use in the program.                                     
4. agentstore.txt: Text file - contains a list of agent stores within the program as well as the agents' location and id.
5. environment.txt: Text file - contains a list of integer data for use as the background environment for the program.
6. LICENCE: File - contains information regarding the licencing of the contents associated with this program.
### What is the software?
Generates a number of agents to interact with an environment. Agents are moved around the environment, 
eat the environment and share some of what they have eaten depending on their proximity to another agent. 
Various data is writen out to the text files mentioned in the contents page, with useful information printed to the console.
### How can the software be run?
User input variables are set up with lower and upper limits specified for each. This is set up for the number of agents,
number of iterations and the size of the neighbourhood (used to calculate whether or not an agent will share with another).
### What are the expected outputs?
An animation of the specified number of agents moving around and eating the background environment will appear in a pop-up
window. Guidlines for how the program is running will be printed to the console as well as key data from the program (such as
initial and final agent location and store details).
