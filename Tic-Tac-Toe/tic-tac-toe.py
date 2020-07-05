import sys #exit()

options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

board =	options[0] + "|" + options[1] + "|" + options[2] + "\n------\n" + options[3] + "|" + options[4] + "|" + options[5] + "\n------\n" + options[6] + "|" + options[7] + "|" + options[8] + "\n"

print(board)

players = {1: 'Player 1', 2: 'Player 2'}
queque = players.get(1)
count = 0

#main func
def game():
	global queque
	if  queque == players.get(1):
		x_or_o = 'x'
	else:
		x_or_o = 'o'

	option = int(input("{queque}! Choose where to put {x_o}: ".format(queque = queque, x_o = x_or_o)))
	
	if  queque == players.get(1):
		queque = players.get(2)
	else:
		queque = players.get(1)

	refresh_board(option, x_or_o)


#Check if the player wins
def winner(): 
	global options
	# 1, 2, 3
	# 4, 5, 6
	# 7, 8, 9

	# 1, 4, 7
	# 2, 5, 8
	# 3, 6, 9

	# 1, 5, 9
	# 3, 5, 7

	if (options[0] == options[1] == options[2] == 'x') or (options[3] == options[4] == options[5] == 'x') or (options[6] == options[7] == options[8] == 'x') or (options[0] == options[3] == options[6] == 'x') or (options[1] == options[4] == options[7] == 'x') or (options[2] == options[5] == options[8] == 'x') or (options[0] == options[4] == options[6] == 'x') or (options[2] == options[4] == options[6] == 'x'):

		print("Winner is {player}".format(player = players.get(1)))
		sys.exit()

	elif (options[0] == options[1] == options[2] == 'o') or (options[3] == options[4] == options[5] == 'o') or (options[6] == options[7] == options[8] == 'o') or (options[0] == options[3] == options[6] == 'o') or (options[1] == options[4] == options[7] == 'o') or (options[2] == options[5] == options[8] == 'o') or (options[0] == options[4] == options[6] == 'o') or (options[2] == options[4] == options[6] == 'o'):

		print("Winner is {player}".format(player = players.get(2)))
		sys.exit()
	elif count == 9:
		print("No Winner")
		sys.exit()
	

def refresh_board(option, x_or_o):
	global options
	global board
	global count
	if options[option-1] == 'x' or options[option-1] == 'o':
		print("\nIt is already taken. Lost your chance\n")
	else:
		options[option-1] = x_or_o
	board =	options[0] + "|" + options[1] + "|" + options[2] + "\n------\n" + options[3] + "|" + options[4] + "|" + options[5] + "\n------\n" + options[6] + "|" + options[7] + "|" + options[8] + "\n"
	print(board)
	count += 1
	winner()
	game()

game()

