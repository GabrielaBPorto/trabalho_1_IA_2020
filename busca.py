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

def foiVisitado(estado, fila):
    for temp in fila.list:
        if temp == estado:
            return True
    return False

def tratamentoEstadoInicial(estado, inicial):
    if(estado != inicial):
        return estado[0]
    else:
        return estado

def adicionarFilhosNaoVisitadosNaListaParaVisitar(filhos, estadosVisitados, estadosAVisitar):
    for filho in filhos:
        if(not foiVisitado(filho[0],estadosVisitados)):
            estadosAVisitar.push(filho)

def pegaCaminhoDaBusca(goalAttained, problem, estadoSendoVisitado, direcoes):
    if(not(goalAttained is None)):
        vizinhos = problem.getSuccessors(goalAttained[0])
        for vizinho in vizinhos:
            if(vizinho[0] == estadoSendoVisitado[0]):
                direcoes.push(estadoSendoVisitado[1])
                goalAttained = estadoSendoVisitado
        return goalAttained

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
    goalAttained = False

    estadoInicial = problem.getStartState()
    filhos = problem.getSuccessors(estadoInicial)

    estadosVisitados = Stack()
    direcoes = Stack()

    estadosVisitados.push(estadoInicial)

    buscaEmProfundidade(problem, filhos, estadosVisitados, direcoes, goalAttained)

    return direcoes.list

def buscaEmProfundidade(problem, estados, estadosVisitados, direcoes, goalAttained):
    for estado in estados:
        if(not goalAttained):
            filhos = problem.getSuccessors(estado[0])

            if(not foiVisitado(estado[0],estadosVisitados)):
                estadosVisitados.push(estado[0])
                direcoes.push(estado[1])

                if(not problem.isGoalState(estado[0])):
                    goalAttained = buscaEmProfundidade(problem, filhos, estadosVisitados, direcoes, goalAttained)

                    if(not goalAttained):
                        direcoes.pop()
                    else:
                        return True
                else:
                    goalAttained = True
                    return True
        else:
            return False
               

def breadthFirstSearch(problem):
    """Busca primeiro os nos menos profundos na arvore de busca"""
    goalAttained = None

    estadoInicial = problem.getStartState()
    filhos = problem.getSuccessors(estadoInicial)

    estadosAVisitar = Queue()
    estadosVisitados = Stack()
    direcoes = Queue()

    estadosAVisitar.push(estadoInicial)
    buscaEmLargura(problem, estadosAVisitar, estadosVisitados, direcoes, goalAttained)

    return direcoes.list

def buscaEmLargura(problem, estadosAVisitar, estadosVisitados, direcoes, goalAttained):
    for i in range(0, len(estadosAVisitar.list)):
        if(goalAttained is None):

            estadoSendoVisitado = estadosAVisitar.pop()

            estadosVisitados.push(tratamentoEstadoInicial(estadoSendoVisitado, problem.getStartState()))

            if(not problem.isGoalState(estadoSendoVisitado[0])):

                filhos = problem.getSuccessors(tratamentoEstadoInicial(estadoSendoVisitado, problem.getStartState()))

                adicionarFilhosNaoVisitadosNaListaParaVisitar(filhos, estadosVisitados, estadosAVisitar)
                goalAttained = buscaEmLargura(problem, estadosAVisitar, estadosVisitados, direcoes, goalAttained)
                return pegaCaminhoDaBusca(goalAttained, problem, estadoSendoVisitado,direcoes)
            else:
                direcoes.push(estadoSendoVisitado[1])
                return estadoSendoVisitado
        else:
            return goalAttained
                


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
