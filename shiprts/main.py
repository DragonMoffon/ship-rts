from shiprts.lib.application import Window
from shiprts.views.root import RootView

def main() -> None:
    win = Window()
    root = RootView()

    win.show_view(root)
    win.run()
