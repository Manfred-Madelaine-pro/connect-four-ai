
import p4 as game
import player as pl

NB_STEP = 2
population = 10



# --------------------------------------
#               AI ML
# --------------------------------------

class AI_ml(pl.AI_plus):

	def __init__(self, name, piece):
		pl.AI_plus.__init__(self, name, piece)
		
		self.ais = []
		self.init()

	def init(self):
		# create all the AIs
		for _ in range(population):
			self.ais.append(pl.AI_plus(self.name, self.piece))

	def play(self):
		pass

# --------------------------------------
#               ML opponent
# --------------------------------------

class opponent(pl.AI_plus):

	def __init__(self, name, piece):
		pl.AI_plus.__init__(self, name, piece)

		self.history = []




def play():
	player_a = AI_ml('MFD', 'O')
	player_b = opponent('INS', 'X')
	
	end_of_game = False
	game_history = []

	while(not end_of_game):
		end_of_game = game.round(player_a, player_b, game_history)
