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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    stack = util.Stack() #frontier
    visited = [] #explored
    stack.push((start,[])) #in stack we push the first node and its path to it ([] rn)

    while not stack.isEmpty(): #while there are nodes in the frontier
        node, path = stack.pop() #we pop the node and its path to it

        if not node in visited: #if the node is not visited yet
            visited.append(node) #we add it to the visited list

            if problem.isGoalState(node): #if the node is the goal state
                return path #we return the path to it
            
            successors = problem.getSuccessors(node) #we get the successors of the node
            for successor in successors: #for each successor
                newNode, newAction, cost = successor #we get the node, the action that leads to it and the cost (we don't need the cost but the autograder does)
                newPath = path + [newAction] #we add the action to the path and get the new path
                stack.push((newNode, newPath)) #we push the new node and its path to it to the stack
    
    return [] #if we don't find a path we return an empty list


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    queue = util.Queue() #frontier
    visited = [] #explored
    queue.push((start,[]))

    while not queue.isEmpty(): #same as DFS but with a queue (FIFO) instead of a stack (LIFO)
        node, path = queue.pop()

        if not node in visited:
            visited.append(node)

            if problem.isGoalState(node):
                return path
            
            successors = problem.getSuccessors(node)
            for successor in successors:
                newNode, newAction, cost = successor #again, we don't need the cost but the autograder does
                newPath = path + [newAction]
                queue.push((newNode, newPath))
    
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    pqueue = util.PriorityQueue() #frontier
    visited = [] #explored
    
    pqueue.push((start,[]), 0) #we push the first node, its path to it ([] rn) and the cost (0 rn)

    while not pqueue.isEmpty(): #same as BFS but with a priority queue instead of a queue
        node, path = pqueue.pop() #now we pop the node (and its path to it) with the lowest cost 
       
        if not node in visited:
            visited.append(node)

            if problem.isGoalState(node):
                return path
            
            successors = problem.getSuccessors(node)
            for successor in successors:
                newNode, newAction, cost = successor
                newPath = path + [newAction]
                priority = problem.getCostOfActions(newPath)
                pqueue.push((newNode, newPath), priority) 

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    start = problem.getStartState()
    pqueue = util.PriorityQueue() #frontier
    visited = [] #explored
    pqueue.push((start,[]), heuristic(start, problem)) #we push the first node, its path to it ([] rn) and the iniital heuristic

    while not pqueue.isEmpty(): #same as UCS but with a priority queue that takes into account the heuristic
        node, path = pqueue.pop()
        
        if not node in visited:
            visited.append(node)

            if problem.isGoalState(node):
                return path
            
            successors = problem.getSuccessors(node)
            for successor in successors:
                newNode, newAction, cost = successor
                newPath = path + [newAction]
                priority = problem.getCostOfActions(newPath) + heuristic(newNode, problem) #here we add the heuristic to the cost
                pqueue.push((newNode, newPath), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
