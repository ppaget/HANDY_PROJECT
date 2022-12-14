import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import requests, os
from gwpy.timeseries import TimeSeries
from gwosc.locate import get_urls
from gwosc import datasets
from gwosc.api import fetch_event_json

from copy import deepcopy
import base64

from helper import make_audio_file

mpl.use("agg")

from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock


# -- Set page config
apptitle = 'GW Quickview'

st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']

# Title the app
st.title('Gravitational Wave Quickview')

st.markdown("""
 * Use the menu at left to select data and set plot parameters
 * Your plots will appear below
""")

