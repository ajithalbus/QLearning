#!/usr/local/bin/python
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import pygame

WIND = True

def moveVector(action):
	if action==0:
		vector=[0,-1]
	elif action==1:
		vector=[-1,0]
	elif action==2:
		vector=[0,1]
	elif action==3:
		vector=[1,0]
		
	return vector

class GridEnvB(gym.Env):
	metadata = {'render.modes': ['human']}
	def _makeEnv(self,goal,goalReward=10):
		'''Creates a numpy array as the reward environment'''
		rews=np.loadtxt('./gym_grid/envs/map',dtype=np.int)*-1
		rews[goal]=goalReward
		return rews

	def _take_action(self,action):
		
		if WIND:
			self.position[1] += np.random.binomial(1,0.5) #wind
		if	np.random.choice([0,1],p=[0.9,0.1]): # p=0.1 take random move 
			possibleActions=[0,1,2,3]
			possibleActions.remove(action)
			action=np.random.choice(possibleActions)
		self.position += moveVector(action) #for taking action
		self.position = np.clip(self.position,0,11) # to avoid out of bounds
		
	

		

	def __init__(self):
		self.goal=(2,9)
		self.rews=self._makeEnv(goal=self.goal)
		self.observation_space=spaces.Tuple((spaces.Discrete(12),spaces.Discrete(12)))
		self.action_space=spaces.Discrete(4)
		
		

		
	def step(self, action):
		self._take_action(action)
		reward = self.rews[self.position[0],self.position[1]]
		ob = np.copy(self.position)
		done = np.array_equal(self.position,list(self.goal)) 
		return ob,reward,done,{}
	
	def reset(self,Gui=False):
		startState=np.random.choice([5,6,10,11])
		self.position=np.array([startState,0])
		self.rews=self._makeEnv(self.goal)
		
		if Gui:
			pygame.init()
			
			WINDOW_SIZE = [305, 305]
			self.screen = pygame.display.set_mode(WINDOW_SIZE)
			
			pygame.display.set_caption("Grid")
			
			
			self.clock = pygame.time.Clock()
			

		return np.copy(self.position)
		
	def render(self, mode='human', close=False):
		BLACK = (0, 0, 0)
		WHITE = (255, 255, 255)
		GREEN = (0, 255, 0)
		RED1 = (160, 69, 46)
		RED2 = (183, 52, 20)
		RED3 = (255, 50, 0)
		
		WIDTH = 20
		HEIGHT = 20
		
		MARGIN = 5
		
		grid = self.rews
		
		done = False
		
		# Set the screen background
		self.screen.fill(BLACK)
		# Draw the grid
		for row in range(12):
			for column in range(12):
				color = WHITE
				if grid[row][column] == -1:
					color = RED1
				elif grid[row,column] == -2:
					color = RED2
				elif grid[row,column] == -3:
					color = RED3
				elif grid[row,column] > 0:
					#print row,column
					color = GREEN
				pygame.draw.rect(self.screen,
								color,
								[(MARGIN + WIDTH) * column + MARGIN,
								(MARGIN + HEIGHT) * row + MARGIN,
								WIDTH,
								HEIGHT])
		pygame.draw.circle(self.screen,BLACK,[(MARGIN + WIDTH) * self.position[1] + 3*MARGIN,
                              (MARGIN + HEIGHT) * self.position[0] + 3*MARGIN],5)
	
		self.clock.tick(60)
	
		pygame.display.flip()
	
		

		
