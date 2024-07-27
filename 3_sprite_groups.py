import pygame, random

#from pygame.sprite import _Group

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Groups!")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#define classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, monster_group):
        #calling super class init method
        super().__init__()
        #load in image
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 10

        self.monster_group = monster_group

    def update(self):
        #move player and check for collisions
        self.move()
        self.check_collisions()

    def move(self):
        #move the player continuously
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        #check if individual sprite collides with sprite group
        #in other words player (self) with monster group
        #takes 3 parameters: individual sprite (player or self because we are inside of player class), group we are looking at, and 
        #whether or not we want to destroy the sprite that we collide with from this group
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))


#in parenthesis is the super sprite class
class Monster(pygame.sprite.Sprite):
    #initialize class
    #this Monster class is a sub class to the sprite class
    #so call super classes init class first
    def __init__(self, x, y):
        super().__init__()
        #give monster its own attributes
        #link image to given object we are creating
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    #this method will always have the name 'update'
    def update(self):
        #update and move the monster
        #move the rect as usual
        self.rect.y += self.velocity

#create a monster group and add 10 monsters
my_monster_group = pygame.sprite.Group()
for i in range(10):
    #just need to pass in x, y coordinates, do not need to pass self
    my_monster_group = Monster(i*64, 10)
    my_monster_group.add(my_monster_group)

#you can't draw sprites to the screen, you have to draw sprite groups
#individual sprites cannot access 'draw' method
#create a player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, my_monster_group)
player_group.add(player)

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0, 0, 0))

    #draw assets and update
    player_group.update()
    player_group.draw(display_surface)

    #this one line will draw all 10 monsters 
    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#end the game
pygame.quit()

