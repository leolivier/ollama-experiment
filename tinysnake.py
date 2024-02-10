# Import the necessary libraries for the game
from random import randint, seed, random
from time import sleep
import pygame

# Define a function to create a new snake object and initialize its properties
def create_new_snakes():
	global head
	# Create an empty list to hold the snakes' head positions
	head = []
	
	# Initialize the snakes' body positions using randint numbers
	for I in range(3):
			head.append([randint(-50, 50), randint(-50, 50)])
					
	return [head]

# Define a function to update the game state every tick
def update_state():
	# Select a random head position and set its velocity based on the snakes' direction
	head_pos = head[0][0] + 1 if randint(0, 1) == 1 else head[0][0] - 1
		
	# Check whether the snakes crossed the edge of the screen
	if head_pos < 0 or head_pos >= len(head):
			# If it has crossed, remove its tail from the list and set its direction to None
			head.pop()[0][0] = randint(-50, 50)
			head[0][1] -= randint(1, 3)
	elif randint(0, 1):
			# If it's on the right side of the screen, set its direction to -1
			head_pos += 1
	else:
			# If it's on the left side of the screen, set its direction to +1
			head_pos -= 1
		
	# Draw the snakes based on their new positions
	for i in range(3):
			pygame.draw.line(surf, (255,0,0), (head[i][0], head[i][1]), (head[i][0]+20, head[i][1]+20))
			pygame.draw.rect(surf, (0,0,0), [head[i][0]-30, head[i][1]-30, 50, 50])
					
	# Update the clock's interval
	sleep(1)
     
# Main function that starts the game loop
def main():
	# Set up the window, surface, and clock
	global surf
	seed()
	surf = pygame.display.set_mode((600, 400))
	clock = pygame.time.Clock()
	
	# Create an infinite loop to make sure the game runs forever
	while True:
			# Update the game state based on the clock's interval
			for event in pygame.event.get():
						if event.type == pygame.QUIT:
								pygame.quit()
								exit(0)
				
			# Draw the game screen
			surf.fill((255,255,255))
			draw_snakes(surf)
			
			# Draw the game screen again after each update
			sleep(1)
			
# Draw the snakes and update the game state based on a random number between 0 and 1
def draw_snakes(surf):
	for i in range(3):
		pygame.draw.line(surf, (255,0,0), (random()*80-30, random()*40+40), (random()*80+30, random()*40+40))
        
# Function to handle user input and update the game state based on a random number between 0 and 1
def handle_input():
	while True:
			if randint(0, 1):
						# If the direction of the snakes has changed, update their positions accordingly
						for i in range(3):
								head[i][1] += randint(-2, 2)
		
			sleep(1)

main()