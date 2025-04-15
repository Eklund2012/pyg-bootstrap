import pygame, asyncio

from .settings import WIDTH, HEIGHT, FPS



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PLACEHOLDER")
        self.clock = pygame.time.Clock()
        self.frame_count = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self, keys):
        pass

    def draw(self):
        pass
        pygame.display.flip()

    async def run(self):
        while True:
            keys = pygame.key.get_pressed()
            self.handle_events()
            self.update(keys)
            self.draw()

            self.clock.tick(FPS)
            self.frame_count += 1
            await asyncio.sleep(0)