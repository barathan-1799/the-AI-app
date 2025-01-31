# Step 1: Importing dependencies
import streamlit as st
import pandas as pd

# Step 2: Setting app title and description
st.set_page_config(page_title="BMW data", page_icon=":)")
st.title("Analyzing the performance of different BMW models")
st.write(
    """
    This app is for analyzing the performance figures of various BMW models!
    """
)

# Step 3: Defining a function to load the data from the csv file. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("PCA_BMW_dataset.csv")
    return df

# Step 4: Executing the function to load data from csv file
df = load_data()

# Step 5: Renaming the first column title of the dataframe to "Model"
df = df.rename(columns = {df.columns[0]: "Model"})

# Step 6: Displaying the data as a table using `st.dataframe`.
st.dataframe(
    df,
    use_container_width=True
)
