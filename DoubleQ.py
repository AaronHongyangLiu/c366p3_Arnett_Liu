import mountaincar
from pylab import *

Q1 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q2 = 0.00001*rand(181, 2)  # NumPy array of correct size
Q1[0,:] = 0
Q2[0,:] = 0
GAMMA = 1

def learn(alpha, eps, numTrainingEpisodes):
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0
        S = mountaincar.init()
        R, S = mountaincar.sample(S, 1)
        G += R
        while (S):
            Q = Q1[S,:]+Q2[S,:]
            prob1 = np.random.random()
            if prob1 < eps:
                # explore
                A = np.random.choice([0, 1])
            else:
                # greedy
                A = Q.argmax()

            R, S_prime = mountaincar.sample(S, A)
            G += R
            S_prime = int(S_prime)

            prob2 = np.random.choice([1, 2])
            if prob2 == 1:
                Q1[S, A] = Q1[S, A] + alpha * (
                R + GAMMA * Q2[S_prime, (Q1[S_prime]).argmax()] - Q1[S, A])
            else:
                Q2[S, A] = Q2[S, A] + alpha * (R + GAMMA * Q1[S_prime, (Q2[S_prime]).argmax()] - Q2[S, A])

            S = S_prime
        #print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
        #if episodeNum % 10000 == 0 and episodeNum != 0:
         #   print("Average return so far: ", returnSum/episodeNum)

def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        G = 0
        S = mountaincar.init()
        R, S = mountaincar.sample(S, 1)
        G += R
        while (S):
            Q = Q1[S,:]+Q2[S,:]
            A = Q.argmax()
            R, S = mountaincar.sample(S,A)
            G += R

        returnSum = returnSum + G
    return returnSum / numEvaluationEpisodes

def policy(state):
    Q = Q1[state,:]+Q2[state,:]
    return Q.argmax()

learn(0.001,1,1000000)

learn(0.001,0.01,1000000)

