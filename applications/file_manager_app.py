import tkinter as tk

from tkinter import ttk

from applications.base_app import BaseApp


class FileManagerApp(BaseApp):

    TITLE = "File Explorer"

    def build(self):

        tree = ttk.Treeview(self.window)

        tree.pack(fill="both", expand=True)