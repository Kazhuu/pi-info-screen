

class ViewSelector(object):

    def __init__(self, start_index=0):
        self._view_list = ["MainView"]
        self._view_index = start_index

    def show_next_view(self):
        pass

    def show_view(self, view_index=0):
        pass

    def update(self, screen):
        pass
