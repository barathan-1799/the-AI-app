import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMW data", page_icon=":)")
st.title("Analyzing the performance of different BMW models")
st.write(
    """
    This app is for analyzing the performance figures of various BMW models!
    """
)

# Load the data from the Excel file. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("/PCA_BMW_dataset.csv")
    return df


df = load_data()

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df,
    use_container_width=True
)
