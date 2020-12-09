import os
import pygame
import pygame_menu
from pygame_menu.themes import Theme

icon = pygame.image.load('PNG/menu/icon.png')
pygame.display.set_icon(icon)

font= 'PNG/menu/font.ttf'

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((700, 700))


def support_the_devs():
    """
    Make a charity to the developers
    """
    print('Soon!')


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print(' soon!')

myimage = pygame_menu.baseimage.BaseImage(
    image_path='PNG/menu/background.jpg',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)

mytheme = Theme(widget_font=font,
                background_color=(255, 255, 255),
                title_shadow=True,
                title_background_color=(0, 0, 0)
                )

mytheme.background_color = myimage

menu = pygame_menu.Menu(height=650,
                        width=650,
                        theme=mytheme,
                        title='ZaLuPa KoNyA')

menu.add_text_input('Name: ', default='Player 1',
                    font_color= (0, 0, 0))
menu.add_button('Play', start_the_game,
                 font_color= (0, 0, 0))
menu.add_button('Support the devs ', support_the_devs,
                font_color= (0, 0, 0))
menu.add_button('Exit', pygame_menu.events.EXIT,
                align=pygame_menu.locals.ALIGN_RIGHT,
                font_color= (0, 0, 0))

if __name__ == '__main__':
    menu.mainloop(surface)
