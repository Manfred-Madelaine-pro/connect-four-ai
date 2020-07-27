#!/usr/bin/env python
# coding: utf-8

import random
import board as b



# --------------------------------------
#               Human Player
# --------------------------------------

class Player:
	def __init__(self, name, piece):
		self.name = name
		self.piece = piece
		self.last_move = None

	def play(self, *argv):
		column = -1
		is_ok = False
		choices = b.get_available_col()

		while (not is_ok):
			try:
				column = int(input(self.name + ' (' + self.piece + ') > choose a column : '))

			except NameError:
				pass
			except SyntaxError:
				pass
			except ValueError:
				pass
			
			is_ok = not input_control(column, choices)

		return column


# --------------------------------------
#               Random AI
# --------------------------------------

class AI(Player):
	def __init__(self, name, piece):
		Player.__init__(self, name, piece)

	def play(self, *argv):
		choices = b.get_available_col()
		column = random.choice(choices)
		return column


# --------------------------------------
#               AI Attacking
# --------------------------------------

class AI_plus(AI):
	def __init__(self, name, piece):
		AI.__init__(self, name, piece)

	
	def attack(self):
		# if I can win, play it
		col = control_col(self.piece, self.last_move)
		if (col):
			print ('win', col)
			return col

		return []

	def defense(self):
		# if opponent can win, block him
		return []

	def play(self, *argv):
		defense_choices = self.defense()
		attack_choices = self.attack()
		choice = -1

		if (defense_choices):
			choice = defense_choices[0]
		elif(attack_choices):
			choice = attack_choices[0]
		else:
			print('random')
			choice = AI.play(self)
			# random
			# play

		# si jouer ne permet pas à ladversaire de gagner 
		# dans les 2 tours qui suivent, le mouve est safe
		# simuler des parties
		'''
		random
		att def random
		simulé 2 tours
		s 'il y a une faibesse, retirer la colonne comme choix possible'
		'''
		return choice


# ia : alpha beta; min max



def input_control(column, choices):	
	is_filled = column not in choices
	wrong_input = (column < 0) or (column >= b.BOARD_SIZE)

	if (wrong_input):
		print('wrong input, please try again.')
	elif (is_filled):
		print('this column is already filled..')

	return is_filled or wrong_input

	
def control_col(piece, column):
	res = {}

	if(column == None):
		return res

	row = b.get_row_from(column)
	res['verti'] = vertical_control(row, column, piece)
	res['hori'] = horizontal_control(row, column, piece)
	res ['diago'] = diagonal_control(row, column, piece)

	print(res)
	if res['verti'] != []:
		return res['verti']
	else:
		return res['hori']


def diagonal_control(row, column, piece):
	# diago 1
	# sens haut
	# sens bas

	# diago 2
	# sens bast
	# sens bas
	return []

def horizontal_control(row, column, piece):
	col = column
	count_l, count_r = 0, 0
	min_piece = b.MIN_ALINED_PIECES
	no_left, no_right = False, False
	move = []

	for i in range(1, min_piece):
		# left
		count_l, no_left = control_dir(piece, row, col, -i, no_left, count_l, move)
		# right
		count_r, no_right = control_dir(piece, row, col, i, no_right, count_r, move)

		if(no_left and no_right):
			break

	print('\tout', count_l, count_r)
	return move if (count_r+count_l >= min_piece-1) else []


def control_dir(piece, row, col, delta, stop, counter, move):
	i = 1 if delta > 0 else -1
	if (not b.out_of_border(row, col+delta) and not stop
		and (b.BOARD[row][col+delta] == piece or b.BOARD[row][col+delta] == None)):
		if (b.BOARD[row][col+delta] == None):
			if (not b.out_of_border(row, col+delta-i) and b.BOARD[row][col+delta-i] == None):
				stop = True
			else:
				if(row+1 >= b.BOARD_SIZE or
				 (not b.out_of_border(row+1, col+delta-i) and b.BOARD[row+1][col+delta] != None)):
					move.append(col+delta)
		if (not stop):
			counter += 1
	else:
		stop = True
	return counter, stop


def vertical_control(row, col, piece):
	res = []
	count = 0
	min_piece = b.MIN_ALINED_PIECES-1
	row_height = b.get_row_height(row)
	print(col, row, row_height)
	# if the row is high enough but not too much
	if(row_height >= min_piece and row_height < b.BOARD_SIZE):
		for i in range (row, b.BOARD_SIZE):
			if(b.BOARD[i][col] == piece):
				count += 1
			else:
				break
			print(b.BOARD[i][col])

	if count >= min_piece:
		res.append(col)

	return res