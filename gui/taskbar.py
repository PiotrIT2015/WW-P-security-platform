import tkinter as tk


class Taskbar:


    def __init__(
            self,
            parent,
            window_manager
    ):


        self.window_manager = window_manager


        self.frame = tk.Frame(

            parent,

            bg="#303030",

            height=35

        )


        self.frame.pack(

            side=tk.BOTTOM,

            fill=tk.X

        )


        self.buttons = {}



    def add_button(
            self,
            name,
            title,
            window
    ):


        button = tk.Button(

            self.frame,

            text=title,

            bg="#505050",

            fg="white",

            command=lambda:
            self.toggle(window)

        )


        button.pack(

            side=tk.LEFT,

            padx=2

        )


        self.buttons[name] = button



    def toggle(self, window):

        if window.state()=="normal":

            window.iconify()

        else:

            window.deiconify()

            window.lift()