"""
applications/settings_app.py

WW-P Security Platform
Settings Application
Based on OS-WW-P-1 Settings module
"""

import tkinter as tk
from tkinter import messagebox


class SettingsApp:
    """
    Centrum ustawień WW-P Security Platform.
    """


    def __init__(self):

        self.window = None



    def open(self, root):

        self.window = tk.Toplevel(root)

        self.window.title(
            "WW-P Settings"
        )

        self.window.geometry(
            "650x450"
        )

        self.window.configure(
            bg="#20242b"
        )


        # ==========================
        # Nagłówek
        # ==========================

        title = tk.Label(
            self.window,
            text="WW-P Security Platform Settings",
            font=(
                "Segoe UI",
                18,
                "bold"
            ),
            fg="white",
            bg="#20242b"
        )

        title.pack(
            pady=15
        )


        # ==========================
        # Notebook
        # ==========================

        notebook = tk.Frame(
            self.window,
            bg="#20242b"
        )

        notebook.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=20
        )


        # --------------------------
        # System
        # --------------------------

        system_frame = tk.LabelFrame(
            notebook,
            text="System",
            fg="white",
            bg="#20242b"
        )

        system_frame.pack(
            fill=tk.X,
            pady=10
        )


        self.dark_mode = tk.BooleanVar(
            value=True
        )


        tk.Checkbutton(
            system_frame,
            text="Dark Mode",
            variable=self.dark_mode,
            fg="white",
            bg="#20242b",
            selectcolor="#11151b"
        ).pack(
            anchor="w"
        )



        # --------------------------
        # Security
        # --------------------------

        security_frame = tk.LabelFrame(
            notebook,
            text="Security",
            fg="white",
            bg="#20242b"
        )


        security_frame.pack(
            fill=tk.X,
            pady=10
        )


        tk.Button(
            security_frame,
            text="Clear Logs",
            command=self.clear_logs
        ).pack(
            side=tk.LEFT,
            padx=5,
            pady=5
        )


        tk.Button(
            security_frame,
            text="Security Scan",
            command=self.security_scan
        ).pack(
            side=tk.LEFT,
            padx=5
        )



        # --------------------------
        # About
        # --------------------------

        about_frame = tk.LabelFrame(
            notebook,
            text="Information",
            fg="white",
            bg="#20242b"
        )


        about_frame.pack(
            fill=tk.X,
            pady=10
        )


        tk.Label(
            about_frame,
            text=
            "WW-P Security Platform\n"
            "Desktop Environment\n"
            "Version 1.2",
            fg="white",
            bg="#20242b"
        ).pack(
            pady=10
        )



    def clear_logs(self):

        messagebox.showinfo(
            "Logs",
            "Security logs cleared."
        )



    def security_scan(self):

        messagebox.showinfo(
            "Security",
            "Security scan started."
        )