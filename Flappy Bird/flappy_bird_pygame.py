# Flappy Bird

import pygame
import sys
import time
from random import seed
from random import randint

pygame.init()

seed(1)

FPS = 40
CLOCK = pygame.time.Clock() 
HEIGHT = 750
WIDTH = 500

FONT = pygame.font.Font('freesansbold.ttf', 32)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running_game = True
running_start_screen = True
running_end_screen = False

score = 0

#coordinate of the bird
bird_x = 50
bird_y = 300
bird_y_change = 0

#coordinate of the pipes
pipe_x = 500
pipe_x_change = 0
top_pipe_y = 0
btm_pipe_y = 380 #x+150(space)

#width and height of the pipes
pipe_width = 100 
t_pipe_height = 230
b_pipe_height = 230


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# LOAD IMAGES
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (64, 64))

def start_screen():
	start_text = FONT.render("PRESS SPACE BAR TO START", True, WHITE)
	screen.blit(start_text, (20, 200))
	pygame.display.update()

# Create different pipes 
def unique_pipe():
	global t_pipe_height, b_pipe_height, btm_pipe_y, pipe_x, score
	pipe_x = 500
	t_pipe_height = randint(20, 440)
	b_pipe_height = 460 - t_pipe_height
	btm_pipe_y = t_pipe_height + 150
	score += 1

# Check if bird hits to the pipes
def check_collision():
	global running_end_screen
	if pipe_x <= 94:
		if bird_y < btm_pipe_y - 150 or bird_y >= btm_pipe_y:
			running_end_screen = True

def show_score():
	score_text = FONT.render("Score: {score}".format(score = score), True, WHITE)
	screen.blit(score_text, (5, 5))
	pygame.display.update()

def end_screen():
	end_text1 = FONT.render("GAME OVER", True, RED)
	screen.blit(end_text1, (150, 170))
	end_text2 = FONT.render("Final Score: {score}".format(score = score), True, WHITE)
	screen.blit(end_text2, (150, 330))
	end_text3 = FONT.render("PRESS SPACE BAR TO RESET", True, WHITE)
	screen.blit(end_text3, (20, 480))

	pygame.display.update()

# Reset the game
def reset():
	global running_end_screen, bird_y, score, bird_y_change, pipe_x
	running_end_screen = False
	score = 0
	bird_y = 300
	bird_y_change = 0
	pipe_x = 500
	pygame.display.update()


while running_game:
	screen.fill(BLACK)
	screen.blit(background, (0, 0))

	while running_start_screen: # Start Screen of the game
		screen.blit(bird_img, (bird_x, bird_y))
		start_screen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					running_start_screen = False

	while running_end_screen: # It runs when the bird collapsed
		end_screen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					reset()

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_y_change = -10

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				bird_y_change = 7

		if pipe_x == 500:
			pipe_x_change = -10

		elif pipe_x == 0:
			pipe_x = 500

	screen.blit(bird_img, (bird_x, bird_y))

	if bird_y >= 570:
		bird_y = 570
	elif bird_y <= 0:
		bird_y = 0

	bird_y += bird_y_change
	pipe_x += pipe_x_change
	if pipe_x <= 0:
		unique_pipe()

	# Draw top pipe
	pygame.draw.rect(screen, GREEN, (pipe_x, top_pipe_y, pipe_width, t_pipe_height))
	# Draw bottom pipe
	pygame.draw.rect(screen, GREEN, (pipe_x, btm_pipe_y, pipe_width, b_pipe_height))

	check_collision()
	show_score()
	pygame.display.update()
	CLOCK.tick(FPS)





