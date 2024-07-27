import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Group Collide!")

#set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#create classes
class Game():
    """A class to help and manage our Game"""
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        #check for collisions between knight group and monster group
        self.check_collisions()
        #self.check_game_over()
        #self.reset_player()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)



#the class Knight inherits from the sprite class 
class Knight(pygame.sprite.Sprite):
    #initialize Knight class
    #what does our Knight class need? Self and parameters.
    def __init__(self, x, y):
        #Knight class is a sub class to the sprite class and so
        #we have to call the super classes init method first
        super().__init__()
        #specifics to the knight
        #we want to link image to given object (Knight))
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        #update and move knight
        self.rect.y -= self.velocity


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

#create a monster group
my_monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

#create a knight group
my_knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT-64)
    my_knight_group.add(knight)

#create a game object
my_game = Game(my_monster_group, my_knight_group)

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the surface
    display_surface.fill((0, 0, 0))

    #update and draw sprite group
    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_knight_group.update()
    my_knight_group.draw(display_surface)

    #update the game
    my_game.update()

    #update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)


#quit game
pygame.quit()