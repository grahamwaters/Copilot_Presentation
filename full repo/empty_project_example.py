# Basic Libraries
import collections, datetime, functools, itertools, json, math, operator, os, random, re, string, sys, time, unicodedata, warnings
from datetime import datetime

# Data Visualization
import matplotlib.pyplot as plt, numpy as np, pyplot, pywaffle, seaborn as sns
import bokeh.io as bkio, bokeh.models as bkmd, bokeh.palettes as bkpl, bokeh.plotting as bkpt, bokeh.transform as bktr
import plotly.express as px, plotly.graph_objs as go

# Data Storage and Analysis
import nltk, pandas as pd

# Excel Files
import openpyxl, xlrd, xlwt, xlsxwriter

# Text Analysis
import textblob, vaderSentiment, sentiment_analyzer, afinn, textatistic

# Web Scraping and Requests
import requests, bs4, tldextract

# Financial Data
import yfinance as yf

# Rate Limiting
from ratelimit import limits, sleep_and_retry

# Machine Learning
import catboost as cat, keras, lightgbm as lgb, numpy.linalg as linalg, scipy, scipy.stats as stats, sklearn, statsmodels.api as sm, statsmodels.formula.api as smf, xgboost as xgb
import keras.callbacks as krcb, keras.layers as krly, keras.models as krmd, keras.preprocessing as krpp
import patsy, sklearn.cluster as skc, sklearn.decomposition as skd, sklearn.ensemble as ske, sklearn.linear_model as sklm, sklearn.manifold as skm, sklearn.metrics as skmtr, sklearn.model_selection as skms, sklearn.naive_bayes as sknb, sklearn.neighbors as skn, sklearn.preprocessing as skpp, sklearn.svm as sksvm, sklearn.tree as skt
import tensorflow as tf, tensorflow_datasets as tfds

# Deep Learning
import keras.applications as kra, torch, torch.autograd as tat, torch.nn as tnn, torch.optim as top, torch.utils.data as tud, torchvision, torchvision.transforms as tvt
import torchtext, torchtext.data as ttd, torchtext.datasets as ttds

# Stochastic Libraries
import numpy.fft as nfft, numpy.matlib as nmlib, numpy.polynomial as npoly, numpy.random as npr, pyro, sympy
import pyro.contrib.autoguide as pyca, pyro.distributions as pyd, pyro.infer as pyi, pyro.optim as pyop, pyro.poutine as pyp
import pyro.ops.indexing as pyi, pyro.ops.sample as pys, pyro.ops.stats as pys, pyro.ops.stats.gaussian_kernel as pysgk, pyro.ops.stats.histogram as pysh, pyro.ops.stats.median as pysm, pyro.ops

# Natural Language Processing
import gensim, nltk, spacy, textblob, vaderSentiment, sentiment_analyzer, afinn, textatistic

# Image Processing
import cv2, imageio, matplotlib.image as mpimg, matplotlib.pyplot as plt, numpy as np, PIL, PIL.Image as Image, PIL.ImageDraw as ImageDraw, PIL.ImageFont as ImageFont, PIL.ImageOps as ImageOps, scipy, scipy.ndimage as ndimage, skimage, skimage.color as skc, skimage.feature as skf, skimage.filters as skfi, skimage.io as skio, skimage.measure as skm, skimage.morphology as skmo, skimage.transform as skt, skimage.util as sku

# Audio Processing
import librosa, librosa.display, matplotlib.pyplot as plt, numpy as np, scipy, scipy.io.wavfile as wav, scipy.signal as sig, soundfile as sf, sounddevice as sd

# Video Processing
import cv2, imageio, matplotlib.pyplot as plt, numpy as np, PIL, PIL.Image as Image, PIL.ImageDraw as ImageDraw, PIL.ImageFont as ImageFont, PIL.ImageOps as ImageOps, scipy, scipy.ndimage as ndimage, skimage, skimage.color as skc, skimage.feature as skf, skimage.filters as skfi, skimage.io as skio, skimage.measure as skm, skimage.morphology as skmo, skimage.transform as skt, skimage.util as sku



# ─── The Prompt ───────────────────────────────────────────────────────────────
"""
Instructions for GitHub Copilot:
    Write a function that reads an XLSX file and returns dataframes where each sheet is a dataframe, each column of each df should be type-cast based on the values from the corresponding sheet in the second row, and the column names are in the first row. The function should save these dataframes in a folder called `extracted_dfs` with each sheet in its own folder named after the sheet's name in the file. Within these folders, the function should save the dataframe as a pickle file. The function should return a dictionary with the sheet names as keys and the dataframe information as values.
"""

# ─── The Code ─────────────────────────────────────────────────────────────────
def read_xlsx(file_path):
    # Read in the file
    with pd.ExcelFile(file_path) as xlsx:
        # Get the sheet names
        sheet_names = xlsx.sheet_names

        # Create an empty dictionary to store the dataframes
        dfs = {}

        # Iterate through the sheets
        for sheet in sheet_names:
            # Get the dataframe from the sheet
            df = pd.read_excel(xlsx, sheet_name=sheet)

            # Get the second row of the dataframe
            second_row = df.iloc[1]

            # Get the first row of the dataframe
            first_row = df.iloc[0]

            # Get the column names from the first row
            df.columns = first_row

            # Drop the first two rows
            df = df.iloc[2:]

            # Iterate through the columns in the second row
            for col in second_row.index:
                # Get the type of the value in the second row
                col_type = type(second_row[col])

                # Cast the column to the type of the second row value
                df[col] = df[col].astype(col_type)

            # Create a folder for the sheet
            os.makedirs(f"extracted_dfs/{sheet}", exist_ok=True)

            # Save the dataframe as a pickle file in the sheet folder
            df.to_pickle(f"extracted_dfs/{sheet}/{sheet}.pkl")

            # Add the dataframe to the dictionary
            dfs[sheet] = df

    # Return the dictionary
    return dfs