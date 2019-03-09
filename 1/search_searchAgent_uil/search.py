# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import random

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """


    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def randomSearch(problem):
    current = problem.getStartState()
    solution = []
    while (not (problem.isGoalState(current))):
        succ = problem.getSuccessors(current)
        no_of_successors = len(succ)
        random_succ_index = int(random.random() * no_of_successors)
        next = succ[random_succ_index]
        current = next[0]
        solution.append(next[1])
    print "The  solution  is ", solution
    return solution

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #util.raiseNotDefined()
    "*** YOUR CODE HERE ***"
    solution = []  #path ul
    current_state = problem.getStartState()# stochez starea de inceput
    node_start = util.CustomNode(current_state, None,"root",0) #creez un nod ce contine --starea curenta-- actiunea ex:"West" ---parinte---cost      def __init__ (self , stare, actiune, parent , cost ):
    if problem.isGoalState(current_state):       #daca starea din care plec e chiar goal state
        return current_state                     #atunci o returnez
    #print "111  CURENT STATE: ", current_state
    frontier = util.Stack()    #creez o stiva
    #print "222"
    explored = []   #vor fi puse nodurile explorate si anume starea ex:(4,5)
    frontier.push(node_start)  #pun nodul pe stiva
    #print "333  ", node_start
    #node_aux = util.CustomNode((0,0), None, None, 0)
    #print "3334  ",node_aux
    while frontier.isEmpty() == 0: #atat timp cat mai sunt noduri
        #print "444"
        node_aux = frontier.pop()  #scoatem nodul de pe stiva
        #explored.append(node_aux.getStare())
        #print "555  " , node_aux, " nod stare  ", node_aux.getStare()
        stare_nod_aux = node_aux.getStare()  #salvez starea nodului scos
        #print "5556"
        if problem.isGoalState(stare_nod_aux):  #daca este goal state atunci
            #print "000"
            #solution.append(child.getParent().getStare())
            parent = node_aux
            while (parent.getParent() != "root"):  #cat timp nu s a ajuns la primul nod(radacina)
                #print "1111"
                solution.append(parent.getActiune()) # se salveaza aciunea pentru alcatuirea path ului
                parent = parent.getParent()          # se continua cu parintele nodului actual
                # solution.reverse()
            #print "2222"
            #print "SOLUTION--", solution
            solution.reverse()    #se inverseaza locul solutiilor deoarece s a plecat de la ultimul nod la primul in alcatuirea path ului
            return solution       #returnez path ul
        else:                                  #daca nu e goal state
            #print " abc"
            if (not (stare_nod_aux in explored)):  #daca nu s a vizia deja nodul
                #print "ccc"
                explored.append(stare_nod_aux)    #se pun in lista de noduri vizitate
                succ = problem.getSuccessors(stare_nod_aux)  #se stocheaza toti succesorii nodului
                for w in succ:     #pentru fiecare succesor al nodului  stare_nod_aux (starii)
                    # print "SUCCCCCC  " , succ
                    #print "777  succesorii: ", w, "node stare ", node_aux.getStare()
                    stare, actiune, cost = w                                 #despart succesorul in stare, actiune si cost
                    #print "w= ", w
                    child = util.CustomNode(stare, actiune, node_aux, cost)  #si le folosesc in alcatuirea nodului impreuna cu parintele acestuia(pt a putea alcatui path ul)
                    # stare, actiune, node_aux, cost) = parent
                    #print "888  child ", child, "stare=",stare, " actiune=",actiune, " node=",node_aux
                    if child.getStare() not in explored:  # or frontier:
                        #print "999"
                        #stare_get = child.getStare()
                        frontier.push(child)            #pun copilul in coada si la costul acestuia adaug euristica
                    # print "3333"




def breadthFirstSearch(problem):
    # util.raiseNotDefined()
    "*** YOUR CODE HERE ***"
    solution = [] #path ul
    current_state = problem.getStartState() # stochez starea de inceput
    node_start = util.CustomNode(current_state, None, "root", 0) #creez un nod ce contine --starea curenta-- actiunea ex:"West" ---parinte---cost      def __init__ (self , stare, actiune, parent , cost ):
    if problem.isGoalState(current_state):            #daca starea din care plec e chiar goal state
        return current_state                          #atunci o returnez
    # print "111  CURENT STATE: ", current_state
    frontier = util.Queue() #creez o coada
    # print "222"
    explored = []  #vor fi puse nodurile explorate si anume starea ex:(4,5)
    frontier.push(node_start)  #pun nodul in coada
    # print "333  ", node_start
    # node_aux = util.CustomNode((0,0), None, None, 0)
    # print "3334  ",node_aux
    while frontier.isEmpty() == 0: #atat timp cat mai sunt noduri
        # print "444"
        node_aux = frontier.pop() #scoatem nodul din coada
        # explored.append(node_aux.getStare())
        # print "555  " , node_aux, " nod stare  ", node_aux.getStare()
        stare_nod_aux = node_aux.getStare()   #salvez starea nodului scos
        # print "5556"
        if problem.isGoalState(stare_nod_aux): #daca este goal state atunci
            # print "000"
            # solution.append(child.getParent().getStare())
            parent = node_aux
            while (parent.getParent() != "root"):  #cat timp nu s a ajuns la primul nod(radacina)
                # print "1111"
                solution.append(parent.getActiune())  # se salveaza aciunea pentru alcatuirea path ului
                parent = parent.getParent()           # se continua cu parintele nodului actual
                # solution.reverse()
            # print "2222"
            # print "SOLUTION--", solution
            solution.reverse()     #se inverseaza locul solutiilor deoarece s a plecat de la ultimul nod la primul in alcatuirea path ului
            return solution        # returnez path ul
        else:                               #daca nu este goal state atunci
            # print " abc"
            if (not (stare_nod_aux in explored)):  #daca nu s a vizia deja nodul
                # print "ccc"
                explored.append(stare_nod_aux)   #se pun in lista de noduri vizitate
                succ = problem.getSuccessors(stare_nod_aux)  #se stocheaza toti succesorii nodului
                for w in succ:      #pentru fiecare succesor al nodului  stare_nod_aux (starii)
                    # print "SUCCCCCC  " , succ
                    # print "777  succesorii: ", w, "node stare ", node_aux.getStare()
                    stare, actiune, cost = w                                  #despart succesorul in stare, actiune si cost
                    # print "w= ", w
                    child = util.CustomNode(stare, actiune, node_aux, cost)   #si le folosesc in alcatuirea nodului impreuna cu parintele acestuia(pt a putea alcatui path ul)
                    # stare, actiune, node_aux, cost) = parent
                    # print "888  child ", child, "stare=",stare, " actiune=",actiune, " node=",node_aux
                    if child.getStare() not in explored:  # or frontier:
                        # print "999"
                        #stare_get = child.getStare()
                        frontier.push(child)               #pun copilul in coada
                        # print "3333"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
     # util.raiseNotDefined()
    "*** YOUR CODE HERE ***"
    #print problem
    solution = [] #path ul
    current_state = problem.getStartState() # stochez starea de inceput
    node_start = util.CustomNode(current_state, None, "root", 0) #creez un nod ce contine --starea curenta-- actiunea ex:"West" ---parinte---cost      def __init__ (self , stare, actiune, parent , cost ):
    if problem.isGoalState(current_state):          #daca starea din care plec e chiar goal state
        return current_state                        #atunci o returnez
    # print "111  CURENT STATE: ", current_state
    frontier = util.PriorityQueue() #creez o coada de prioritati
    # print "222"
    explored = []  #vor fi puse nodurile explorate si anume starea ex:(4,5)
    frontier.push(node_start, node_start.getCost())  #pun nodul  si costul acestuia in coada
   # print ";;;;;;;;;;;;;;;;;;;;;; ", node_start.getCost()
    # print "333  ", node_start
    # node_aux = util.CustomNode((0,0), None, None, 0)
    # print "3334  ",node_aux
    while frontier.isEmpty() == 0:   #atat timp cat mai sunt noduri
        # print "444"
        node_aux = frontier.pop()   #scoatem nodul din coada
        # explored.append(node_aux.getStare())
        # print "555  " , node_aux, " nod stare  ", node_aux.getStare()
        stare_nod_aux = node_aux.getStare()  #salvez starea nodului scos
        # print "5556"
        if problem.isGoalState(stare_nod_aux):     #daca este goal state atunci
            # print "000"
            # solution.append(child.getParent().getStare())
            parent = node_aux
            while (parent.getParent() != "root"):  #cat timp nu s a ajuns la primul nod(radacina)
                # print "1111"
                solution.append(parent.getActiune())  # se salveaza aciunea pentru alcatuirea path ului
                parent = parent.getParent()           # se continua cu parintele nodului actual
                # solution.reverse()
            # print "2222"
            # print "SOLUTION--", solution
            solution.reverse()     #se inverseaza locul solutiilor deoarece s a plecat de la ultimul nod la primul in alcatuirea path ului
            return solution        #returnez path ul
        else:                                     #daca nu este goal state atunci
            # print " abc"
            if (not (stare_nod_aux in explored)):   #daca nu s a vizia deja nodul
                # print "ccc"
                explored.append(stare_nod_aux)   #se pun in lista de noduri vizitate
                succ = problem.getSuccessors(stare_nod_aux)  #se stocheaza toti succesorii nodului
                for w in succ:      #pentru fiecare succesor al nodului  stare_nod_aux (starii)
                    # print "SUCCCCCC  " , succ
                    # print "777  succesorii: ", w, "node stare ", node_aux.getStare()
                    stare, actiune, cost = w                                                      #despart succesorul in stare, actiune si cost
                    # print "w= ", w                                                              #     |-----<la costul copilului se adauga si cel al parintelui (uniform cost)
                    child = util.CustomNode(stare, actiune, node_aux, cost + node_aux.getCost())  #si le folosesc in alcatuirea nodului impreuna cu parintele acestuia(pt a putea alcatui path ul)
                    # stare, actiune, node_aux, cost) = parent
                    # print "888  child ", child, "stare=",stare, " actiune=",actiune, " node=",node_aux
                    if child.getStare() not in explored:  # or frontier:
                        # print "999"
                        #stare_get = child.getStare()
                        #cost_parent = child.getParent().getCost()
                        frontier.push(child, child.getCost())         #pun copilul in coada
                        # print "3333"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """Search the node of least total cost first."""
     # util.raiseNotDefined()
    #print problem
    solution = []  #path ul
    current_state = problem.getStartState() # stochez starea de inceput
    node_start = util.CustomNode(current_state, None, "root", 0) #creez un nod ce contine --starea curenta-- actiunea ex:"West" ---parinte---cost      def __init__ (self , stare, actiune, parent , cost ):
    if problem.isGoalState(current_state):      #daca starea din care plec e chiar goal state
        return current_state                    #atunci o returnez
    # print "111  CURENT STATE: ", current_state
    frontier = util.PriorityQueue() #creez o coada de prioritati
    # print "222"
    explored = []   #vor fi puse nodurile explorate si anume starea ex:(4,5)
    frontier.push(node_start, node_start.getCost())  #pun nodul  si costul acestuia in coada
   # print ";;;;;;;;;;;;;;;;;;;;;; ", node_start.getCost()
    # print "333  ", node_start
    # node_aux = util.CustomNode((0,0), None, None, 0)
    # print "3334  ",node_aux
    while frontier.isEmpty() == 0:  #atat timp cat mai sunt noduri
        # print "444"
        node_aux = frontier.pop()   #scoatem nodul din coada
        # explored.append(node_aux.getStare())
        # print "555  " , node_aux, " nod stare  ", node_aux.getStare()
        stare_nod_aux = node_aux.getStare() #salvez starea nodului scos
        # print "5556"
        if problem.isGoalState(stare_nod_aux):        #daca este goal state atunci
            # print "000"
            # solution.append(child.getParent().getStare())
            parent = node_aux
            while (parent.getParent() != "root"):  #cat timp nu s a ajuns la primul nod(radacina)
                # print "1111"
                solution.append(parent.getActiune())  # se salveaza aciunea pentru alcatuirea path ului
                parent = parent.getParent()           # se continua cu parintele nodului actual
                # solution.reverse()
            # print "2222"
            # print "SOLUTION--", solution
            solution.reverse()       #se inverseaza locul solutiilor deoarece s a plecat de la ultimul nod la primul in alcatuirea path ului
            return solution          #returnam path ul
        else:                                       #daca nu este goal state atunci
            # print " abc"
            if (not (stare_nod_aux in explored)):  #daca nu s a vizia deja nodul
                # print "ccc"
                explored.append(stare_nod_aux)     #se pun in lista de noduri vizitate
                succ = problem.getSuccessors(stare_nod_aux)   #se stocheaza toti succesorii nodului
                for w in succ:        #pentru fiecare succesor al nodului  stare_nod_aux (starii)
                    # print "SUCCCCCC  " , succ
                    # print "777  succesorii: ", w, "node stare ", node_aux.getStare()
                    stare, actiune, cost = w                                                       #despart succesorul in stare, actiune si cost
                    # print "w= ", w                                                               #     |-----<la costul copilului se adauga si cel al parintelui (uniform cost)
                    child = util.CustomNode(stare, actiune, node_aux, cost + node_aux.getCost())   #si le folosesc in alcatuirea nodului impreuna cu parintele acestuia(pt a putea alcatui path ul)
                    # stare, actiune, node_aux, cost) = parent
                    # print "888  child ", child, "stare=",stare, " actiune=",actiune, " node=",node_aux
                    if child.getStare() not in explored:  # or frontier:             #daca starea copilului nu e
                        # print "999"
                        #stare_get = child.getStare()
                        #cost_parent = child.getParent().getCost()
                        frontier.push(child, child.getCost() + heuristic(stare,problem))   #pun copilul in coada si la costul acestuia adaug euristica
                        # print "3333"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
rs = randomSearch