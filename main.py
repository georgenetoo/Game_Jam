import pygame,sys   
from configuraçao import * 
from Level import Level


class Game:
    def __init__(self):
        # setup geral

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Star Dust")
        self.clock = pygame.time.Clock()

        self.Level=Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            self.Level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
