#!/usr/bin/env python
# coding: utf-8


BOARD = []
BOARD_SIZE = 8
MAX_PLAYER = 2
MIN_ALINED_PIECES = 4
ROUND, ID_PLAYER = 0, 0


def get_available_col():
	available_col = []
	for i, col in enumerate(BOARD[0]):
		if not col:
			available_col.append(i)

	return available_col


def set_board():
	global BOARD, ROUND, ID_PLAYER
	ROUND, ID_PLAYER = 0, 0
	BOARD = [[None for i in range(BOARD_SIZE)]for i in range(BOARD_SIZE)]


# Check End Of Game
def check_eog(col):
	end = verif_last_piece(col)
	no_col_available = ([] == get_available_col())
	return end or no_col_available


def move_piece(piece, col):
	have_played = True 
	update_round()
	for row in reversed(BOARD):
		if (not row[col]):
			row[col] = piece
			return have_played
	return not have_played


def update_round():
	global ROUND, ID_PLAYER
	ID_PLAYER += 1
	if ID_PLAYER == MAX_PLAYER:
		ROUND += 1
		ID_PLAYER = 0


# Control from the last piece played
def verif_last_piece(col):
	row = get_row_from(col)
	max_count = []

	# Right or Left control for the end of game
	diago_end_r = diago_control(row, col, max_count)
	diago_end_l = diago_control(row, col, max_count, top_right=False )
	diago_end = diago_end_r or diago_end_l

	# Vertical or Horizontal control for the end of game
	ortho_end_v = ortho_control(row, col, max_count)
	ortho_end_h = ortho_control(row, col, max_count, vertical_verif=False)
	ortho_end = ortho_end_v or ortho_end_h

	end_of_game = (ortho_end or diago_end)

	# TODO cas particulier ou aligné horizontalement & verticalement
	if end_of_game:
		print_end(row, col, ortho_end_v, ortho_end_h, diago_end, max_count)

	return end_of_game


# Orthogonal control : Vertical and Horizontal
def ortho_control(row, col, max_count, vertical_verif=True):
	piece = BOARD[row][col]
	l_count = [0]

	for i in range(BOARD_SIZE):
		if (vertical_verif):
			check(piece, i, col, l_count)
		else:
			check(piece, row, i, l_count)

	return count_manager(l_count, max_count)


def diago_control(row, col, max_count, top_right=True):
	piece = BOARD[row][col]

	diago_r, diago_c = get_top_diago(row, col, top_right)	
	
	# Top Diago
	td_row = row + diago_r
	td_col = col + diago_c

	end_diago = verif_diago(td_row, td_col, piece, max_count, top_right)
	return end_diago


# Return the position of the top case on the right or left digonal
def get_top_diago(row, col, top_right):
	i, j = 0, 0
	i_delta = -1 
	j_delta = 1 if top_right else -1

	while(not out_of_border(row + i + i_delta, col + j + j_delta)):
		i, j = i + i_delta, j + j_delta

	return i, j


def verif_diago(row, col, piece, max_count, top_right):
	i, j, l_count = 0, 0, [0]
	i_delta = 1 
	j_delta = -1 if top_right else 1

	while(not out_of_border(row + i + i_delta, col + j + j_delta)):
		i, j = i + i_delta, j + j_delta
		check(piece, row + i, col + j, l_count)

	return count_manager(l_count, max_count)


# to rename
def count_manager(l_count, max_count):
	if(max(l_count) >= MIN_ALINED_PIECES):
		max_count.append(max(l_count))

	return max(l_count) >= MIN_ALINED_PIECES


def out_of_border(row, col):
	return (row >= BOARD_SIZE or row < 0) or (col >= BOARD_SIZE or col < 0)


def check(piece, i, j, l_count):
	if BOARD[i][j] == piece:
		l_count[-1] += 1
	else:
		l_count.append(0)


def get_row_from(column):
	for i in range(BOARD_SIZE):
		if (BOARD[i][column] != None):
			return i
	return None



def print_end(row, col, vertical, horizontal, diagonal, max_count):
	# TODO improve to show multiple end case simultaneously
	end = 'verticaly' if vertical else (
		'horizontaly' if horizontal else (
			'diagonaly'))
	print('\n\t Puissance {0} {1} at ({2};{3}) !'.format(max_count[0], end, col, row))



def is_filled(col):
	return BOARD[0][col]


def get_round():
	return ROUND

def get_row_height(row):
	return BOARD_SIZE-row


def print_board():
	# os.system('cls' if os.name == 'nt' else 'clear')
	print('round : ' + str(ROUND))
	draw_board()


def draw_board():
	border = '-----'
	tab, piece = '', ''
	line = '\n' + '   ' + border*BOARD_SIZE + '\n'

	for i, row in enumerate(BOARD):
		tab += line
		tab += ' ' + str(BOARD_SIZE-i-1) + ' '
		for case in row:
			piece = case if case else ' '

			tab += '| ' + piece + ' |'

	tab += line + '   '

	# Indices
	for i in range (BOARD_SIZE):
		tab += '  ' + str(i) + '  '

	print(tab + '\n')
