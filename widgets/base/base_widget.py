import os


class BaseWidget(object):

    def __init__(self, screen, width=None, heigth=None):
        self._widget_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir))
        if not width:
            self._width = screen.get_width()
        else:
            self._width = width
        if not heigth:
            self._height = screen.get_heigth()
        else:
            self._height = heigth

    def get_size(self):
        return (self._width, self._height)
