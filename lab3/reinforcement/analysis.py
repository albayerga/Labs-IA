# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0 #changed value -> ignore cliff
    return answerDiscount, answerNoise
"""
the grid only has one exit, so the discount factor should be high to prioritize long term rewards
and the noise should be 0 to ignore the cliff and have some chance of reaching the exit
"""

#higher discount factor -> prioritize long term rewards
#lower discount factor -> prioritize short term rewards
#higher noise -> avoids risks
#lower noise -> takes risks (0 -> ignores risks)

def question3a(): #prefer close exit (+1), risking cliff (-10)
    answerDiscount = 0.2 #focus on short term rewards
    answerNoise = 0 #ignore cliff
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b(): #prefer close exit (+1), but avoiding cliff (-10)
    answerDiscount = 0.4 #focus on short term rewards
    answerNoise = 0.3 #avoid cliff
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c(): #prefer distant exit (+10), risking cliff (-10)
    answerDiscount = 1 #focus on long term rewards
    answerNoise = 0 #ignore cliff
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d(): #prefer distant exit (+10), avoiding cliff (-10)
    answerDiscount = 0.9 #focus on long term rewards
    answerNoise = 0.4 #avoid cliff
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e(): #avoid both exits and cliff
    answerDiscount = 0 #ignore rewards
    answerNoise = 0 #ignore cliff
    answerLivingReward = 0 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
