import pygame
import sys
from button import Button
from configuraçao import *
from level import Level

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
BG = pygame.image.load("../assets/stardust.JPEG")

def get_font(size): 
    return pygame.font.Font('../assets/font.ttf', 50)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Star Dust")
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

def play():
    game = Game()
    game.run()

def cutscene():
    font = pygame.font.Font('../assets/font.ttf', 36)
    text = font.render("Bem-vindo à Star Dust!", True, "#fbf1bc")
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    SCREEN.fill((0, 0, 0))
    SCREEN.blit(text, text_rect)
    pygame.display.flip()

    pygame.time.wait(2000) 
    
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(500).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(1000, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(1000, 350), 
                            text_input="PLAY", font=get_font(100), base_color="White", hovering_color="#2b1545")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(1000, 550), 
                            text_input="QUIT", font=get_font(100), base_color="White", hovering_color="#2b1545")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    cutscene()  # Executa a cutscene antes de iniciar o jogo
                    play()      # Inicia o jogo após a cutscene
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main_menu()


