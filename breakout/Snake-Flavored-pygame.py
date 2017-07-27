import sys, pygame
pygame.init()

size = width, height = 600, 400

speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
bricklist = None

brick = pygame.image.load("waterbrick.png")
brickrect = brick.get_rect()
rows, cols = 3, 12
def initlist(rows, cols): #returns a list of lists of lists
    bricklist = []
    for row in range(0,rows):
        bricklist.append([])
        bricky = 25 * row + 50
        for col in range (0,cols):
            brickx = col * 50 + (.5 * (600-(50*cols)))
            brect = pygame.Rect(brickx, bricky, 50, 25)
            bricklist[row].append([False, brect])
    return bricklist
bricklist = initlist(rows, cols)
print(bricklist)
def draw_bricks(bricklist):
    for row in range (0,rows):
        for col in range(0,cols):
            if bricklist[row][col][0] == False:
                screen.blit(brick, bricklist[row][col][1])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    draw_bricks(bricklist)
    pygame.display.flip()
