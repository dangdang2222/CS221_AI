from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

## Example Agent
class ReflexAgent(Agent):

  def Action(self, gameState):

    move_candidate = gameState.getLegalActions()

    scores = [self.reflex_agent_evaluationFunc(gameState, action) for action in move_candidate]
    bestScore = max(scores)
    Index = [index for index in range(len(scores)) if scores[index] == bestScore]
    get_index = random.choice(Index)

    return move_candidate[get_index]

  def reflex_agent_evaluationFunc(self, currentGameState, action):

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()



def scoreEvalFunc(currentGameState):

  return currentGameState.getScore()

class AdversialSearchAgent(Agent):

  def __init__(self, getFunc ='scoreEvalFunc', depth ='2'):
    self.index = 0
    self.evaluationFunction = util.lookup(getFunc, globals())

    self.depth = int(depth)

######################################################################################

class MinimaxAgent(AdversialSearchAgent):
  """
    [문제 01] MiniMax의 Action을 구현하시오. (20점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    maximum = -float("inf")
    actions = gameState.getLegalActions(0)
    i=0

    while i<len(actions):
      action = actions[i]

      v = self.Min_Value(gameState.generateSuccessor(0, action), 1 , 0)
      if(maximum<v):
        maximum = v
        result_move = action
      i=i+1
    #print(maximum)
    return result_move
  def Max_Value(self, gameState,index,depth):
    if gameState.isLose() or gameState.isWin() or depth == self.depth:
      return self.evaluationFunction(gameState)
    
    maxx = -float("inf")
    actions = gameState.getLegalActions(0)
    i=0

    while i<len(actions):
      action = actions[i]
      maxx = max(maxx,self.Min_Value(gameState.generateSuccessor(0,action),1,depth))
      i=i+1
    return maxx

  def Min_Value(self, gameState, index, depth):
    if gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    minn = float("inf")
    actions = gameState.getLegalActions(index)
    i=0

    while i<len(actions):
      action = actions[i]

      if index+1<gameState.getNumAgents(): #ghost
        minn = min(minn,self.Min_Value(gameState.generateSuccessor(index,action),index+1,depth))
      elif index+1 == gameState.getNumAgents(): #pacman
        minn = min(minn,self.Max_Value(gameState.generateSuccessor(index,action),0,depth+1))
      else: #error
        print("error")
        return -1
      i=i+1
    return minn

class AlphaBetaAgent(AdversialSearchAgent):
  """
    [문제 02] AlphaBeta의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    alpha = -float("inf")
    beta = float("inf")  
    maximum = -float("inf")

    actions = gameState.getLegalActions(0)
    i=0

    while i<len(actions):
      action = actions[i]
      v = self.AB_Min_Value(gameState.generateSuccessor(0, action), 1 , 0,alpha,beta)
      if(maximum<v):
        maximum = v
        result_move = action
        #alpha = max(alpha,maximum)
        alpha = v
      i=i+1
    #print(maximum)
    return result_move
  def AB_Max_Value(self,gameState, index,depth,alpha,beta):
    if gameState.isLose() or gameState.isWin() or depth == self.depth or len(gameState.getLegalActions(0)) == 0:
      return self.evaluationFunction(gameState)
    
    maxx = -float("inf")
    actions = gameState.getLegalActions(index)
    i=0

    while i<len(actions):
      action = actions[i]

      vv = self.AB_Min_Value(gameState.generateSuccessor(index,action),1,depth,alpha,beta)
      if(vv>maxx):
        maxx=vv
      if(maxx>beta):
        return maxx
      alpha = max(alpha,maxx)

      i=i+1
    return maxx

  def AB_Min_Value(self,gameState,index,depth,alpha,beta):
    if gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    minn = float("inf")
    actions = gameState.getLegalActions(index)
    i=0

    while i<len(actions):
      action = actions[i]

      if index+1<gameState.getNumAgents():
        vv = self.AB_Min_Value(gameState.generateSuccessor(index,action),index+1,depth,alpha,beta)
      elif index+1 == gameState.getNumAgents():
        vv = self.AB_Max_Value(gameState.generateSuccessor(index,action),0,depth+1,alpha,beta)
      else:
        print("error")
        return -1

      if(vv<minn):
        minn=vv
      if(minn<alpha):
        return minn
      beta = min(beta,minn)
      i=i+1
    return minn
class ExpectimaxAgent(AdversialSearchAgent):
  """
    [문제 03] Expectimax의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    maximum = -float("inf")

    actions = gameState.getLegalActions(0)
    i=0

    while i<len(actions):
      action = actions[i]
      v = self.EX_Chance_Value(gameState.generateSuccessor(0, action), 1 , 0)
      if(maximum<v):
        maximum = v
        result_move = action
      i=i+1
    return result_move 
  def EX_Max_Value(self, gameState,index,depth):
    if gameState.isLose() or gameState.isWin() or depth == self.depth:
      return self.evaluationFunction(gameState)
  
    maxx = -float("inf")
    actions = gameState.getLegalActions(0)
    i=0

    while i<len(actions):
      action = actions[i]
      maxx = max(maxx,self.EX_Chance_Value(gameState.generateSuccessor(0,action),1,depth))
      i=i+1
    return maxx

  def EX_Chance_Value(self, gameState, index, depth):
    if gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    sum = 0
    actions = gameState.getLegalActions(index)
    i=0

    while i<len(actions):
      action = actions[i]

      if index+1<gameState.getNumAgents(): #ghost
        sum += self.EX_Chance_Value(gameState.generateSuccessor(index,action),index+1,depth)
      elif index+1 == gameState.getNumAgents(): #pacman
        sum += self.EX_Max_Value(gameState.generateSuccessor(index,action),0,depth+1)
      else: #error
        print("error")
        return -1
      i=i+1
    
    result = sum/len(actions)
    return result