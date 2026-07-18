"""
WW-P Security Platform

Security Center
Version: 1.0.3
"""

import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

from applications.base_app import BaseApp

from security.nmap_scanner import NmapScanner
from security.port_scanner import PortScanner
from security.shodan import ShodanLauncher


class SecurityApp(BaseApp):

    TITLE = "Security Center"

    WIDTH = 900
    HEIGHT = 650

    def __init__(self):

        super().__init__()

        self.nmap = NmapScanner()
        self.port_scanner = PortScanner()

    ###########################################################
    # GUI
    ###########################################################

    def build(self):

        notebook = ttk.Notebook(self.window)

        notebook.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        ########################################################
        # NMAP
        ########################################################

        self.nmap_frame = ttk.Frame(notebook)

        notebook.add(
            self.nmap_frame,
            text="Nmap Scanner"
        )

        self.create_nmap_tab()

        ########################################################
        # TCP
        ########################################################

        self.tcp_frame = ttk.Frame(notebook)

        notebook.add(
            self.tcp_frame,
            text="TCP Scanner"
        )

        self.create_tcp_tab()

        ########################################################
        # TOOLS
        ########################################################

        self.tools_frame = ttk.Frame(notebook)

        notebook.add(
            self.tools_frame,
            text="Security Tools"
        )

        self.create_tools_tab()

    ###########################################################
    # NMAP TAB
    ###########################################################

    def create_nmap_tab(self):

        top = ttk.Frame(self.nmap_frame)

        top.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )

        ttk.Label(
            top,
            text="Host:"
        ).grid(row=0, column=0, sticky="w")

        self.host_entry = ttk.Entry(
            top,
            width=25
        )

        self.host_entry.insert(
            0,
            "127.0.0.1"
        )

        self.host_entry.grid(
            row=0,
            column=1,
            padx=5
        )

        ttk.Label(
            top,
            text="Start port:"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.start_port = ttk.Entry(
            top,
            width=8
        )

        self.start_port.insert(
            0,
            "1"
        )

        self.start_port.grid(
            row=0,
            column=3
        )

        ttk.Label(
            top,
            text="End port:"
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        self.end_port = ttk.Entry(
            top,
            width=8
        )

        self.end_port.insert(
            0,
            "1024"
        )

        self.end_port.grid(
            row=0,
            column=5
        )

        ttk.Button(

            top,

            text="Run Scan",

            command=self.run_nmap_scan

        ).grid(

            row=0,

            column=6,

            padx=10

        )

        self.output = scrolledtext.ScrolledText(

            self.nmap_frame,

            wrap=tk.WORD,

            font=("Consolas", 10)

        )

        self.output.pack(

            fill=tk.BOTH,

            expand=True,

            padx=10,

            pady=10

        )

    ###########################################################
    # TCP TAB
    ###########################################################

    def create_tcp_tab(self):

        frame = ttk.Frame(self.tcp_frame)

        frame.pack(

            pady=20

        )

        ttk.Label(

            frame,

            text="Host"

        ).grid(

            row=0,

            column=0

        )

        self.tcp_host = ttk.Entry(

            frame,

            width=20

        )

        self.tcp_host.insert(

            0,

            "127.0.0.1"

        )

        self.tcp_host.grid(

            row=0,

            column=1,

            padx=5

        )

        ttk.Label(

            frame,

            text="Port"

        ).grid(

            row=0,

            column=2,

            padx=5

        )

        self.tcp_port = ttk.Entry(

            frame,

            width=8

        )

        self.tcp_port.insert(

            0,

            "80"

        )

        self.tcp_port.grid(

            row=0,

            column=3

        )

        ttk.Button(

            frame,

            text="Check",

            command=self.run_tcp_scan

        ).grid(

            row=0,

            column=4,

            padx=10

        )

        self.tcp_result = ttk.Label(

            self.tcp_frame,

            text=""

        )

        self.tcp_result.pack(

            pady=20

        )

    ###########################################################
    # TOOLS TAB
    ###########################################################

    def create_tools_tab(self):

        ttk.Button(

            self.tools_frame,

            text="Open Shodan",

            width=25,

            command=ShodanLauncher.open

        ).pack(

            pady=30

        )

    ###########################################################
    # EVENTS
    ###########################################################

    def run_nmap_scan(self):

        thread = threading.Thread(

            target=self._scan_thread,

            daemon=True

        )

        thread.start()

    def _scan_thread(self):

        host = self.host_entry.get()

        try:

            start = int(

                self.start_port.get()

            )

            end = int(

                self.end_port.get()

            )

        except ValueError:

            self.window.after(

                0,

                lambda:

                messagebox.showerror(

                    "Error",

                    "Ports must be integers."

                )

            )

            return

        try:

            results = self.nmap.scan(

                host,

                start,

                end

            )

            self.window.after(

                0,

                lambda:

                self.show_results(

                    results

                )

            )

        except Exception as e:

            self.window.after(

                0,

                lambda:

                messagebox.showerror(

                    "Nmap",

                    str(e)

                )

            )

    ###########################################################

    def show_results(self, results):

        self.output.delete(

            "1.0",

            tk.END

        )

        if not results:

            self.output.insert(

                tk.END,

                "No open ports found."

            )

            return

        for item in results:

            self.output.insert(

                tk.END,

                f"[{item['protocol'].upper()}] "

                f"{item['port']:>5} "

                f"{item['service']}\n"

            )

            if item["description"]:

                self.output.insert(

                    tk.END,

                    f"    {item['description']}\n"

                )

            if item["banner"]:

                self.output.insert(

                    tk.END,

                    f"    Banner: {item['banner']}\n"

                )

            self.output.insert(

                tk.END,

                "\n"

            )

    ###########################################################

    def run_tcp_scan(self):

        host = self.tcp_host.get()

        try:

            port = int(

                self.tcp_port.get()

            )

        except ValueError:

            messagebox.showerror(

                "Error",

                "Invalid port."

            )

            return

        opened = self.port_scanner.scan_port(

            host,

            port

        )

        if opened:

            self.tcp_result.config(

                text="Port OPEN",

                foreground="green"

            )

        else:

            self.tcp_result.config(

                text="Port CLOSED",

                foreground="red"

            )