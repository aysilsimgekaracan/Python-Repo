import pygame
import sys
import time 
from pygame.locals import *

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 30
CLOCK = pygame.time.Clock() 
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
GAP = 20
BOX_SIZE = 120

game = True
x_or_o = 'x'
count = 0
col = 0
row = 0
board = {
	1 :	None,
	2 : None,
	3 : None,
	4 : None,
	5 : None,
	6 : None,
	7 : None,
	8 : None,
	9 : None
}

# X AND O PICTURES
x_img = pygame.image.load('x.png')
y_img = pygame.image.load('o.png')

x_img = pygame.transform.scale(x_img, (80, 80))
y_img = pygame.transform.scale(y_img, (80, 80))

	# SURFACE
surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
surf.fill(WHITE)

def game_initiating_window():

	# LINES
	pygame.draw.line(surf, BLACK, (GAP + BOX_SIZE, GAP),
	                 (GAP + BOX_SIZE, WINDOW_HEIGHT - GAP), width=3)
	pygame.draw.line(surf, BLACK, (WINDOW_WIDTH - BOX_SIZE, GAP),
	                 (WINDOW_WIDTH - BOX_SIZE, WINDOW_HEIGHT - GAP), width=3)
	pygame.draw.line(surf, BLACK, (GAP, GAP + BOX_SIZE),
	                 (WINDOW_WIDTH - GAP, GAP + BOX_SIZE), width=3)
	pygame.draw.line(surf, BLACK, (GAP, WINDOW_HEIGHT - (GAP + BOX_SIZE)),
	                 (WINDOW_WIDTH - GAP, WINDOW_HEIGHT - (GAP + BOX_SIZE)), width=3)


def board_pos():
	if row == col == 1:
		position = 1
	elif row == 1 and col == 2:
		position = 2
	elif row == 1 and col == 3:
		position = 3
	elif row == 2 and col == 1:
		position = 4
	elif row == col == 2:
		position = 5
	elif row == 2 and col == 3:
		position = 6
	elif row == 3 and col == 1:
		position = 7
	elif row == 3 and col == 2:
		position = 8
	elif row == 3 and col == 3:
		position = 9
	else:
		position = 0

	return position


def click_coordinates(x, y):
	global row
	global col

	if x > GAP and x < (GAP + BOX_SIZE):
		row = 1
	elif x > GAP + BOX_SIZE and x < GAP + (2 * BOX_SIZE):
		row = 2
	elif x > GAP + (2 * BOX_SIZE) and x < GAP + (3 * BOX_SIZE):
		row = 3
	else:
		row = 0

	if (y > GAP) and (y < (GAP + BOX_SIZE)):
		col = 1
	elif y > GAP + BOX_SIZE and y < GAP + (2 * BOX_SIZE):
		col = 2
	elif y > GAP + (2 * BOX_SIZE) and y < GAP + (3 * BOX_SIZE):
		col = 3
	else:
		col = 0

	drawXO()

# Draw pictures into the board

def drawXO():
	global x_or_o
	global board
	global count

	pos = board_pos()

	if row == 1:
		posx = 40
	elif row == 2:
		posx = 170
	elif row == 3:
		posx = 300

	if col == 1:
		posy = 40
	elif col == 2:
		posy = 160
	elif col == 3:
		posy = 280

	if row != 0 and col != 0 and board.get(pos) == None:
		if x_or_o == 'x':
			surf.blit(x_img, (posx, posy))
			board[pos] = x_or_o
			x_or_o = 'o'
			count += 1
		elif x_or_o == 'o':
			surf.blit(y_img, (posx, posy))
			board[pos] = x_or_o
			x_or_o = 'x'
			count += 1


# Give message of the winner
def message(message, size):
	font = pygame.font.Font('freesansbold.ttf', size)
	text = font.render(message, True, RED, WHITE)
	text_rect = text.get_rect()
	text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
	surf.blit(text, text_rect) 
	pygame.display.update()
	time.sleep(3)
	surf.fill(WHITE)

# Check the winner
def winner():
	global board
	global game

	# 1, 2, 3
	# 4, 5, 6
	# 7, 8, 9

	# 1, 4, 7
	# 2, 5, 8
	# 3, 6, 9

	# 1, 5, 9
	# 3, 5, 7


	if (board[1] == board[2] == board[3] == 'x') or (board[4] == board[5] == board[6] == 'x') or (board[7] == board[8] == board[9] == 'x') or (board[1] == board[4] == board[7] == 'x') or (board[2] == board[5] == board[8] == 'x') or (board[3] == board[6] == board[9] == 'x') or (board[1] == board[5] == board[9] == 'x') or (board[3] == board[5] == board[7] == 'x'):
		msg = "Winner is X"
		message(msg, 52)
		game = False

	elif (board[1] == board[2] == board[3] == 'o') or (board[4] == board[5] == board[6] == 'o') or (board[7] == board[8] == board[9] == 'o') or (board[1] == board[4] == board[7] == 'o') or (board[2] == board[5] == board[8] == 'o') or (board[3] == board[6] == board[9] == 'o') or (board[1] == board[5] == board[9] == 'o') or (board[3] == board[5] == board[7] == 'o'):

		msg = "Winner is O"
		message(msg, 52)
		game = False

	elif count == 9:
		msg = "Game Draw"
		message(msg, 52)
		game = False

# Restart the game
def restart():
	global board, x_or_o, count, col, row, game

	message("Game is restarting...", 28)

	surf.fill(WHITE)

	game = True
	x_or_o = 'x'
	count = 0
	col = 0
	row = 0
	board = {
		1 :	None,
		2 : None,
		3 : None,
		4 : None,
		5 : None,
		6 : None,
		7 : None,
		8 : None,
		9 : None
	}

	game_initiating_window()



game_initiating_window()
# Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			click_coordinates(x, y)
			winner()

			if game == False:
				restart()

	pygame.display.update()
	CLOCK.tick(FPS)



