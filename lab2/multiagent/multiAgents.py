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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

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
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
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
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        newFood = currentGameState.getFood().asList() # list of food
        closestFood = float("inf") 
        closestGhost= float("inf")

        #get the closest food
        for food in newFood:
            closestFood = min(closestFood, manhattanDistance(newPos, food))

        #get the closest ghost
        for ghost in successorGameState.getGhostPositions():
            closestGhost = min(closestGhost, manhattanDistance(newPos, ghost))
        
        #if the ghost is too close, return -inf
        if closestGhost < 2:
            return float("-inf")

        #if there is no food left, return inf
        if closestFood == 0:
            return float("inf")

        #return the reciprocal of the closest food and the closest ghost  
        return closestGhost / closestFood


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

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        return self.max_pacman(gameState, 0, 0)[0]  #We are going to work with a 2 pos array where index 0 will be state actions and index 1 the actions value

    def minimax(self, gameState, agentIndex, depth): #MiniMax recursive primary function
        if (depth == (self.depth * gameState.getNumAgents())) or gameState.isWin() or gameState.isLose(): #Return when we are on a final state
            return self.evaluationFunction(gameState)
        if agentIndex == 0: #When we are pacman (max)
            return self.max_pacman(gameState, agentIndex, depth)[1]
        else: #When we are ghosts (min)
            return self.min_ghost(gameState, agentIndex, depth)[1]

    def max_pacman(self, gameState, agentIndex, depth):  #Max function
        highestAction = ("",-float('inf'))
        for action in gameState.getLegalActions(agentIndex):
            succAction = (action,self.minimax(gameState.generateSuccessor(agentIndex,action), (depth + 1) % gameState.getNumAgents(), depth+1))
            highestAction = max(highestAction,succAction,key=lambda x:x[1]) #We want to compare action value for each of them and take the maximum one
        return highestAction

    def min_ghost(self, gameState, agentIndex, depth):
        lowestAction = ("",float('inf'))
        for action in gameState.getLegalActions(agentIndex):
            succAction = (action,self.minimax(gameState.generateSuccessor(agentIndex,action), (depth + 1) % gameState.getNumAgents(), depth+1))
            lowestAction = min(lowestAction,succAction,key=lambda x:x[1])  #We want to compare action value for each of them and take the minimum one
        return lowestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.max_pacman(gameState, 0, 0, -float("inf"), float("inf"))[0]  #Again, we are going to use a two position variable, our return will be the actions list

    def alphabeta(self, gameState, agentIndex, depth, alpha, beta):  #In this case we are going to copy the same recursive code structure of minimax algorythm. Alpha and beta now are part of our function arguments
        if (depth is self.depth * gameState.getNumAgents()) or gameState.isLose() or gameState.isWin():  #Access when we are on a recursive final state
            return self.evaluationFunction(gameState)
        if agentIndex == 0: #Pacman
            return self.max_pacman(gameState, agentIndex, depth, alpha, beta)[1]
        else:  #Ghosts
            return self.min_ghost(gameState, agentIndex, depth, alpha, beta)[1]

    def max_pacman(self, gameState, agentIndex, depth, alpha, beta):
        highestAction = ("",-float('inf'))
        for action in gameState.getLegalActions(agentIndex):
            succAction = (action,self.alphabeta(gameState.generateSuccessor(agentIndex,action), (depth + 1) % gameState.getNumAgents(), depth+1, alpha, beta))
            highestAction = max(highestAction,succAction,key=lambda x:x[1])  #We want to compare action value for each of them and take the maximum one

            #If prunning
            if highestAction[1] > beta:
                return highestAction
            else:
                alpha = max(alpha, highestAction[1]) #Alpha assignment

        return highestAction

    def min_ghost(self, gameState, agentIndex, depth, alpha, beta):
        lowestAction = ("",float('inf'))
        for action in gameState.getLegalActions(agentIndex):
            succAction = (action,self.alphabeta(gameState.generateSuccessor(agentIndex,action), (depth + 1) % gameState.getNumAgents(), depth+1, alpha, beta))
            lowestAction = min(lowestAction,succAction,key=lambda x:x[1])  #We want to compare action value for each of them and take the minimum one

            # Prunning
            if lowestAction[1] < alpha:
                return lowestAction
            else:
                beta = min(beta, lowestAction[1]) #Beta assignment

        return lowestAction


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
