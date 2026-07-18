import tkinter as tk


class WindowManager:


    def __init__(self, root):

        self.root = root

        self.windows = {}



    def open_window(
            self,
            name,
            title,
            size="800x600"
    ):

        if name in self.windows:

            window = self.windows[name]

            if window.winfo_exists():

                window.deiconify()
                window.lift()

                return window



        window = tk.Toplevel(self.root)

        window.title(title)

        window.geometry(size)


        self.windows[name] = window


        return window



    def close_window(self, name):

        if name in self.windows:

            window = self.windows[name]

            if window.winfo_exists():

                window.destroy()


            del self.windows[name]