"""
applications/pca_analyzer.py

WW-P Security Platform
PCA Analyzer Module

Features:
- Multiple CSV/TXT file loading
- Background loading thread
- Data merging
- StandardScaler normalization
- PCA analysis
- PC1/PC2 visualization
- CSV export

Based on previous WW-P projects
"""


import tkinter as tk
from tkinter import filedialog, messagebox

#import threading

import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class PCAAnalyzer:


    def __init__(self):

        self.window = None

        self.datasets = []

        self.data = None

        self.result = None

        self.file_paths = []

    def load_next_file(self):

        if self.current_index >= len(self.current_files):
            self.status.config(
                text=
                f"Loaded {len(self.datasets)} files"
            )

            self.data = pd.concat(
                self.datasets,
                ignore_index=True
            )

            self.status.config(
                text=
                f"Ready. Rows: {len(self.data)}"
            )

            return

        path = self.current_files[self.current_index]

        self.status.config(
            text=
            f"Loading {self.current_index + 1}/"
            f"{len(self.current_files)}"
        )

        try:

            if path.lower().endswith(".csv"):

                df = pd.read_csv(path)


            else:

                df = pd.read_csv(
                    path,
                    delimiter="\t"
                )

            df["SOURCE_FILE"] = (
                path.split("/")[-1]
            )

            self.datasets.append(df)

            self.current_index += 1

            self.window.after(
                50,
                self.load_next_file
            )


        except Exception as error:

            messagebox.showerror(
                "Loading error",
                str(error)
            )

    # ==================================================
    # Open application
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


        #self.create_gui()



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



        tk.Button(

            toolbar,

            text="Clear",

            command=self.clear_data

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
    # Load files
    # ==================================================

    def load_file(self):


        paths = filedialog.askopenfilenames(

            title="Select CSV/TXT files",

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

        print("Selected files:")
        for p in paths:
            print(p)



        self.datasets.clear()

        self.file_paths.clear()

        self.data = None

        self.result = None



        self.status.config(

            text="Starting loading..."

        )

        self.current_files = list(paths)
        self.current_index = 0

        self.load_next_file()

        # thread = threading.Thread(
        #
        #     target=self._load_files_thread,
        #
        #     args=(paths,),
        #
        #     daemon=True
        #
        # )
        #
        #
        # thread.start()




    def _load_files_thread(self, paths):


        try:


            loaded = 0



            for index, path in enumerate(paths, start=1):


                self.status.config(

                    text=
                    f"Loading {index}/{len(paths)}"

                )



                if path.lower().endswith(".csv"):


                    df = pd.read_csv(

                        path

                    )


                else:


                    df = pd.read_csv(

                        path,

                        delimiter="\t"

                    )



                df["SOURCE_FILE"] = (

                    path.split("/")[-1]

                )



                self.datasets.append(df)

                self.file_paths.append(path)


                loaded += 1




            self.status.config(

                text="Joining datasets..."

            )



            self.data = pd.concat(

                self.datasets,

                ignore_index=True

            )



            self.status.config(

                text=
                f"Loaded {loaded} files. "
                f"Rows: {len(self.data)}"

            )



        except Exception as error:


            messagebox.showerror(

                "Loading error",

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


            self.status.config(

                text="Preparing PCA..."

            )


            self.window.update_idletasks()



            numeric_data = (

                self.data

                .drop(

                    columns=[

                        "SOURCE_FILE"

                    ],

                    errors="ignore"

                )

                .select_dtypes(

                    include=np.number

                )

            )



            if numeric_data.empty:


                raise ValueError(

                    "No numeric columns found."

                )



            scaler = StandardScaler()



            scaled = scaler.fit_transform(

                numeric_data

            )



            components_count = min(

                2,

                scaled.shape[1]

            )



            self.status.config(

                text="Running PCA..."

            )


            self.window.update_idletasks()



            pca = PCA(

                n_components=components_count

            )



            components = pca.fit_transform(

                scaled

            )



            columns = [

                f"PC{i+1}"

                for i in range(components_count)

            ]



            self.result = pd.DataFrame(

                components,

                columns=columns

            )



            if "SOURCE_FILE" in self.data.columns:


                self.result["SOURCE_FILE"] = (

                    self.data["SOURCE_FILE"]

                    .values

                )



            for i, value in enumerate(

                pca.explained_variance_ratio_

            ):

                self.result[

                    f"Explained_PC{i+1}"

                ] = value




            self.draw_plot()



            self.status.config(

                text="PCA completed"

            )



        except Exception as error:


            messagebox.showerror(

                "PCA error",

                str(error)

            )





    # ==================================================
    # Plot
    # ==================================================

    def draw_plot(self):


        for widget in self.plot_frame.winfo_children():

            widget.destroy()



        fig, ax = plt.subplots(

            figsize=(7,5)

        )



        if "PC2" in self.result.columns:


            ax.scatter(

                self.result["PC1"],

                self.result["PC2"]

            )


            ax.set_xlabel(

                "PC1"

            )


            ax.set_ylabel(

                "PC2"

            )



        else:


            ax.scatter(

                range(len(self.result)),

                self.result["PC1"]

            )


            ax.set_xlabel(

                "Samples"

            )


            ax.set_ylabel(

                "PC1"

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
    # Save
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





    # ==================================================
    # Clear
    # ==================================================

    def clear_data(self):


        self.datasets.clear()

        self.file_paths.clear()

        self.data = None

        self.result = None



        for widget in self.plot_frame.winfo_children():

            widget.destroy()



        self.status.config(

            text="Data cleared"

        )