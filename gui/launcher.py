"""
WW-P Security Platform
Launcher Menu
"""


import tkinter as tk



class Launcher:


    def __init__(
            self,
            parent,
            apps
    ):

        self.parent = parent

        self.apps = apps


        self.menu = tk.Menu(

            parent,

            tearoff=False

        )


        self.build()



    def build(self):

        for name, callback in self.apps.items():

            self.menu.add_command(

                label=name,

                command=callback

            )


        self.menu.add_separator()


        self.menu.add_command(

            label="Exit",

            command=self.parent.destroy

        )



    def show(
            self,
            widget
    ):

        x = widget.winfo_rootx()

        y = widget.winfo_rooty()


        self.menu.tk_popup(

            x,

            y

        )