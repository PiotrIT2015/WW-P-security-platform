"""
applications/web_app.py

WW-P Security Platform
White Dwarf Search
v1.0
"""

import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext

import requests
from bs4 import BeautifulSoup

from textblob import TextBlob


class WebApp:

    def __init__(self):

        self.window = None

    # --------------------------------------------------

    def open(self, root):

        if self.window and self.window.winfo_exists():

            self.window.lift()
            return

        self.window = tk.Toplevel(root)

        self.window.title("White Dwarf Search")

        self.window.geometry("900x650")

        self.create_widgets()

    # --------------------------------------------------

    def create_widgets(self):

        frame = ttk.Frame(self.window, padding=10)

        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            frame,
            text="Adres strony:"
        ).pack(anchor="w")

        self.url_entry = ttk.Entry(frame)

        self.url_entry.pack(fill=tk.X, pady=5)

        self.url_entry.insert(
            0,
            "https://www.wikipedia.org"
        )

        ttk.Label(
            frame,
            text="Szukana fraza:"
        ).pack(anchor="w")

        self.query_entry = ttk.Entry(frame)

        self.query_entry.pack(fill=tk.X, pady=5)

        self.query_entry.insert(
            0,
            "Python"
        )

        button_frame = ttk.Frame(frame)

        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(

            button_frame,

            text="Szukaj",

            command=self.search

        ).pack(side=tk.LEFT)

        ttk.Button(

            button_frame,

            text="Wyczyść",

            command=self.clear

        ).pack(side=tk.LEFT, padx=5)

        self.sentiment_label = ttk.Label(

            button_frame,

            text="Sentyment: -"

        )

        self.sentiment_label.pack(side=tk.RIGHT)

        self.output = scrolledtext.ScrolledText(

            frame,

            wrap=tk.WORD

        )

        self.output.pack(

            fill=tk.BOTH,

            expand=True

        )

    # --------------------------------------------------

    def clear(self):

        self.output.delete("1.0", tk.END)

        self.sentiment_label.config(

            text="Sentyment: -"

        )

    # --------------------------------------------------

    def search(self):

        url = self.url_entry.get().strip()

        query = self.query_entry.get().strip()

        if not url:

            messagebox.showwarning(

                "Błąd",

                "Podaj adres URL."

            )

            return

        if not query:

            messagebox.showwarning(

                "Błąd",

                "Podaj szukaną frazę."

            )

            return

        self.output.delete(

            "1.0",

            tk.END

        )

        self.output.insert(

            tk.END,

            "Pobieranie strony...\n"

        )

        threading.Thread(

            target=self.perform_search,

            args=(url, query),

            daemon=True

        ).start()

    # --------------------------------------------------

    def perform_search(self, url, query):

        try:

            headers = {

                "User-Agent":
                "Mozilla/5.0"

            }

            response = requests.get(

                url,

                timeout=15,

                headers=headers

            )

            response.raise_for_status()

            soup = BeautifulSoup(

                response.text,

                "html.parser"

            )

            paragraphs = soup.find_all("p")

            results = []

            for paragraph in paragraphs:

                text = paragraph.get_text(

                    strip=True

                )

                if query.lower() in text.lower():

                    results.append(text)

            if not results:

                result_text = "Nie znaleziono wyników."

            else:

                result_text = "\n\n".join(results)

            sentiment = self.analyze_sentiment(

                result_text

            )

            self.window.after(

                0,

                lambda: self.update_gui(

                    result_text,

                    sentiment

                )

            )

        except Exception as e:

            self.window.after(

                0,

                lambda: messagebox.showerror(

                    "Błąd",

                    str(e)

                )

            )

    # --------------------------------------------------

    def analyze_sentiment(self, text):

        if not text:

            return "Neutralny"

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.2:

            return "Pozytywny"

        elif polarity < -0.2:

            return "Negatywny"

        return "Neutralny"

    # --------------------------------------------------

    def update_gui(self, text, sentiment):

        self.output.delete(

            "1.0",

            tk.END

        )

        self.output.insert(

            tk.END,

            text

        )

        self.sentiment_label.config(

            text=f"Sentyment: {sentiment}"

        )

    def open_shodan(self, root):

        self.open(root)

        self.url_entry.insert(
            0,
            "https://www.shodan.io"
        )