import pygame, sys
from  walking_bg_2 import Player
import asyncio

pygame.init()

class Game:
    
    async def run(self):
        #Game Screen
        screen_width = 1080
        screen_height = 720
        screen = pygame.display.set_mode((screen_width, screen_height))
        caption = pygame.display.set_caption("Scrolling Bg")
        #Time controler
        clock = pygame.time.Clock()

        bg = pygame.transform.scale(pygame.image.load("./bg0.jpg"),(screen_width, screen_height))
        x = 0

        plx = 300
        ply = 400
        player = Player(plx,ply,bg)
        #main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            clock.tick(50)
            screen.blit(bg,(x,0))
            screen.blit(bg,(x + screen_width, 0))
            x -= 5
            if x < -screen_width:
                x = 0
            
            player.walking(x)
            player.jump(x)
            await asyncio.sleep(0)
            pygame.display.update()
            
            
        pygame.quit()
        sys.exit()
        
if __name__ == "__main__":
    app = Game()
    asyncio.run(app.run())