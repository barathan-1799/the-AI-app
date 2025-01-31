# Step 1: Importing dependencies
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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
    
    # Renaming the first column title of the dataframe to "Model"
    if df.columns[0] != "Model":
        df = df.rename(columns = {df.columns[0]: "Model"})
        
    return df

# Step 4: Executing the function to load data from csv file
df = load_data()

# Step 5: Displaying the data as a table using `st.dataframe`.
st.dataframe(
    df,
    use_container_width=True
)

# Step 6: Label encoding: 0 = Non-M-Performance model, 1 = M-Performance model
# Creating a list of all models
model_list = list(df["Model"])
label_M = 1
label_non_M = 0
encoded_label_list = []

for index, model in enumerate(model_list):
  if model[4] != "M":
    encoded_label_list.append(label_non_M)
  
  else:
    encoded_label_list.append(label_M)

# Step 7: Revising the original labels to the encoded labels in the DataFrame
df["Model"] = pd.DataFrame(encoded_label_list)

# Step 8: Extracting the Features of the data
x = np.array(df.iloc[:,1:])

# Step 9: Scaling the Features of the data
s = StandardScaler().fit(x)
x_scaled = s.transform(x)

# Step 10: Defining a function that performs PCA using the Features data
def perform_pca(x_data, n_components):
  pca = PCA(n_components = n_components)
  fit_pca = pca.fit(x_data)
  print("Variance explained with {0} components:".format(n_components),
        round(sum(fit_pca.explained_variance_ratio_), 2))

  return fit_pca, fit_pca.transform(x_data)

# Step 11: Executing PCA for 2 principal components (PCs)
fit_pca, pc_list = perform_pca(x_scaled, 2)

# Step 12: Determining the variance explained by each PC
variance_ratios = fit_pca.explained_variance_ratio_

# Step 13: Visualizing the PCA outcome
# Convert y to a numpy array if it's a list (optional)
y = encoded_label_list
y = np.array(y)

# Find the unique labels
unique_labels = np.unique(y)

plt.figure(figsize=(6, 6))

# Plot each label's subset with a separate scatter call
for label in unique_labels:
    # Mask or boolean index for the current label
    indices = (y == label)
    plt.scatter(pc_list[indices, 0],
                pc_list[indices, 1],
                label=str(label),  # Convert label to string if needed
                alpha=0.7)
    
plt.xlabel(f"PC 1 ({variance_ratios[0]*100:.0f}% var)")
plt.ylabel(f"PC 2 ({variance_ratios[1]*100:.0f}% var)")
plt.title('PCA Scatter Plot with Discrete Legend')
plt.legend()  # Shows legend with each label
plt.show()
