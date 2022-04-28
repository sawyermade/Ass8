import random

# Player parent class
class Player:
	def __init__(self, name):
		self.name = name 
		self.w    = 0
		self.l    = 0
		self.val  = ''
		self.rps_dict = {
			'r' : 'rock',
			'p' : 'paper',
			's' : 'scissors'
		}

	def __str__(self):
		return f'{self.name}: {self.rps_dict[self.val]}'

# Bart, Player child class
class Bart(Player):
	def __init__(self):
		super().__init__('Bart')

	def generateRoshambo(self):
		self.val = 'r'

# Lisa, Player child class
class Lisa(Player):
	def __init__(self):
		super().__init__('Lisa')

	def generateRoshambo(self):
		self.val = random.choice(['r', 'p', 's'])

# Play function and summary logic
def play(player, opponent, game_count):
	# Win/Draw flags
	win_flag, draw_flag = True, False

	# Check for draw
	if player.val == opponent.val:
		draw_flag = True

	# If player has rock and opponent not scissors
	elif player.val == 'r':
		if opponent.val != 's':
			win_flag = False

	# If player has paper and opponent not rock
	elif player.val == 'p':
		if opponent.val != 'r':
			win_flag = False

	# If player has scissors and opponent not paper
	else:
		if opponent.val != 'p':
			win_flag = False

	# Print summary and update wins/losses
	if draw_flag:
		print('---> Draw!')

	elif win_flag:
		print(f'---> {player.name} wins!')
		player.w += 1
		opponent.l += 1

	else:
		print(f'---> {opponent.name} wins!')
		player.l += 1
		opponent.w += 1

	print(
		f'{player.name} total wins: {player.w}/{game_count}, total lose: {player.l}/{game_count}\n'
		f'{opponent.name} total wins: {opponent.w}/{game_count}, total lose: {opponent.l}/{game_count}'
	)

# Main function
def main():
	# Title
	print('Roshambo Game\n')

	# Get name
	player_name = input('Enter your name: ').strip()
	print()

	# Hints
	print(
		'Hint 1: Bart\'s Roshambo is always rock.\n'
		'Hint 2: Lisa\'s Roshambo is selected by random.\n'
	)

	# Select opponent
	opponent_name = input('Would you like to play against Bart or Lisa? (b/B or l/L): ').strip().lower()
	print()

	# Create player/opponent objects
	player = Player(player_name)
	if opponent_name == 'b': 
		opponent = Bart()
	else: 
		opponent = Lisa()

	# Game count
	game_count = 0

	# Loop for playing game and continuing/quitting
	cont_flag = True
	while cont_flag:
		# Get player rps value
		val = input('Rock, paper, or scissors? (r/p/s): ').strip().lower()
		print()

		# Check if rps value is valid and play, else try again
		if val in ['r', 'p', 's']:
			# Since valid, increase game count
			game_count += 1

			# Set player value, opponent value, print values, and play
			player.val = val
			opponent.generateRoshambo()
			print(player)
			print(opponent)
			play(player, opponent, game_count)
			print()

			# Ask to play again/continue
			cont = input('Play again? (y/n): ').strip().lower()
			print()

			# User wants to quit
			if cont != 'y':
				print('Thanks for playing!')
				cont_flag = False

		# Invalid rps choice, try again
		else:
			print('Invalid choice. Try again.\n')

# If running file directly, run main function
if __name__ == '__main__':
	main()