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
In busca.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from lib.searchProblem import SearchProblem

import lib.util as util
from lib.util import Stack, Queue, PriorityQueue
'''
Uso da pilha:
stack = Stack()
stack.push(element)
l = stack.list # Lista de elementos na pilha
e = stack.pop()

Uso da fila:
queue = Queue()
queue.push(element)
l = queue.list # Lista de elementos na fila
e = queue.pop()

Uso da fila de prioridades:
queuep = PriorityQueue()
queuep.push(element, value) # Valores baixos indicam maior prioridade
queuep.update(element, value) # Atualiza o valor de prioridade  de um elemento
l = queuep.heap # Lista de elementos na fila
e = queuep.pop()
'''

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
    Busca primeiro os nos mais profundos na arvore de busca

    Seu algoritmo deve retornar uma lista de acoes que atinja o objetivo.
    """
    "*** YOUR CODE HERE ***"
    # print problem.getStartState()
    # print problem.isGoalState(problem.getStartState())
    print problem.getSuccessors(problem.getStartState())

    estadoAtual = problem.getStartState()
    filhos = problem.getSuccessors(estadoAtual)

    estadosVisitados = Queue()
    direcoes = Stack()

    estadosVisitados.push(estadoAtual)

    buscaEmProfundidade(problem, filhos, estadosVisitados, direcoes)

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    # return [s, s, w, s, w, w, s, w]

    print '*'
    print direcoes.list
    return direcoes.list

def buscaEmProfundidade(problem, estados, estadosVisitados, direcoes):
    for estado in estados:
        
        if(not problem.isGoalState(estado) and not foiVisitado(estado[0],estadosVisitados)):
            print estado
            estadosVisitados.push(estado[0])
            direcoes.push(estado[1])
            print estadosVisitados.list
            print direcoes.list
            filhos = problem.getSuccessors(estado[0])
            # print '*'
            # print filhos
            buscaEmProfundidade(problem, filhos, estadosVisitados, direcoes)
        
def foiVisitado(estado, fila):
    for temp in fila.list:
        if temp == estado:
            return True
        
    return False

def breadthFirstSearch(problem):
    """Busca primeiro os nos menos profundos na arvore de busca"""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Busca primeiro os nos com o menor custo total"""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Busca primeiro os nos que tem a menor combinacao de custo total e heuristica"""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
