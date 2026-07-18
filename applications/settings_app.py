import tkinter as tk

from applications.base_app import BaseApp


class SettingsApp(BaseApp):

    TITLE = "Settings"

    def build(self):

        tk.Label(

            self.window,

            text="Settings",

            font=("Segoe UI",20)

        ).pack(pady=20)

        tk.Button(

            self.window,

            text="Desktop"

        ).pack()

        tk.Button(

            self.window,

            text="Network"

        ).pack()

        tk.Button(

            self.window,

            text="Appearance"

        ).pack()