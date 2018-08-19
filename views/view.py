import os
import pygame
import time
from tools import aspect_scale
from time import strftime, localtime


class BaseView(object):

    def __init__(self, screen):
        self.screen = screen
        self.run = True

    def main(self):
        pass

    def stop(self):
        self.run = False


class ImageViewerView(BaseView):

    def __init__(self, screen, image_folder_path):
        super(ImageViewerView, self).__init__(screen)
        self.image_folder_path = image_folder_path

    def main(self):
        i = 0
        images = [
            f
            for f in os.listdir(self.image_folder_path)
            if os.path.isfile(os.path.join(self.image_folder_path, f))]
        while self.run:
            image = pygame.image.load(os.path.join(self.image_folder_path,
                                                   images[i]))
            self.screen.blit(image, image.get_rect())
            pygame.display.update()
            time.sleep(3)
            i += 1
            if i >= len(images):
                i = 0


class ClockView(BaseView):

    def __init__(self, screen):
        super(ClockView, self).__init__(screen)

    def main(self):
        screen_size = self.screen.get_size()
        clockface = pygame.image.load(
            os.path.join("./images/clockface-darkblue.png")).convert_alpha()
        clockface = aspect_scale(clockface, screen_size)
        hourhand = pygame.image.load(
            os.path.join("./images/hourhand-darkblue.png")).convert_alpha()
        hourhand = aspect_scale(hourhand, screen_size)
        minhand = pygame.image.load(
            os.path.join("./images/minhand-darkblue.png")).convert_alpha()
        minhand = aspect_scale(minhand, screen_size)
        width_center = int(screen_size[0]/2)
        min_tick_angle = 60.0/360.0
        hour_tick_angle = 12.0/360.0
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
        while self.run:
            ts = time.localtime()
            hour = ts.tm_hour
            min = ts.tm_min
            min_angle = -int(min/min_tick_angle)
            hour_angle = -int(hour/hour_tick_angle)-int(min/60.0*30)
            r_hourhand = pygame.transform.rotate(
                hourhand, hour_angle)
            r_minhand = pygame.transform.rotate(
                minhand, min_angle)
            self.screen.fill((0, 0, 0))
            self.screen.blit(
                clockface, (width_center-int(clockface.get_width()/2), 0))
            self.screen.blit(
                r_hourhand, (width_center-int(r_hourhand.get_width()/2),
                             int(screen_size[1]/2-r_hourhand.get_height()/2)))
            self.screen.blit(
                r_minhand, (width_center-int(r_minhand.get_width()/2),
                            int(screen_size[1]/2-r_minhand.get_height()/2)))
            pygame.display.flip()
