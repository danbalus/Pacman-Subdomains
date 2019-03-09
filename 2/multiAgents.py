# multiAgents.py
# --------------
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

import sys
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
class RandomAgent ( Agent ) :
    def getAction ( self , gameState ) :
        legalMoves = gameState . getLegalActions ()
        chosenIndex = random . choice ( range (0 , len ( legalMoves ) ) ) # Pick randomly among the legal
        return legalMoves [ chosenIndex ]

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)

        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        dist_G = []
        dist_F = []
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #for gp in successorGameState.getGhostPositions():
        #    dist_G.append(manhattanDistance(newPos, gp))
        #distanceToGhosts = min(dist_G)

        distanceToGhosts = [manhattanDistance(newPos, gp)
                            for gp in successorGameState.getGhostPositions()]
        distG = min(distanceToGhosts)
        #print "distG", distG
        mancare = currentGameState.getFood()
        for gp in mancare.asList():
            dist_F.append(manhattanDistance(newPos, gp))
        distanceToFood = min(dist_F)
        #print "distanceToFood", distanceToFood

        #print " New position ", newPos
        #print " Ghost positions ", successorGameState.getGhostPositions()
        #print " Distance to ghosts ", distanceToGhosts
        "*** YOUR CODE HERE ***"

        return successorGameState.getScore() - distanceToFood + distG
        #return min(distanceToFood, distanceToGhosts)
        


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        #print "self.depth: ", self.depth
        #print "self.evaluationFunction:", self.evaluationFunction
        #print "gameState.getLegalActions(): ",gameState.getLegalActions()
        #print "gameState: ", gameState
        #print "gameState.getNumAgents(): ", gameState.getNumAgents()
        #print "gameState.generateSuccessor() ", gameState.generateSuccessor(0,'West')
        "*** YOUR CODE HERE ***"
        #return 'Stop'
        return self.Min_max(gameState, 0, 1)

    def Min_max(self, gameState, agentIndex, depth):
        #print "agentIndex ",agentIndex
        if depth > self.depth or gameState.isLose() or gameState.isWin(): #cond te terminare
            return self.evaluationFunction(gameState)

        mutari = [] #lista cu mutarile bune a lui pacman ex: 'west', 'east'
        results = [] #punctajul lui pacman
        index_list= [] #indicii cu muarea buna
        for action in gameState.getLegalActions(agentIndex): #pt fiecare actiune
            #print "gameState.getLegalActions(agentIndex): ", gameState.getLegalActions(agentIndex)
            mutari.append(action)
        #print "mutari: ", mutari
        next_index = agentIndex + 1 #randul fantomei
        #print "gameState.getNumAgents(): ", gameState.getNumAgents()
        #print "next_index: ", next_index
        if next_index >= gameState.getNumAgents(): #nu mai ai unde face min max ca depaseste
            depth = depth + 1 #crestem adancimea
            next_index = 0  # resetam, trecem din nou la pacman

        for action in mutari: #pt fiecare actiune din mutari
            stare = gameState.generateSuccessor(agentIndex, action)
            x = self.Min_max(stare, next_index, depth)
            #print "x: ", x
            results.append(x)#punem scorul in lista
        #print "results: ", results
        if agentIndex == 0 and depth == 1:  # pacman prima mutare
            best_move = max(results) #alegem maximul
            for index in range(len(results)):
                #print "index: ",index
                if results[index] == best_move: #selectam "scorul" care are muarea cea mai buna
                    index_list.append(index)
                    #print "index_list: ",index_list
            k = min(index_list)  # se comporta mai bine cu min decat cu random/max
            # "mutari[k]: ", mutari[k]
            return mutari[k] #reurnam mutarea ex: 'west'

        if agentIndex == 0: #daca e pacman
            best_move = max(results)
            # print best_move
            return best_move
        #daca e fantoma
        best_move = min(results)
        # print best_move
        return best_move


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        #print "selffff --", self.alpha_beta_search(gameState, -999999, 999999, 0, 0)[0]
        return self.alpha_beta_search(gameState, -999999, 999999, 0, 0)[0] #ex:stop, west///[1]=scor

    def alpha_beta_search(self, gameState, alpha, beta, agent,  depth):
        #print "agent ", agent #ex 1 2 3 ... la care egent se ajunge
        if agent >= gameState.getNumAgents(): #penru a se reveni la primul agent
            #print "gameState.getNumAgents(): ",gameState.getNumAgents()
            depth = depth + 1  #creste adancimea
            agent = 0

        if (depth >= self.depth or gameState.isLose() or gameState.isWin()): #ca sus(cnd te term)
            return self.evaluationFunction(gameState) #ca sus
        else:#daca nu se e indeplinita cond de terminare
            if (agent == 0):  # pacman prima mutare
                return self.max_value(gameState, alpha, beta, agent, depth )
            else:  #fantome
                return self.min_value(gameState, alpha, beta, agent, depth)

    def max_value(self,gameState, alpha, beta, agent, depth):#pt pacman
        results = ["", -999999]# tupla cu 2 calri, aciunea si scorul
        #print "gameState.getLegalActions(agent):" , gameState.getLegalActions(agent) #ex:['West', 'Stop', 'East']

        for action in gameState.getLegalActions(agent): #actiunile posibile ale lui pacman
            stare_curenta = gameState.generateSuccessor(agent, action)
            #print "stare_curenta ",stare_curenta #ex: %G%  %        %.o%.%
            valoare = self.alpha_beta_search(stare_curenta,alpha, beta, agent + 1, depth )
            #print "valoare ", valoare
            if type(valoare) is list: #['East', 84.0]
                valoare_aux = valoare[1] #iau scorul
            else: #daca primese cnd de terminare
                valoare_aux = valoare #84.0
            if valoare_aux > results[1]: #daca scorul e mai mare
                results = [action, valoare_aux] #il alegem
            alpha = max(alpha, valoare_aux)#calc max
            if valoare_aux > beta:
                return [action, valoare_aux]
            #print "results ", results #ex: ['west', 323.0]
        return results #v



    #la fel ca max, difera inegalitatea si ceea ce comparam(alfa beta)
    def min_value(self,gameState, alpha, beta, agent, depth ):#pt fantome
        results = ["", 999999]
        #print "gameState.getLegalActions(agent):" , gameState.getLegalActions(agent) #ex:['West', 'Stop', 'East']

        for action in gameState.getLegalActions(agent):#actiunile posibile ale fantomelor
            stare_curenta = gameState.generateSuccessor(agent, action)
            # print "stare_curenta ",stare_curenta #ex: %G%  %        %.o%.%
            valoare = self.alpha_beta_search(stare_curenta,alpha, beta, agent + 1, depth )
            # print "valoare ", valoare
            if type(valoare) is list:
                valoare_aux = valoare[1]
            else:
                valoare_aux = valoare
            if valoare_aux < results[1]:
                results = [action, valoare_aux]
            beta = min(beta, valoare_aux)
            if valoare_aux < alpha:
                return [action, valoare_aux]
            # print "results ", results #ex: ['west', 323.0]
        return results




class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

