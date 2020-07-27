#!/usr/bin/env python
# coding: utf-8

import os

import ml
import player
import board as b

# TODO: bonus pour chaque pieces alignées en plus 

replay_list = [0, 0, 2, 5, 7, 1, 2, 3, 1, 2, 7, 1, 6, 0, 0, 0, 2, 4, 3, 6, 3, 2, 5, 5, 5, 6, 7, 4, 3, 7, 0, 1, 0, 2, 0, 1, 4]


IN_REPLAY_MODE = False
TOUR_BY_TOUR = True

LAST_PLAY = None
NB_TEST = 1
ML_MODE = False


# --------------------------------------
#               Methods
# --------------------------------------


def test():
	list_round = []

	for _ in range(NB_TEST):
		start()
		list_round.append(b.get_round())
		# input()

	avg = sum(list_round)/len(list_round)
	print('\n\tTotal of round : ' + str(list_round))
	print('\taverage of round per game : ' + str(avg))


def start():
	b.set_board()
	
	if(ML_MODE):
		ml.play()
	else:
		play()


def play():
	player_a = player.AI_plus('AI-o', 'O')
	player_b = player.AI('AI-x', 'X')
	
	end_of_game = False
	game_history = []

	while(not end_of_game):
		end_of_game = round(player_a, player_b, game_history)


	# b.print_board()
	# print('history :\n\t' + str(game_history))


def round(player_a, player_b, game_history):
	end_of_game = make_a_move(player_a, game_history)
	if(not end_of_game):
		end_of_game = make_a_move(player_b, game_history)

	return end_of_game


def make_a_move(player, game_history):
	have_played = False
	# last_play = -1 if (len(game_history) == 0) else game_history[-1]
		
	while (have_played == False):
		if (IN_REPLAY_MODE):
			col = replay_list.pop(0) 
		else:
			col = player.play()

		have_played = b.move_piece(player.piece, col)
	
	player.last_move = col
	# print(player.name, player.last_move)
	game_history.append(col)

	eog = b.check_eog(col)
	if(TOUR_BY_TOUR):
		clear()
		b.print_board()
		input()
	return eog


clear = lambda: os.system('cls')

# --------------------------------------
#               Main
# --------------------------------------

if __name__ == '__main__':
	# test()
	start()
