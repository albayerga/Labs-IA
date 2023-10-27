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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    stack = util.Stack() #frontier
    visited = [] #explored

    stack.push((start, [])) #in stack we push the first node and its path ([] rn)

    while not stack.isEmpty(): #while there are nodes in the stack
        
        node, path = stack.pop() #we pop the node and its path
        
        if node not in visited: #if the node is not explored yet
            visited.append(node) #we add it to the explored list

            if problem.isGoalState(node): #if the node is the goal state we return the path
                return path        
        
            else:
                successors = problem.getSuccessors(node) #we get the successors of the node
                for successor in successors: #for each successor
                    new_node = successor[0] 
                    new_path = path + [successor[1]] 
                    stack.push((new_node, new_path)) #we push the successor and its path to the stack
    
    return path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))


    start = problem.getStartState()
    queue = util.Queue() #frontier
    visited = [] #explored

    queue.push((start, [])) #in queue we push the first node and its path ([] rn)

    while not queue.isEmpty(): #while there are nodes in the queue
        node, path = queue.pop()

        if node not in visited: #if the node is not explored yet
            visited.append(node)

            if problem.isGoalState(node): #if the node is the goal state we return the path
                return path
            
            else:
                successors = problem.getSuccessors(node)
                for successor in successors:
                    new_node = successor[0]
                    new_path = path + [successor[1]]
                    queue.push((new_node, new_path))
    
    return path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    pqueue = util.PriorityQueue() #frontier
    visited = {} #explored
    
    init_node = (start, [], 0) #(state, action, cost)
    
    pqueue.push(init_node, 0) #in pqueue we push the first node and the cost
    
    while not pqueue.isEmpty():
        node, path, cost = pqueue.pop()
       
        if (node not in visited) or (cost < visited[node]):
            visited[node] = cost

            if problem.isGoalState(node):
                return path
            
            else:
                successors = problem.getSuccessors(node)
                
                for succ_node, succ_path, succ_cost in successors:
                    new_path = path + [succ_path]
                    new_cost = cost + succ_cost
                    new_node = (succ_node, new_path, new_cost)
                    pqueue.update(new_node, new_cost)

    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
