import tkinter as tk


class BaseApp:

    TITLE = "Application"

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.window = None

    def open(self, root):

        if self.window and self.window.winfo_exists():
            self.window.lift()
            return

        self.window = tk.Toplevel(root)
        self.window.title(self.TITLE)
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.build()

    def build(self):
        pass