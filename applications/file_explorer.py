"""
applications/file_explorer.py

WW-P Security Platform
File Explorer
"""

import os
import tkinter as tk
from tkinter import filedialog


class FileExplorer:
    """
    Prosty menedżer plików WW-P.
    """


    def __init__(self):

        self.window = None



    def open(self, root):

        self.window = tk.Toplevel(root)

        self.window.title(
            "WW-P File Explorer"
        )

        self.window.geometry(
            "800x500"
        )

        self.window.configure(
            bg="#20242b"
        )


        # -------------------------
        # Toolbar
        # -------------------------

        toolbar = tk.Frame(
            self.window,
            bg="#11151b"
        )

        toolbar.pack(
            fill=tk.X
        )


        tk.Button(
            toolbar,
            text="Open Folder",
            command=self.open_folder
        ).pack(
            side=tk.LEFT,
            padx=5,
            pady=5
        )


        # -------------------------
        # Path
        # -------------------------

        self.path_label = tk.Label(
            self.window,
            text=os.getcwd(),
            fg="white",
            bg="#20242b"
        )

        self.path_label.pack(
            fill=tk.X,
            pady=5
        )


        # -------------------------
        # File list
        # -------------------------

        self.listbox = tk.Listbox(
            self.window,
            bg="#15191f",
            fg="white",
            font=(
                "Segoe UI",
                11
            )
        )


        self.listbox.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )


        self.load_directory(
            os.getcwd()
        )



    def load_directory(self, path):

        self.listbox.delete(
            0,
            tk.END
        )


        try:

            for item in os.listdir(path):

                self.listbox.insert(
                    tk.END,
                    item
                )


            self.path_label.config(
                text=path
            )


        except Exception as error:

            self.listbox.insert(
                tk.END,
                str(error)
            )



    def open_folder(self):

        folder = filedialog.askdirectory()


        if folder:

            self.load_directory(
                folder
            )