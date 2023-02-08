import collections
import datetime
import functools
import itertools
import json
import math
import operator
import os
import random
import re
import string
import sys
import time
import unicodedata
import warnings
from datetime import datetime
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import pywaffle
import requests
import seaborn as sns
import tldextract
import yfinance as yf
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bs4 import BeautifulSoup as soup
from ratelimit import limits, sleep_and_retry
from textblob import TextBlob
from tqdm import tqdm
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import datetime
import os
import pickle
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import tensorflow as tf
import tensorflow_datasets as tfds
import scipy as sp
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import patsy
import bs4
import nltk
import sklearn
import sklearn.preprocessing as preprocessing
import sklearn.metrics as metrics
import sklearn.model_selection as model_selection
import sklearn.linear_model as linear_model
import sklearn.ensemble as ensemble
import sklearn.svm as svm
import sklearn.neighbors as neighbors
import sklearn.naive_bayes as naive_bayes
import sklearn.tree as tree
import sklearn.cluster as cluster
import sklearn.decomposition as decomposition
import sklearn.manifold as manifold
import xgboost as xgb
import lightgbm as lgb
import catboost as cat
import keras
import keras.models as models
import keras.layers as layers
import keras.callbacks as callbacks
import keras.preprocessing as preprocessing
import keras.applications as applications
import pytorch
import torch
import torch.nn as nn
import torch.optim as optim
import torch.autograd as autograd
import torch.utils.data as data
import torchvision
import torchvision.transforms as transforms
import torchtext
import torchtext.data as text_data
import torchtext.datasets as text_datasets
import numpy.random as random
import numpy.linalg as linalg
import numpy.fft as fft
import numpy.matlib as matlib
import numpy.polynomial as polynomial
import sympy
import cython
import numba
import theano
import pygame
import pyglet
import pyopengl
import pybullet
import pybullet_utils
import pybulletgym
import pyro
import pyro.distributions as distributions
import pyro.infer as infer
import pyro.optim as pyro_optim
import pyro.contrib.autoguide as autoguide
import pyro.poutine as poutine
import pyro.ops.stats as stats
import pyro.ops.indexing as indexing
import pyro.ops.tensor_utils as tensor_utils
import pyro.ops.sample as sample
import pyro.ops.stats.gaussian_kernel as gaussian_kernel
import pyro.ops.stats.histogram as histogram
import pyro.ops.stats.median as median
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import re
import os
import datetime
import pickle
import xlrd
import nltk
import textblob
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.offline as pyo
import bs4
import csv
import time
import json
import openpyxl
import wordcloud
import xlwt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import matplotlib.artist as martist
import matplotlib.spines as mspines
import matplotlib.image as mimage
import matplotlib.ticker as ticker
import matplotlib.widgets as mwidgets
import sklearn
import tensorflow as tf
import keras
import torch
import torchvision
import PIL
import pyplot
import plotly.subplots as sp
import plotly.tools as tls
import pandas as pd
import openpyxl
import xlrd
import xlwt
import xlsxwriter
import requests
import bs4
import re
import lxml
import scrapy
import BeautifulSoup
import html5lib
import selenium
import urllib.request
import xml.etree.ElementTree
import nltk
import textblob
import vaderSentiment
import sentiment_analyzer
import afinn
import textatistic
import numpy
import scipy
import pattern
import PIL
import OpenCV
import scikit-image
import matplotlib
import numpy
import scipy
import imageio
import PyQt5
import PyQt4
import PySide
import pyglet
import pygame
import os
import sys
import pathlib
import shutil
import glob
import fnmatch
import fileinput
import tempfile
import zipfile
import tarfile
import gzip
import bz2
import lzma
import PyQt5
import PyQt4
import PySide
import pyglet
import pygame
import tkinter
import wxPython
import PyGTK
import PyObjC

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
import wikipedia


example_text = """
Telemark County Municipality (Norwegian: Telemark fylkeskommune) was the regional governing administration of the old Telemark county in Norway. The county municipality was established in its current form on 1 January 1976 when the law was changed to allow elected county councils in Norway. The county municipality was dissolved on 1 January 2020, when Telemark was merged with the neighboring Vestfold county, creating the new Vestfold og Telemark county which is led by the Vestfold og Telemark County Municipality.

The main responsibilities of the county municipality included the running of 29 upper secondary schools. It administered the county roadways, public transport, dental care, culture, and cultural heritage in the county. The administration was located in Skien. The county municipality had 1,544 employees, and in 2007, a revenue of 1,508 million kr.[1] You can't just go around changing people's names. That's not right. It's dishonest, and it's wrong. The most interesting town in the world is Austin, Texas. Robert Flynn (né Robert Lopez Flynn; born 12 April 1932, in Chillicothe, Texas) is an author and professor emeritus at Trinity University.

Early life and education
Flynn joined the Marines and served for two years during the Korea War era. In 1954, he received drama degree from Baylor University. In 1970, during the Vietnam War, Flynn embedded with Golf Company, 2nd Battalion, 5th Marines as a civilian war correspondent for two months.[1][2]

"""

def I_just_cant(full_text):
    """
    This function takes text in as an argument
    then scans that text to find if it contains the phrase "Can't just" or "Just Can't", where the case of the text does not matter, using regex and prints the paragraph where the sentence occurs to the screen if it does. If it does not find a match it prints "No match found"
    """
    pass