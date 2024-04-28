import os

import pandas as pd
import streamlit as st

sales_filepath = os.environ.get(
    "SALES_FILEPATH", default="21.streamlit_and_gradio/examples/streamlit/sales.csv"
)

df = pd.read_csv("streamlit/sales.csv")

st.dataframe(df)
