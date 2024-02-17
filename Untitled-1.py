import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            #create a rect
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #draw the rect
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]


class FRUIT:
    # create an x and y position
    def __init__(self):
        self.randomize()

    # draw a square
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        # draw the rectangle
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #reposition the fruit
            self.fruit.randomize()
            #add another block to the snake



pygame.init()

#kepernyo meretenek beallitasa
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))

#valtozo, idobeallitashoz
clock = pygame.time.Clock()

main_game = MAIN()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


'''#surface keszitese:
test_surface = pygame.Surface((100,200))
#test_surface szinezese:
test_surface.fill((pygame.Color('blue')))

#rectangle keszites
#test_rect = pygame.Rect(100,200,100,100)

#test_rect elhelyezese
test_rect = test_surface.get_rect(topright = (200,250))
'''



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)

    #szinezzuk a hatteret:
    #screen.fill(pygame.Color('gold'))
    screen.fill((175,215,70))

    main_game.draw_elements()


    '''
    #rect megjelenitese
    #pygame.draw.rect(screen,pygame.Color('red'), test_rect)
    #mozgatjuk a test_rect nevu elemet:
    test_rect.left -= 1

    #rect megjelenitese2
    screen.blit(test_surface,test_rect)
    
    #test_surface nevu surface megjelenitese
    #screen.blit(test_surface,(200,250))
    '''

    #draw all our elements
    pygame.display.update()
    #ora beallitas, tick/1 perc
    clock.tick(60)