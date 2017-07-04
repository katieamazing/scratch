'''Breakout'''
import sys
import sdl2
import sdl2.ext
import sdl2.sdlimage

class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.ball = None
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def _overlap(self, item):
        pos, sprite = item
        if sprite == self.ball.sprite:
            return False

        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area

        return (bleft < right and bright > left and
                btop < bottom and bbottom > top)

    def process(self, world, componentsets):
        collitems = [comp for comp in componentsets if self._overlap(comp)]
        if collitems:
            self.ball.velocity.vx = -self.ball.velocity.vx

        # Handle edge collisions
        if (self.ball.sprite.y <= self.miny or
            self.ball.sprite.y + self.ball.sprite.size[1] >= self.maxy):
            self.ball.velocity.vy = - self.ball.velocity.vy

        if (self.ball.sprite.x <= self.minx or
            self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx):
            self.ball.velocity.vx = - self.ball.velocity.vx

class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight

class Velocity(object):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0

class Paddle(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite = sprite
        self.sprite.position = x, y
        self.velocity = Velocity()


class Ball(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite = sprite
        self.sprite.position = x, y
        self.velocity = Velocity()

class Bricks:
    def __init__(self, player):
        pass

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0,0,0))
        super(SoftwareRenderer, self).render(components)

class Player(): #whatever world is??
    def __init__(self, lives, level):
        self.lives = lives
        self.level = level

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window('Breakout', size=(600, 400))
    window.show()

    world = sdl2.ext.World()

    sprite_renderer = SoftwareRenderer(window)



    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    bg_sprite = sdl2.ext.load_image('gradientbg.png')
    #bg_renderer = factory.create_sprite_render_system(window)
    #bg_renderer.render(bg_sprite)

    pad_sprite = factory.from_color((sdl2.ext.Color(255,255,255)), size=(80, 20))
    ball_sprite = factory.from_color((sdl2.ext.Color(255,255,255)), size=(20,20))

    paddle = Paddle(world, pad_sprite, 340, 380)


    movement = MovementSystem(0,0,600,400)
    collision = CollisionSystem(0,0,600,400)
    sprite_renderer = SoftwareRenderer(window)

    world.add_system(movement)
    world.add_system(collision)
    world.add_system(sprite_renderer)

    ball = Ball(world, ball_sprite, 390, 290)
    ball.velocity.vx = -3
    collision.ball = ball


    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_LEFT:
                    paddle.velocity.vx = -3
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    paddle.velocity.vx = 3
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym in (sdl2.SDLK_LEFT, sdl2.SDLK_RIGHT):
                    paddle.velocity.vx = 0
        sdl2.SDL_Delay(10)
        world.process()
    return 0

if __name__ == '__main__':
    sys.exit(run())
