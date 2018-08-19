import os
import pygame


class Framebuffer(object):

    def __init__(self):
        self.screen = None
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print("I'm running under X display = {0}".format(disp_no))
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print('Driver: {0} failed.'.format(driver))
                continue
            print("Using {video} video driver".format(video=driver))
            found = True
            break

        if not found:
            raise Exception('No suitable video driver found!')

        size = (
            pygame.display.Info().current_w,
            pygame.display.Info().current_h)
        print("Framebuffer size: {width} x {heigth}".format(
            width=size[0], heigth=size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.screen.fill((0, 0, 0))
        pygame.font.init()
        pygame.mouse.set_visible(False)
        pygame.display.update()

    def get_framebuffer_suface(self):
        return self.screen

    def test(self):
        red = (255, 0, 0)
        self.screen.fill(red)
        pygame.display.update()
