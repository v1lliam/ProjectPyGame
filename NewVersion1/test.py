# Pygame шаблон - скелет для нового проекта Pygame
import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load(r'DRAWS\Characters\PNG\Adventurer\Poses\adventurer_stand.png'))
        self.sprites.append(pygame.image.load(r'DRAWS\Characters\PNG\Adventurer\Poses\adventurer_jump.png'))
        self.sprites.append(pygame.image.load(r'DRAWS\Characters\PNG\Adventurer\Poses\adventurer_cheer2.png'))
        self.sprites.append(pygame.image.load(r'DRAWS\Characters\PNG\Adventurer\Poses\adventurer_duck.png'))
        self.current_sprite = 0
        
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.recr.topleft = [pos_x,pos_y]

        def animate(self):
            is_animating = True

        def update(self):
            if self.is_animating == False
                self.current_sprite += 1

                if self.current_sprite >= len(self.sprite)
                    self.currnet.sprite = 0
                    self.is_animating == True

            self.image = self.sprites[self.current_sprite]


# Создаем игру и окно
pygame.init()
clock = pygame.time.Clock()

#окно
screen_w = 400
screen_h = 400
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Test Animation")

#otrisovka 
moving_sprites = pygame.sprite.Group()
player = Player(10,10)
moving_sprites.add(palyer)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()
    
    #draw
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)



pygame.quit()