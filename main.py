import pygame
import random
pygame.init()

class Dice(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()

        # All dice's images
        image1 = pygame.image.load('images/dice_states/dice_1.png')
        image2 = pygame.image.load('images/dice_states/dice_2.png')
        image3 = pygame.image.load('images/dice_states/dice_3.png')
        image4 = pygame.image.load('images/dice_states/dice_4.png')
        image5 = pygame.image.load('images/dice_states/dice_5.png')
        image6 = pygame.image.load('images/dice_states/dice_6.png')
        self.images = [image1, image2, image3, image4, image5, image6]
        self.imageindex = 0

        # Other arguments
        self.num = num
        self.image = self.images[self.imageindex]
        self.rect = self.image.get_rect(midtop = (150, 50))

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # Roll the dice
            self.imageindex = random.randint(0, 5)
            self.image = self.images[self.imageindex]

    def update(self):
        self.input()

# Create a window
screen = pygame.display.set_mode((300, 300))

# Icon and caption
pygame.display.set_caption('Dice')
icon = pygame.image.load('images/dice_icon.png')
pygame.display.set_icon(icon)

# Prompt
font = pygame.font.Font('other_assests/default.ttf', 25)
prompt_surf = font.render('Press SPACE!', False, (25, 25, 25))
prompt_rect = prompt_surf.get_rect(midtop = (150, 10))

# Create the dice
dice_group = pygame.sprite.GroupSingle()
dice_group.add(Dice(1))

# Fill the screen with white
screen.fill((255, 255, 255))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Display the prompt first
    screen.blit(prompt_surf, prompt_rect)

    # Update the dice
    dice_group.draw(screen)
    dice_group.update()

    pygame.display.update()
    pygame.time.Clock().tick(60)
