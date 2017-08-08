import sys, pygame, math
pygame.init()

size = width, height = 600, 400

speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)


rows, cols = 3, 12

class Bricks(object):
    def __init__(self, rows, cols, sprite_name):
        self.sprite = pygame.image.load(sprite_name)
        self.grid = self.initlist(rows, cols)

    def initlist(self, rows, cols): #returns a list of lists of lists
        bricklist = []
        for row in range(0,rows):
            bricklist.append([])
            bricky = 25 * row + 50
            for col in range (0,cols):
                brickx = col * 50 + (.5 * (600-(50*cols)))
                bricklist[row].append(Brick(brickx, bricky, self.sprite))
        return bricklist

    def draw(self):
        for row in self.grid:
            for brick in row:
                brick.draw()

class Brick(object):
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.sprite = sprite
        self.hit = False

    def draw(self):
        if not self.hit:
            screen.blit(self.sprite, pygame.Rect(self.x, self.y, self.width, self.height))

class Paddle(object):
    def __init__(self, x, velx):
        self.x = x
        self.y = height - 4
        self.width = 80
        self.height = 4
        self.velx = velx
        self.speed = 4

    def keypress(self, key):
        if key == pygame.K_LEFT and self.velx > -self.speed:
            self.velx -= 1
        elif key == pygame.K_RIGHT and self.velx < self.speed:
            self.velx += 1

    def update(self):
        # apply friction
        self.velx *= 0.95
        # move paddle
        self.x += self.velx
        # lock paddle to screen
        if self.x < 0:
            self.x = 0
        elif self.x > width - 80:
            self.x = width - 80

    def draw(self):
        pygame.draw.rect(screen, (255,255,255), [self.x, self.y, self.width, self.height])

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.r = 6
        self.launched = False
        self.speed = 6

    def launch(self, pos):
        if self.launched:
            pass
        mx = pos[0] - 300
        my = pos[1] - 400
        dist = math.sqrt(mx ** 2 + my ** 2)
        self.velx = mx/(dist)
        self.vely = my/(dist)
        self.launched = True

    def update(self):
        # move ball
        self.x += self.velx
        self.y += self.vely
        # edge collisions
        if self.x < 0 or self.x > width:
            self.velx *= -1
        if self.y < 0:
            self.vely *= -1
        if self.y > height:
            #lose a point, reset ball
            pass

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.r)

bricks = Bricks(rows, cols, "waterbrick.png")
paddle = Paddle(width/2, 0)
ball = Ball(paddle.x + paddle.width/2, paddle.y + 3)
pygame.key.set_repeat(30, 30)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            paddle.keypress(event.key)
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            ball.launch(position)
    paddle.update()
    ball.update()
    screen.fill(black)
    bricks.draw()
    paddle.draw()
    ball.draw()
    pygame.display.flip()
