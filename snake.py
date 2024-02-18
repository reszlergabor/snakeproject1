import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_tl.png').convert_alpha()



    def draw_snake(self):
        '''Ez a korabbi kigyo, meg csak szines blokkokbol
        for block in self.body:
            #create a rect
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #draw the rect
            pygame.draw.rect(screen,(183,111,122),block_rect)'''
        
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index,block in enumerate(self.body):
            #1. Kell egy négyszög a pozícionáláshoz
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            #2. milyen irányba néz a fej?
            if index == 0:
                #3. kigyo fej iranyat updateljuk
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    #ekkor ez vertikalis resze a kigyonak
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    #ekkor ez horizontalis resze a kigyonak
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                     


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[len(self.body) - 1] - self.body[len(self.body) - 2]
        #de ugyanez ez a sor is:
        #tail_relation = self.body[-1] - self.body[-2]

        if tail_relation == Vector2(-1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,1): self.tail = self.tail_down


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True     


class FRUIT:
    # create an x and y position
    def __init__(self):
        self.randomize()

    # draw a square
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # draw the rectangle
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #reposition the fruit
            self.fruit.randomize()
            #add another block to the snake
            self.snake.add_block()

    def check_fail(self):
        #check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        #check snake beleharap-e magaba
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
            
    def game_over(self):
        pygame.quit()
        sys.exit()

    

pygame.init()

#kepernyo meretenek beallitasa
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))

#valtozo, idobeallitashoz
clock = pygame.time.Clock()

main_game = MAIN()

apple = pygame.image.load('Graphics/apple.png').convert_alpha()


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
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN  and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT  and main_game.snake.direction.x != -1:
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