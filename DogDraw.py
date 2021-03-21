import pygame

class DrawDog(object):
    def __init__(self):
        pygame.init()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.dis = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('PZ-1')
        self.x1_change = 0
        self.y1_change = 0
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.x1 = 300
        self.y1 = 300
        self.run()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -4
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = 4
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -4
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = 4
                        self.x1_change = 0

            self.x1 += self.x1_change
            self.y1 += self.y1_change
            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.white, [self.x1, self.y1, 10, 10])

            pygame.display.update()

            self.clock.tick(30)

DrawDog()