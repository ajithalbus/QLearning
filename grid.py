import gym
import gym_grid
import numpy as np
import sys
 
import argparse
import matplotlib.pyplot as plt
from algos import runQGame,runSarsaGame,runSarsaLambdaGame
def checkArgs(args=None):
	parser = argparse.ArgumentParser(description='Grid World')
	parser.add_argument('--alpha',help = 'Learning Rate(alpha)', default = 0.5,type=float)
	parser.add_argument('--epsilon',help = 'epsilon for exploration', default= 0.1,type=float)
	parser.add_argument('--gamma',help = 'Discount rate', default=0.9,type=float)
	parser.add_argument('--episodes',help = 'Number of episodes',default=1000,type=int)
	parser.add_argument('--verbose',help = 'Verbosity', action='store_true',default=False)
	parser.add_argument('--grid',help = 'A/B/C', default='A')
	parser.add_argument('--render',help = 'Render Environment', action='store_true',default=False)
	parser.add_argument('--show-policy',help='Show policy at end',action='store_true',default=False)
	parser.add_argument('--algo',help='Learning algorithm[Q/SARSA/SARSAlam]',default='Q')
	parser.add_argument('--games',help='Number of games',default=1,type=int)
	parser.add_argument('--lam',help='Lambda for sarsa-lambda',default=0.5,type=float)
	args = parser.parse_args(args)
	return args



envs={'A':'grid-v0','B':'grid-v1','C':'grid-v2'}
if __name__ =='__main__':
	np.random.seed(1234)
	args=checkArgs(sys.argv[1:])
	print "Starting With : ",args
	
	stepsOfGames,returnsOfGames=[],[]
	
	if args.algo=='Q':
		runGame=runQGame
	elif args.algo=='SARSA':
		runGame=runSarsaGame
	elif args.algo=='SARSAlam':
		runGame=runSarsaLambdaGame
	
	env=gym.make(envs[args.grid])

	for i in range(args.games):
		print 'game :',i
		Steps,Returns = runGame(env,episodes=args.episodes,render=args.render,
		showPolicyAtEnd=args.show_policy,verbose=args.verbose,alpha=args.alpha,epsilon=args.epsilon,gamma=args.gamma,lam=args.lam)

		stepsOfGames.append(Steps)
		returnsOfGames.append(Returns)
	stepsOfGames=np.mean(np.array(stepsOfGames),axis=0)
	returnsOfGames=np.mean(np.array(returnsOfGames),axis=0)
	#print returnsOfGames

	xaxis=range(len(stepsOfGames))
	
	print 'Ploting Results'
	plt.title(args.algo+' - Grid '+args.grid)	
	plt.xlabel('Episodes')
	plt.ylabel('Number of Steps')
	plt.plot(xaxis,stepsOfGames)
	plt.show()
	plt.title(args.algo+' - Grid '+args.grid)
	plt.xlabel('Episodes')
	plt.ylabel('Return')
	plt.plot(xaxis,returnsOfGames)
	plt.show()
