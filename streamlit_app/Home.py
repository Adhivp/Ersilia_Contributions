import streamlit as st
import pandas as pd
from repo_path import repo_path
import os

st.title("hERG Blocker Classification Model(eos30gr)")
st.write("Welcome to the hERG Blocker Classification Model. This model predicts the probability that a molecule is a hERG blocker.")

st.header("Model Characteristics")
st.markdown("""
- **Input:** Compound
- **Task:** Classification
- **Output:** Probability
- **Interpretation:** Probability of hERG blockade. The training dataset used a threshold of 80% inhibition to define hERG blockers.
""")


st.header("Model Testing Information (My Contribution)")
st.markdown("""
As per the guidance form the mentor ,I have tested the model. One dataset was used to identify model bias, and the other two were used to check reproducibility.
""")
st.success("Explore the tables below to see the datasets used for testing:")


st.header("Datasets")
st.write("Below are the datasets used for testing the model:")
repo_path = repo_path()

st.subheader("Dataset 1: Model Bias (Reference Libary)")
reference_library_path = os.path.join(repo_path,'data/reference_library.csv')
reference_library = pd.read_csv(reference_library_path)
st.write(reference_library)



st.subheader("Dataset 2: Reproducibility Test 1(Table S7)")
table_S7_path = os.path.join(repo_path, 'data/eos30gr/Table S7.xlsx')
table_S7 = pd.read_excel(table_S7_path, skiprows=1)
st.write(table_S7)



st.subheader("Dataset 3: Reproducibility Test 2 (Table S6)")
table_S6_path = os.path.join(repo_path, 'data/eos30gr/Table S6.xlsx')
table_S6 = pd.read_excel(table_S6_path, skiprows=1)
st.write(table_S6)

st.subheader("Dataset 4: External dataset Model evaluation (external_dataset_1287_random.csv)")
external_dataset_1287_random_path = os.path.join(repo_path, 'data/eos30gr/external_dataset_1287_random.csv')
external_dataset_1287_random = pd.read_csv(external_dataset_1287_random_path)
external_dataset_1287_random = external_dataset_1287_random.rename(columns={'class': 'Experimental_value'})
external_dataset_1287_random = external_dataset_1287_random[['Standardised_smiles','Inchikey','Experimental_value']]
st.write(external_dataset_1287_random)

