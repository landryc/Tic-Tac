#################################
#				 #
#  AUTHOR 	: NOULAWE LANDRY #	
#  LICENSE 	: LGPL		 #
#				 #
#################################

# human Vs human
TAILLE = 3
ITEMS = '.◉◎'

# importation de librairies

import numpy as np 
import os
import random

class Player:
	""" This class represent the players in the game """
	def __init__(self, id_player, name=None): # Le joueur peut avoir un nom s'il ne s'agit pas d'un joueur machine sinon c'est IA
		self.name = name or 'IA'
		self.id_player = id_player


class Tictac3:
	""" This class represent the game tic-tac 3 """
	def __init__(self):
		name1, name2 = self.setting()
		self.board = np.zeros((TAILLE,TAILLE), dtype=np.int8)
		self.players = [Player(1,name1), Player(2,name2)]
		self.cur_player = random.randrange(2)


	def swap_player(self): # permit to change the current player
		self.cur_player = (self.cur_player + 1) % 2

	def setting(self):
			""" Configure the game """
			name1 = input('entrez votre nom: ')
			name2 = input('entrez votre nom: ')
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

	def put(self, x,y, id_player):
		""" to play in position x,y """
		self.board[x,y] = id_player

	def play(self, player,case=None): 

		def choice_case():
			# Minmax algorithm 
			return x,y

		def isvalid(case):
			x,y = case
			if 0 <= x < TAILLE and 0 <= y < TAILLE and self.board[x,y] == 0:
				return True

		if player.name == 'IA':
			case = choice_case()
		elif not isvalid(case):
			return False
		self.put(*case, player.id_player)
		return True


	def has_won(self, player):
		""" Determine if the player who has id_player won """
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

			print("\n\n Bienvenue dans le jeu tic-tac 3")
			winner = False
			print(self)
			for i in range(TAILLE * TAILLE):
				test = False
				while not test:
					response = input(f'A vous de jouer {self.players[self.cur_player].name}. Ex: 1,1: ')
					case = parser(response)
					test = self.play(self.players[self.cur_player], case)
				os.system('clear')
				print(self)
				if i > 4:
					if self.has_won(self.players[self.cur_player]):
						winner = True
						print(f'le gagnant est {self.players[self.cur_player].name}')
						break
				self.swap_player()
			if not winner:
				print('Match nul !!!')

if __name__ == '__main__':
	Tictac3().party()
