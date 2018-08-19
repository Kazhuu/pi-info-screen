from tools.framebuffer import Framebuffer
from views.main_view import MainView

import traceback


try:
    framebuffer = Framebuffer()
    surface = framebuffer.get_framebuffer_suface()
    v = MainView(surface)
    while True:
        v.update(surface)
except Exception:
    print(traceback.format_exc(Exception))
