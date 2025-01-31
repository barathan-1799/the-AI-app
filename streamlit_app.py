import streamlit as st

st.set_page_config(page_title="BMW data", page_icon=":)")
st.title("My Streamlit app")
st.write(
    """
    This app is for analyzing BMW performance figures!
    """
)

# Load the data from the Excel file. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_excel("PCA_BMW_dataset")
    return df


df = load_data()

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df,
    use_container_width=True
)
