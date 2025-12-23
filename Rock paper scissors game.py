import random

options = ('ROCK', 'PAPER', 'SCISSORS')
score = 0
game_state = 0
quit = False

print('Welcome to THE ULTIMATE ROCK PAPER SCISSORS GAME' + '\n')

# Each round, the script randomly selects either rock, paper or scissors. The player can choose 
# their option.

while game_state < 3:
	print(f'-------------------- ROUND {game_state + 1} ---------------------' + '\n')
	hand_computer = random.choice(options)
	hand_player = input('Please enter your move (rock/paper/scissors; q to quit): ').upper()

# 'Q/q' exits the game:

	if hand_player == 'Q':
		quit = True
		break

# 3 states are defined: round won (+1 point score), round lost and tie. 3 rounds without a tie 
# must be played until the game ends. 

	elif (hand_computer == 'ROCK' and hand_player == 'PAPER') or (hand_computer == 'PAPER' and hand_player == 'SCISSORS') or (hand_computer == 'SCISSORS' and hand_player == 'ROCK'):
		print(f'Player picked: {hand_player}' + '\n' + f'Computer picked: {hand_computer}')
		print(f'You win this round! {hand_player} beats {hand_computer}' + '\n')
		score += 1
		game_state += 1
	
	elif (hand_computer == 'ROCK' and hand_player == 'SCISSORS') or (hand_computer == 'PAPER' and hand_player == 'ROCK') or (hand_computer == 'SCISSORS' and hand_player == 'PAPER'):
		print(f'Player picked: {hand_player}' + '\n' + f'Computer picked: {hand_computer}')
		print(f'You lose this round! {hand_computer} beats {hand_player}' + '\n')
		game_state += 1

	elif hand_computer == hand_player:
		print(f'Player picked: {hand_player}' + '\n' + f'Computer picked: {hand_computer}')
		print('It\'s a tie! Let\'s try again!' + '\n')

# If the player selects an invalid option, the code in the While loop reruns and the round 
# repeats.

	else:
		print('Invalid input! Try again' + '\n')

# If the player didn't quit earlier, the game will print their final score and the score of 
# their adversary, and also a won/lost message will be displayed depending on the player's score.

if not quit:
	print('--------------------------------------------------')
	print('\n' + f'You final score is {score}. Your adversary scored {3 - score}')

	if score > 1:
		print('You won the game!')
	else:
		print('You lost the game!')