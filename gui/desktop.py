"""
gui/desktop.py

WW-P Security Platform
Desktop Environment
Version 1.2
"""

import os
import tkinter as tk
from tkinter import messagebox

from tkinter import Menu

from PIL import Image, ImageTk

from gui.taskbar import Taskbar
from gui.windows import WindowManager
from gui.launcher import Launcher

from applications.security_app import SecurityApp
from applications.network_app import NetworkApp
from applications.web_app import WebApp

from applications.file_explorer import FileExplorer
from applications.pca_analyzer import PCAAnalyzer
from applications.settings import SettingsApp

class Desktop:
    """
    Główny pulpit systemu WW-P Security Platform.
    """


    def __init__(self, root):

        self.root = root

        self.root.configure(
            bg="#20242b"
        )


        # =====================================
        # Window Manager
        # =====================================

        self.window_manager = WindowManager(
            root
        )


        # =====================================
        # Aplikacje
        # =====================================

        self.security_app = SecurityApp()
        self.network_app = NetworkApp()
        self.web_app = WebApp()
        self.file_explorer = FileExplorer()
        self.settings_app = SettingsApp()
        self.pca_analyzer = PCAAnalyzer()



        # =====================================
        # Ikony pulpitu
        # =====================================

        self.desktop_icons_data = [

            {
                "name": "File Explorer",
                "icon": "folder_icon.png"
            },

            {
                "name": "Settings",
                "icon": "settings_icon.png"
            }





            # {
            #     "name": "Pandas Analyzer",
            #     "icon": "chart_icon.png"
            # },
            #
            # {
            #     "name": "PCA Analyzer",
            #     "icon": "chart_icon.png"
            # },
            #
            # {
            #     "name": "Web Explorer",
            #     "icon": "browser.png"
            # },
            #
            # {
            #     "name": "Shodan - shortcut",
            #     "icon": "browser.png"
            # },
            #
            # {
            #     "name": "Network Monitor",
            #     "icon": "network_monitor.png"
            # },
            #
            # {
            #     "name": "Nmap Scanner",
            #     "icon": "network_scanner.png"
            # },
            #
            # {
            #     "name": "WitchCraft (Web)",
            #     "icon": "musical-note.png"
            # },

        ]
        



        # przechowywanie PhotoImage
        self.icon_images = []


        # =====================================
        # GUI
        # =====================================

        self.create_desktop()


        # pasek menu
        self.taskbar = Taskbar(
            self.root,
            self.window_manager
        )


        # rejestr aplikacji
        self.create_app_registry()


        # launcher
        self.create_launcher()


        # ikony
        self.create_icons()

        self.create_menu_bar()

    # ==================================================
    # Desktop
    # ==================================================

    def create_desktop(self):


        self.frame = tk.Frame(
            self.root,
            bg="#20242b"
        )

        self.frame.pack(
            fill=tk.BOTH,
            expand=True
        )


        self.title_label = tk.Label(
            self.frame,
            text="WW-P Security Platform",
            font=(
                "Segoe UI",
                24,
                "bold"
            ),
            fg="white",
            bg="#20242b"
        )


        self.title_label.pack(
            pady=(20,5)
        )


        self.subtitle = tk.Label(
            self.frame,
            text="Cyber Security Desktop Environment",
            font=(
                "Segoe UI",
                11
            ),
            fg="#7fd6ff",
            bg="#20242b"
        )


        self.subtitle.pack()



        self.desktop_icons = tk.Frame(
            self.frame,
            bg="#20242b"
        )


        self.desktop_icons.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=20
        )



    # ==================================================
    # Rejestr aplikacji
    # ==================================================

    def create_app_registry(self):


        self.apps = {

            "File Explorer":
                lambda:
                self.file_explorer.open(
                    self.root
                ),

            "Network Monitor":
                lambda:
                self.network_app.open(
                    self.root
                ),


            "Nmap Scanner":
                lambda:
                self.security_app.open(
                    self.root
                ),


            "Web Explorer":
                lambda:
                self.web_app.open(
                    self.root
                ),


            "Shodan - shortcut":
                lambda:
                self.web_app.open_shodan(
                    self.root
                ),


            "Settings":
                lambda:
                self.settings.open(
                    self.root
                ),

            "PCA Analyzer":
                lambda:
                self.pca_analyzer.open(
                    self.root
                ),

        }



    # ==================================================
    # Launcher
    # ==================================================

    def create_launcher(self):

        self.launcher = Launcher(
            self.root,
            self.apps
        )



    # ==================================================
    # Ładowanie ikon
    # ==================================================

    def load_icon(
        self,
        filename,
        size=(64,64)
    ):


        path = os.path.join(
            "img",
            "sys",
            filename
        )


        try:

            image = Image.open(
                path
            )


        except Exception:


            image = Image.new(
                "RGBA",
                size,
                (
                    70,
                    130,
                    180,
                    255
                )
            )


        image = image.resize(
            size,
            Image.Resampling.LANCZOS
        )


        photo = ImageTk.PhotoImage(
            image
        )


        self.icon_images.append(
            photo
        )


        return photo



    # ==================================================
    # Ikony pulpitu
    # ==================================================

    def create_icons(self):


        columns = 4


        for index, item in enumerate(
            self.desktop_icons_data
        ):


            frame = tk.Frame(
                self.desktop_icons,
                bg="#20242b",
                width=120,
                height=120
            )


            frame.grid(
                row=index // columns,
                column=index % columns,
                padx=20,
                pady=20
            )


            frame.pack_propagate(
                False
            )


            icon = self.load_icon(
                item["icon"]
            )


            icon_label = tk.Label(
                frame,
                image=icon,
                bg="#20242b"
            )


            icon_label.image = icon


            icon_label.pack(
                pady=5
            )



            text_label = tk.Label(
                frame,
                text=item["name"],
                fg="white",
                bg="#20242b",
                font=(
                    "Segoe UI",
                    9
                ),
                wraplength=110
            )


            text_label.pack()



            icon_label.bind(
                "<Double-Button-1>",
                lambda event,
                name=item["name"]:
                self.launch_app(name)
            )


            text_label.bind(
                "<Double-Button-1>",
                lambda event,
                name=item["name"]:
                self.launch_app(name)
            )



    # ==================================================
    # Uruchamianie aplikacji
    # ==================================================

    def launch_app(
        self,
        name
    ):


        if name in self.apps:

            self.apps[name]()


        else:

            messagebox.showinfo(
                "WW-P Security Platform",
                f"{name} module not configured"
            )

    # ==================================================
    # Pasek menu
    # ==================================================

    def create_menu_bar(self):

        self.menu_bar = Menu(
            self.root,
            bg="#11151b",
            fg="white",
            activebackground="#2d6cdf",
            activeforeground="white"
        )

        # -------------------------
        # Menu WW-P
        # -------------------------

        system_menu = Menu(
            self.menu_bar,
            tearoff=0,
            bg="#11151b",
            fg="white"
        )

        system_menu.add_command(
            label="About WW-P Security Platform",
            command=lambda:
            messagebox.showinfo(
                "WW-P Security Platform",
                "Cyber Security Desktop Environment\nVersion 1.2"
            )
        )

        system_menu.add_separator()

        system_menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        self.menu_bar.add_cascade(
            label="WW-P",
            menu=system_menu
        )

        # -------------------------
        # Applications
        # -------------------------

        app_menu = Menu(
            self.menu_bar,
            tearoff=0,
            bg="#11151b",
            fg="white"
        )

        for name in [
            "Network Monitor",
            "Nmap Scanner",
            "Web Explorer",
            "PCA Analyzer"
        ]:
            app_menu.add_command(
                label=name,
                command=lambda n=name:
                self.launch_app(n)
            )

        self.menu_bar.add_cascade(
            label="Applications",
            menu=app_menu
        )

        # # -------------------------
        # # Security
        # # -------------------------
        #
        # security_menu = Menu(
        #     self.menu_bar,
        #     tearoff=0,
        #     bg="#11151b",
        #     fg="white"
        # )
        #
        # security_menu.add_command(
        #     label="Nmap Scanner",
        #     command=lambda:
        #     self.launch_app(
        #         "Nmap Scanner"
        #     )
        # )
        #
        # security_menu.add_command(
        #     label="Network Monitor",
        #     command=lambda:
        #     self.launch_app(
        #         "Network Monitor"
        #     )
        # )
        #
        # self.menu_bar.add_cascade(
        #     label="Security",
        #     menu=security_menu
        # )

        # -------------------------
        # Help
        # -------------------------

        help_menu = Menu(
            self.menu_bar,
            tearoff=0,
            bg="#11151b",
            fg="white"
        )

        help_menu.add_command(
            label="Documentation",
            command=lambda:
            messagebox.showinfo(
                "Documentation",
                "WW-P Security Platform documentation"
            )
        )

        self.menu_bar.add_cascade(
            label="Help",
            menu=help_menu
        )

        # instalacja menu w oknie

        self.root.config(
            menu=self.menu_bar
        )
