#################################
#								#								
#  AUTHOR 	: NOULAWE LANDRY	#	
#  LICENSE 	: LGPL				#				
#								#
#################################

# human Vs human
TAILLE = 3
ITEMS = '.◉◎'

# importation de librairies

import numpy as np 
import os
import random
import time

class Player:
	""" This class represent the players in the game """
	def __init__(self, id_player, name=None): # Le joueur peut avoir un nom s'il ne s'agit pas d'un joueur machine sinon c'est IA
		self.name = name or 'AI'
		self.id_player = id_player


class Tictac3:
	""" This class represent the game tic-tac 3 """
	def __init__(self):
		name1, name2 = self.setting()
		self.board = np.zeros((TAILLE,TAILLE), dtype=np.int8)
		self.players = [Player(1,name1), Player(2,name2)]
		self.cur_player = np.random.randint(2)
		self.winner = False


	def switch_player(self): 
		""" permit to change the current player """
		self.cur_player = (self.cur_player + 1) % 2

	def setting(self):
			""" Configure the game """
			name1 = input(f'enter your name player 1 ({ITEMS[1]}): ')
			name2 = input(f'enter your name player 2 ({ITEMS[2]}): ')
			return name1, name2

	def __str__(self):
		""" print the board on screen """
		sep = '\t'
		margin = ' '
		display = margin
		for x in range(TAILLE):
			for y in range(TAILLE):
				display += ITEMS[self.board[x,y]] + sep
			display += '\n\n' + margin
		return display

	def play(self, player, case=None): 
		""" to play one stroke"""

		def isvalid(case):
			x,y = case
			if 0 <= x < TAILLE and 0 <= y < TAILLE and self.board[x,y] == 0:
				return True
			return False

		def put(x,y, id_player):
			# to play in position x,y 
			self.board[x,y] = id_player
			if self.has_won(self.players[id_player - 1]):
				self.winner = True
			self.switch_player()                  # switch player

		def annulate(x,y):
			# to annulate a stroke
			self.board[x,y] = 0
			self.winner = False
			self.switch_player()                  # switch player

		def possibility():
			# generate all possible strokes
			for x in range(TAILLE):
				for y in range(TAILLE):
					if isvalid((x,y)):
						yield x,y

		def save_context():                   # Permit to save the context of game before algo minimax.
			#print('save context')
			table = np.copy(self.board)
			cur = self.cur_player
			win = self.winner
			return table, cur, win

		def restore_context(table, cur, win): # permit to restore context of game after algo minimax.
			#print('restore context')
			self.board = table
			self.cur_player = cur
			self.winner = win

		def evaluate():
			# evaluate the situation of game
			#print('evaluation')
			index_adv = 2 - player.id_player          # calculate the indice of opponent(adversaire)
			if not len(list(possibility())) and not self.winner:
				return 0
			elif self.has_won(player):
				return 1
			elif self.has_won(self.players[index_adv]):
				return -1

		def minimax(best_stroke):
			# Minimax algorithm
			#print("In minimax")
			if len(list(possibility())) == 9:
				return (1,1) , 0
			if self.winner or len(list(possibility())) == 0:
				return best_stroke, evaluate()
			if self.cur_player == player.id_player - 1: # if is the AI which play: NODE MAX
				#print('max')
				best_score = -1
				for case in possibility():
					put(*case, player.id_player)
					best_stroke, score = minimax(best_stroke)
					annulate(*case)
					if score > best_score:
						best_score = score
						best_stroke = case
			else:										# if is the opponent of AI: NODE MIN
				#print('min')
				best_score = 1
				for case in possibility():
					put(*case, self.players[self.cur_player].id_player)
					best_stroke, score = minimax(best_stroke)
					annulate(*case)
					if score < best_score:
						best_score = score
						best_stroke = case

			return best_stroke, best_score




		def choice_case_minimax():
			# execute minimax algorithm 
			table, cur, win = save_context()
			best_stroke = list(possibility())[0] # first possibility is the best_stroke on begining
			best_stroke,_ = minimax(best_stroke)
			restore_context(table,cur,win)
			return best_stroke

		
		if player.name == 'AI':
			case = choice_case_minimax()
		elif not isvalid(case):
			return False
		ex_player = player.id_player - 1      # player who has play
		put(*case, player.id_player)
		return True, ex_player                # ex_player: player's position who has play in the list of players


	def has_won(self, player):
		""" Determine if player won """
		def motifs():
			""" generate the motifs on screen """

			# for lines 
			for x in range(TAILLE):
				m = ''
				for y in range(TAILLE):
					m += str(self.board[x,y])
				yield m

			# for columns
			for x in range(TAILLE):
				m = ''
				for y in range(TAILLE):
					m += str(self.board[y,x])
				yield m

			# first diagonal
			#yield ''.join (str(self.board[x,y]) for (x,y) in self.cases() if x == y)
			yield ''.join( [ str(self.board[0,0]), str(self.board[1,1]), str(self.board[2,2]) ] )

			# 2nd diagonal
			yield ''.join( [ str(self.board[2,0]), str(self.board[1,1]), str(self.board[0,2]) ] )

		motif = str(player.id_player)*3

		return motif in motifs()

	def party(self):
			""" manage the party """
			def parser(chaine):
				""" parse the entry of human player """
				return [int(elt) for elt in chaine.replace(',',' ').replace(';',' ').split()]

			print("\n\n Welcome to the game tic-tac 3")
			print(self)
			for i in range(TAILLE * TAILLE):
				test = False
				while not test:
					if self.players[self.cur_player].name is not 'AI':
						response = input(f'Play {self.players[self.cur_player].name}. Ex: 1,1: ')
						case = parser(response)
					else:
						print(f'Play {self.players[self.cur_player].name}. Ex: 1,1: ')
						case = 1,1
					test, ex_player = self.play(self.players[self.cur_player], case)       # play and switch player
				os.system('clear')
				print(self)
				time.sleep(2)
				if i > TAILLE:
					if self.winner:  
						print(f'The winner is: {self.players[ex_player].id_player}: {self.players[ex_player].name} ({ITEMS[2 - self.cur_player]})')
						break
			if not self.winner:
				print('Match nul !!!')


if __name__ == '__main__':
	Tictac3().party()