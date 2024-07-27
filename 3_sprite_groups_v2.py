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
monster_group = pygame.sprite.Group()
for i in range(10):
    #don't need to pass self, just x and y
    monster = Monster(i*64, 10)
    #add monster to monster_group
    monster_group.add(monster)


#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))

    #update and draw (like bliting) assets
    #this single line of code will draw all 10 monsters
    #each monster is unique
    #"update" and "draw" are specific methods to a group and so must use that exact wording in code
    monster_group.draw(display_surface)
    monster_group.update()

    #update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#end the game
pygame.quit()

