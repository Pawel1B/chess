
import pygame
import pieces.controller.background as background


class game:
    def __init__(self, main_config):
        self.resolution=[main_config['Global']['resolution_x'],main_config['Global']['resolution_y']]
        self.FPS=main_config['Global']['FPS']
        background_image=background(self.resolutionm, main_config)
        self.background=background_image

    def run(self):
        WIN=pygame.display.set_mode((self.resolution[0],self.resolution[1]))
        pygame.display.set_caption("chess")
        clock=pygame.time.Clock()
        run_constant = True

        def draw_window():#todo background
            WIN.fill((255,255,255))
            pygame.display.update()


        while run_constant:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_constant=False
                    break
            draw_window()
        pygame.quit







