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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    c = problem.getStartState()
    exploredState = []
    exploredState.append(start)
    states = util.Stack()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty() and not problem.isGoalState(c):
        state, actions = states.pop()
        exploredState.append(state)
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                c = i[0]
                direction = i[1]
                states.push((coordinates, actions + [direction]))
    return actions + [direction]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    exploredState = []
    exploredState.append(start)
    states = util.Queue()
    stateTuple = (start, [])
    states.push(stateTuple)
    while not states.isEmpty():
        state, action = states.pop()
        if problem.isGoalState(state):
            return action
        successor = problem.getSuccessors(state)
        for i in successor:
            coordinates = i[0]
            if not coordinates in exploredState:
                direction = i[1]
                exploredState.append(coordinates)
                states.push((coordinates, action + [direction]))
    return action
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    states = util.PriorityQueue()
    # visited[] contains all the visited coordinates (x,y)
    visited = []
    path_directions = []
    # getting the start coordinate of pacman from the given pacman environment (problem)
    start = problem.getStartState()

    # push the startState to the states of actions queue with initial empty list of actions
    states.push((start, []), 0)

    # while there are still state-actions,
    # continue searching for the least costly paths that leads to the goalState.
    while not states.isEmpty():
        state, path_directions = states.pop()
        # if this state is the goalState, return the path from startState to goalState
        if problem.isGoalState(state):
            return path_directions
        else:
            # if this state is not yet visited,
            # look for the next possible move (successors),
            # and calculate the total cost of paths
            if state not in visited:
                successors = problem.getSuccessors(state)
                # for each possible move,
                # if the state_coordinate is not yet visited,
                # add the new path and the cost of the path for this state.
                for scr in successors:
                    scr_state_coordinate = scr[0]
                    if scr_state_coordinate not in visited:
                        newPath = scr[1]
                        paths = path_directions + [newPath]
                        # getting the total cost when going through this path
                        cost = problem.getCostOfActions(paths)
                        # pushing this state with its corresponding path and cost
                        states.push((scr_state_coordinate, paths), cost)
            # setting this state as visited
            visited.append(state)
    return path_directions
    # --- ENDOF MY CODE ----
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    states = util.PriorityQueue()
    # visited[] contains all the visited coordinates (x,y)
    visited = []
    path_directions = []
    # getting the start coordinate of pacman from the given pacman environment (problem)
    start = problem.getStartState()

    # push the startState to the states of actions queue with initial empty list of actions
    states.push((start, []), 0)

    # while there are still state-actions,
    # continue searching for the least costly paths that leads to the goalState.
    while not states.isEmpty():
        state, path_directions = states.pop()
        # if this state is the goalState, return the path from startState to goalState
        if problem.isGoalState(state):
            return path_directions
        else:
            # if this state is not yet visited,
            # look for the next possible move (successors),
            # and calculate the total cost of paths
            if state not in visited:
                successors = problem.getSuccessors(state)
                # for each possible move,
                # if the state_coordinate is not yet visited,
                # add the new path and the cost of the path for this state.
                for scr in successors:
                    scr_state_coordinate = scr[0]
                    if scr_state_coordinate not in visited:
                        newPath = scr[1]
                        paths = path_directions + [newPath]
                        # In A* search, the score (cost) is based on the total cost of path and the heuristics
                        cost = problem.getCostOfActions(paths) + heuristic(scr_state_coordinate, problem)
                        # pushing this state with its corresponding path and cost
                        states.push((scr_state_coordinate, paths), cost)
            # setting this state as visited
            visited.append(state)
    return path_directions
    # --- ENDOF MY CODE
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
