"""
PCA Analyzer
"""

import numpy as np

import matplotlib.pyplot as plt

from scipy import linalg

from sklearn.feature_extraction.text import TfidfVectorizer


class PCAAnalyzer:

    @staticmethod
    def pca(matrix, n_components):

        mean = np.mean(matrix, axis=0)

        centered = matrix - mean

        cov = np.cov(centered, rowvar=False)

        eigval, eigvec = linalg.eig(cov)

        pairs = [

            (np.abs(eigval[i]), eigvec[:, i])

            for i in range(len(eigval))

        ]

        pairs.sort(

            reverse=True,

            key=lambda x: x[0]

        )

        W = np.hstack(

            [

                pairs[i][1].reshape(-1,1)

                for i in range(n_components)

            ]

        ).real

        return centered.dot(W)

    @staticmethod
    def run(documents):

        vectorizer = TfidfVectorizer()

        X = vectorizer.fit_transform(

            documents

        ).toarray()

        reduced = PCAAnalyzer.pca(

            X,

            2

        )

        plt.scatter(

            reduced[:,0],

            reduced[:,1]

        )

        plt.title(

            "PCA"

        )

        plt.show()