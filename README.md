# QLearning
## My implementation of Q-Learning, SARSA and SARSA-λ on a grid-world test-bed

1. Requirements : pygame,gym,numpy,argparse,matplotlib
	
2. Usage:
	
	python2 grid.py [-h] [--alpha ALPHA] [--epsilon EPSILON] [--gamma GAMMA]
               [--episodes EPISODES] [--verbose] [--grid GRID] [--render]
               [--show-policy] [--algo ALGO] --games GAMES [--lam LAM]

	ALPHA : learning rate [Default:0.5]
	EPSILON : Epsilon value for epsilon-greedy exploration [Default:0.1]
	GAMMA : Discount [Default:0.9]
	GAMES : number of games [Default:1]
	--render : to render the game for last 10% of the episodes
	--show-policy : to show policy at the end 
	GRID : A/B/C
	ALGO : Q/SARSA/SARSAlam
	LAM : lambda value for SARSAlam [Default:0.5]

	
3. Example: To run a game with default settings on grid-A, to render the enviroment and show learnt policy at the end
	
	python grid.py --episodes 1000 --render --show-policy
	

4. Reference : [Reinforcement Learning: An Introduction Book by Andrew Barto and Richard S. Sutton](http://incompleteideas.net/book/bookdraft2018mar21.pdf)	
