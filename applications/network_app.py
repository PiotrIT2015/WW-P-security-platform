"""
WW-P Security Platform

Network Monitor
v1.0.2
"""

import socket
import threading
import tkinter as tk
from tkinter import ttk

import requests


class NetworkApp:

    def __init__(self):
        self.window = None

    def open(self, root):

        if self.window and self.window.winfo_exists():
            self.window.lift()
            return

        self.window = tk.Toplevel(root)
        self.window.title("Network Monitor")
        self.window.geometry("700x500")

        self.create_widgets()

        self.refresh()

    def create_widgets(self):

        frame = ttk.Frame(self.window, padding=15)
        frame.pack(fill="both", expand=True)

        title = ttk.Label(
            frame,
            text="Network Monitor",
            font=("Segoe UI", 18)
        )
        title.pack(pady=10)

        info = ttk.LabelFrame(
            frame,
            text="Network Information"
        )

        info.pack(fill="x", pady=10)

        ttk.Label(info, text="Hostname").grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.hostname_label = ttk.Label(info, text="-")
        self.hostname_label.grid(
            row=0,
            column=1,
            sticky="w"
        )

        ttk.Label(info, text="Local IP").grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.local_ip_label = ttk.Label(info, text="-")
        self.local_ip_label.grid(
            row=1,
            column=1,
            sticky="w"
        )

        ttk.Label(info, text="Public IP").grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.public_ip_label = ttk.Label(info, text="-")
        self.public_ip_label.grid(
            row=2,
            column=1,
            sticky="w"
        )

        ttk.Label(info, text="Internet").grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.internet_label = ttk.Label(info, text="-")
        self.internet_label.grid(
            row=3,
            column=1,
            sticky="w"
        )

        ttk.Button(
            frame,
            text="Refresh",
            command=self.refresh
        ).pack(pady=15)

        log_frame = ttk.LabelFrame(
            frame,
            text="Status"
        )

        log_frame.pack(fill="both", expand=True)

        self.log = tk.Text(
            log_frame,
            height=10
        )

        self.log.pack(
            fill="both",
            expand=True
        )

    def refresh(self):

        threading.Thread(
            target=self._load,
            daemon=True
        ).start()

    def _load(self):

        hostname = socket.gethostname()

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()

        except Exception:

            local_ip = "Unavailable"

        try:

            public_ip = requests.get(
                "https://api.ipify.org",
                timeout=5
            ).text

            internet = "Connected"

        except Exception:

            public_ip = "Unavailable"
            internet = "Disconnected"

        self.window.after(
            0,
            lambda: self._update(
                hostname,
                local_ip,
                public_ip,
                internet
            )
        )

    def _update(
        self,
        hostname,
        local_ip,
        public_ip,
        internet
    ):

        self.hostname_label.config(text=hostname)
        self.local_ip_label.config(text=local_ip)
        self.public_ip_label.config(text=public_ip)
        self.internet_label.config(text=internet)

        self.log.delete("1.0", tk.END)

        self.log.insert(
            tk.END,
            f"Hostname : {hostname}\n"
        )

        self.log.insert(
            tk.END,
            f"Local IP : {local_ip}\n"
        )

        self.log.insert(
            tk.END,
            f"Public IP : {public_ip}\n"
        )

        self.log.insert(
            tk.END,
            f"Status : {internet}\n"
        )