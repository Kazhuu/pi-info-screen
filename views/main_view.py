from base_view import BaseView
from widgets.date_time.clock_widget import ClockWidget

import pygame


class MainView(BaseView):

    def __init__(self, screen):
        super(MainView, self).__init__()
        self._widget_list.append(ClockWidget(
            screen, screen.get_width(), screen.get_height()))

    def update(self, screen):
        screen.fill((0, 0, 0))
        for widget in self._widget_list:
            widget.update(screen)
        pygame.display.flip()
