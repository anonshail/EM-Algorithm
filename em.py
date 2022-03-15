import requests
import random

def getCoinFlipDraws():
  '''
  This function calls the coin flip API 30 times and returns data
  1) Calls coin flip API 30 Times
  2) Sends a 30x20 2D List containing the data
  '''
  data = []
  for i in range(30):
    coinFlips = requests.get('https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta')
    coinData = eval(coinFlips.json()["body"])
    data.append(coinData)
  return data

def theta(a, b):
  '''This function calculates theta and returns the value'''
  return (a / (a+b))

def probZAGivenE(thetaA, thetaB, noOfHeads, noOfTails):
  '''Calculates P(za|e) given P(A)'''
  ans = (thetaA**noOfHeads)*((1-thetaA)**noOfTails) / (((thetaA**noOfHeads)*((1-thetaA)**noOfTails))+((thetaB**noOfHeads)*((1-thetaB)**noOfTails)))
  return ans

def emSingleIteration(data, thetaA, thetaB):
  '''The implementation of the EM Algorithm'''

  headsA = 0 
  tailsA = 0
  headsB = 0
  tailsB = 0

  for draw in data:
    #for each draw

    #no of heads and tails
    noOfHeads = 0
    noOfTails = 0

    for coinFlip in draw:
      if(coinFlip == 1):
        noOfHeads += 1
      else:
        noOfTails += 1

    probCoinIsA = probZAGivenE(thetaA, thetaB, noOfHeads, noOfTails)

    probCoinIsB = (1 - probCoinIsA)

    headsA += (probCoinIsA * noOfHeads) 
    tailsA += (probCoinIsA * noOfTails)
    headsB += (probCoinIsB * noOfHeads)
    tailsB += (probCoinIsB * noOfTails)
  
  thetaA = theta(headsA, tailsA)
  thetaB = theta(headsB, tailsB)

  print('thetaA, thetaB', thetaA, thetaB)

  return [thetaA, thetaB]


def emAlgorithm():
  #first obtain the data
  data = getCoinFlipDraws()

  #initalize the bias to a random value
  thetaA = random.random()
  thetaB = random.random()

  #iterate 20 times until the biases converge
  for i in range(20):
    [thetaA, thetaB] = emSingleIteration(data, thetaA, thetaB)

emAlgorithm()

