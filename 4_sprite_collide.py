import pygame, random

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
    #a player that fights monsters
    def __init__(self, x, y, my_monster_group):
        #so Player class can have access to the super sprite class
        #we must call init from sprite class
        super().__init__()

        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = 5

        self.my_monster_group = my_monster_group


    def update(self):
        #move player and check for collisions
        #two seperate methods
        self.move()
        self.check_collisions()

    def move(self):
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
        #use sprite collide method of sprite class
        #check for collisions between player (self) and monster group
        #takes three arguements: sprite in question (self) and the group, and whether or not we want to destroy
        #the sprite of the group
        pygame.sprite.spritecollide(self, self.my_monster_group, True)
        print(len(self.my_monster_group))

#the class Monster inherits from the sprite class 
class Monster(pygame.sprite.Sprite):
    #initialize Monster class
    #what does our MOnster class need? Self and parameters.
    def __init__(self, x, y):
        #Monster class is a sub class to the sprite class and so
        #we have to call the super classes init method first
        super().__init__()
        #specifics to the monster
        #we want to link image to given object (Monster)
        self.image = pygame.image.load("blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        #update and move monster
        self.rect.y += self.velocity

#create a monster group and add 10 monsters
my_monster_group = pygame.sprite.Group()
for i in range(10):
    #don't need to pass self, just x and y
    monster = Monster(i*64, 10)
    #add monster to monster_group
    my_monster_group.add(monster)

#you cannot draw individual sprites to the screen, you have to draw sprite groups
#individual sprites do not have the draw method
#create player group and add a player
player_group = pygame.sprite.Group()
player = Player(500, 500, my_monster_group)
player_group.add(player)

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))

    #update and draw (like bliting) assets
    player_group.update()
    player_group.draw(display_surface)

    #this single line of code will draw all 10 monsters
    #each monster is unique
    #"update" and "draw" are specific methods to a group and so must use that exact wording in code
    my_monster_group.update()
    my_monster_group.draw(display_surface)


    #update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#end the game
pygame.quit()

