"""
applications/pca_analyzer.py

WW-P Security Platform
PCA Analyzer Module

Based on previous WW-P projects
"""

import tkinter as tk
from tkinter import filedialog, messagebox

import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class PCAAnalyzer:
    """
    Analiza głównych składowych PCA.

    Obsługiwane:
    - CSV
    - TXT
    - normalizacja danych
    - PCA
    - wykres PC1/PC2
    - eksport wyników
    """


    def __init__(self):

        self.window = None

        self.data = None

        self.result = None

        self.file_path = None



    # ==================================================
    # Otwarcie aplikacji
    # ==================================================

    def open(self, root):

        self.window = tk.Toplevel(root)

        self.window.title(
            "WW-P PCA Analyzer"
        )

        self.window.geometry(
            "900x650"
        )

        self.window.configure(
            bg="#20242b"
        )


        self.create_gui()



    # ==================================================
    # GUI
    # ==================================================

    def create_gui(self):


        title = tk.Label(
            self.window,
            text="Principal Component Analysis Analyzer",
            font=(
                "Segoe UI",
                18,
                "bold"
            ),
            fg="white",
            bg="#20242b"
        )

        title.pack(
            pady=10
        )


        toolbar = tk.Frame(
            self.window,
            bg="#20242b"
        )

        toolbar.pack(
            fill=tk.X
        )


        tk.Button(
            toolbar,
            text="Load CSV/TXT",
            command=self.load_file
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            toolbar,
            text="Run PCA",
            command=self.run_pca
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        tk.Button(
            toolbar,
            text="Save Result",
            command=self.save_result
        ).pack(
            side=tk.LEFT,
            padx=5
        )


        self.status = tk.Label(
            self.window,
            text="Ready",
            fg="#7fd6ff",
            bg="#20242b"
        )

        self.status.pack(
            pady=5
        )


        self.plot_frame = tk.Frame(
            self.window,
            bg="white"
        )

        self.plot_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )



    # ==================================================
    # Wczytywanie danych
    # ==================================================

    def load_file(self):

        path = filedialog.askopenfilename(

            filetypes=[

                (
                    "CSV files",
                    "*.csv"
                ),

                (
                    "Text files",
                    "*.txt"
                )

            ]

        )


        if not path:
            return


        try:

            if path.endswith(".csv"):

                self.data = pd.read_csv(
                    path
                )

            else:

                self.data = pd.read_csv(
                    path,
                    delimiter="\t"
                )


            self.file_path = path


            self.status.config(
                text=
                f"Loaded: {path}"
            )


        except Exception as error:


            messagebox.showerror(
                "Load error",
                str(error)
            )



    # ==================================================
    # PCA
    # ==================================================

    def run_pca(self):

        if self.data is None:

            messagebox.showwarning(
                "PCA",
                "Load data first."
            )

            return



        try:

            numeric_data = (
                self.data
                .select_dtypes(
                    include=np.number
                )
            )


            if numeric_data.empty:

                raise ValueError(
                    "No numeric columns found"
                )



            scaler = StandardScaler()


            scaled = scaler.fit_transform(
                numeric_data
            )



            pca = PCA(
                n_components=2
            )


            components = pca.fit_transform(
                scaled
            )



            self.result = pd.DataFrame(

                components,

                columns=[
                    "PC1",
                    "PC2"
                ]

            )


            self.result["Explained_PC1"] = (
                pca.explained_variance_ratio_[0]
            )


            self.result["Explained_PC2"] = (
                pca.explained_variance_ratio_[1]
            )



            self.draw_plot()



            self.status.config(
                text=
                "PCA completed"
            )


        except Exception as error:


            messagebox.showerror(
                "PCA error",
                str(error)
            )



    # ==================================================
    # Wykres
    # ==================================================

    def draw_plot(self):


        for widget in self.plot_frame.winfo_children():

            widget.destroy()



        fig, ax = plt.subplots(
            figsize=(7,5)
        )


        ax.scatter(

            self.result["PC1"],

            self.result["PC2"]

        )


        ax.set_xlabel(
            "Principal Component 1"
        )

        ax.set_ylabel(
            "Principal Component 2"
        )

        ax.set_title(
            "PCA Projection"
        )



        canvas = FigureCanvasTkAgg(

            fig,

            master=self.plot_frame

        )


        canvas.draw()


        canvas.get_tk_widget().pack(

            fill=tk.BOTH,

            expand=True

        )



    # ==================================================
    # Eksport
    # ==================================================

    def save_result(self):


        if self.result is None:

            messagebox.showwarning(
                "Save",
                "Run PCA first."
            )

            return



        path = filedialog.asksaveasfilename(

            defaultextension=".csv",

            filetypes=[
                (
                    "CSV",
                    "*.csv"
                )
            ]

        )


        if path:

            self.result.to_csv(
                path,
                index=False
            )


            messagebox.showinfo(
                "Save",
                "PCA result saved."
            )