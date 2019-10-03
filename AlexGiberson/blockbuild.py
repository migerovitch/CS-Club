import pygame, sys
from pygame.locals import *
import csv

width = 600
height = 600

fps = 15
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width,height))

exit = False
blue = (0,0,255)
black = (0,0,0)



x = 0
y = 0
xy = []
  

levelname = input("Enter level name (omit file tag): ")
rectwidth = int(input("Enter rect width: "))
rectheight = int(input("Enter rect height: "))


while exit == False:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit = True
	if event.type == pygame.KEYDOWN:
				#print(str(event.key))
				if event.key == pygame.K_LEFT:
					x += -rectwidth/2
					#print(str(x)+", "+str(y))
				elif event.key == pygame.K_RIGHT:
					x += rectwidth/2
					#print(str(x)+", "+str(y))
				elif event.key == pygame.K_UP:
					y += -rectheight/2
					#print(str(x)+", "+str(y))
				elif event.key == pygame.K_DOWN:
					y += rectheight/2
				if event.key == pygame.K_c:
					xy.append((x,y,rectwidth,rectheight))
					print("Block saved to list")
				if event.key == pygame.K_r:
					print("Resize block: ")
					rectwidth = int(input("Enter rect width: "))
					rectheight = int(input("Enter rect height: "))
				if event.key == pygame.K_f:
					print("Saving..")
					csvfile = open(levelname + ".csv","w", newline='')
					file_writer = csv.writer(csvfile)
					for tup in xy:
						file_writer.writerow(tup)
					csvfile.close()
					print("Saved!")
					exit = True

	screen.fill(black)
	pygame.draw.rect(screen,blue,[x,y,rectwidth,rectheight])
	for coord in xy:
		pygame.draw.rect(screen,blue,[coord[0],coord[1],coord[2],coord[3]])
	pygame.display.update()
	clock.tick(fps)
pygame.quit()
sys.exit()