import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from repo_path import repo_path

def load_table_S6(repo_path):
    table_S6_path = os.path.join(repo_path, 'data/eos30gr/Table S6.xlsx')
    table_S6 = pd.read_excel(table_S6_path, skiprows=1)
    return table_S6

def load_table_S6_predictions(repo_path):
    table_S6_output_from_local_model_eos30gr_path = os.path.join(repo_path, 'data/eos30gr/table_S6_eos30gr_output_google_collab.csv')
    table_S6_predictions = pd.read_csv(table_S6_output_from_local_model_eos30gr_path)
    return table_S6_predictions

def preprocess_table_S6_predictions(table_S6_predictions, table_S6):
    table_S6_predictions = pd.merge(table_S6_predictions, table_S6[['DrugBank ID','Name']], left_index=True, right_index=True)
    table_S6_predictions = table_S6_predictions[table_S6_predictions['input'] != 'CCCC']
    table_S6_predictions.drop(columns='key', inplace=True)
    table_S6_predictions.rename(columns={'activity10':'Predicted_positive_probability','input':'smiles'}, inplace=True)
    desired_columns_order = ['DrugBank ID','Name','smiles','Predicted_positive_probability']
    table_S6_predictions = table_S6_predictions[desired_columns_order]
    table_S6_predictions['Predicted_negative_probability'] = 1 - table_S6_predictions['Predicted_positive_probability']
    return table_S6_predictions

def plot_comparisons(table, table_predictions, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=table.index,
        y=table['Predicted positive probability'],
        mode='lines',
        name='Original Research data (Positive probability)',
        line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=table_predictions.index,
        y=table_predictions['Predicted_positive_probability'],
        mode='lines',
        name='Predicted positive data',
        line=dict(color='red')
    ))
    fig.update_layout(
        xaxis=dict(title='Index'),
        yaxis=dict(title='Probability'),
        title=title,
        legend=dict(x=0, y=1.0),
        height=600,
        width=800
    )
    return fig

def plot_comparisons_negative(table, table_predictions, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=table.index,
        y=table['Predicted negative probability'],
        mode='lines',
        name='Original Research data (Negative probability)',
        line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=table_predictions.index,
        y=table_predictions['Predicted_negative_probability'],
        mode='lines',
        name='Predicted negative data',
        line=dict(color='red')
    ))
    fig.update_layout(
        xaxis=dict(title='Index'),
        yaxis=dict(title='Probability'),
        title=title,
        legend=dict(x=0, y=1.0),
        height=600,
        width=800
    )
    return fig

def plot_venn_diagram(molecules_both_matching, molecules_first_only, molecules_second_only):
    fig = plt.figure(figsize=(10, 6))
    venn2(subsets=(len(molecules_first_only), len(molecules_second_only), len(molecules_both_matching)),
          set_labels=('Original Table S6', 'Predicted Table S6'))
    plt.title('Molecules above 0.5 Probability in Datasets')
    st.pyplot(fig)


repo_path = repo_path() 
table_S6 = load_table_S6(repo_path)


table_S6_predictions = load_table_S6_predictions(repo_path)

st.subheader("Predictions recieved from eos30gr model,it took approx 4 hours to get result(Google collab)")
st.write(table_S6_predictions)
table_S6_predictions = preprocess_table_S6_predictions(table_S6_predictions, table_S6)

downsample_factor = 20
table_S6_downsampled = table_S6.iloc[::downsample_factor]
table_S6_predictions_downsampled = table_S6_predictions.iloc[::downsample_factor]

fig_positive_S6 = plot_comparisons(table_S6_downsampled, table_S6_predictions_downsampled, 'Comparison of Research paper and predicted positive probability (Table S6)')
fig_negative_S6 = plot_comparisons_negative(table_S6_downsampled, table_S6_predictions_downsampled, 'Comparison of Research paper and predicted negative probability (Table S6)')

st.plotly_chart(fig_positive_S6)
st.plotly_chart(fig_negative_S6)

molecules_both_matching = set(table_S6[table_S6['Predicted positive probability'] > 0.5]['Name']).intersection(set(table_S6_predictions[table_S6_predictions['Predicted_positive_probability'] > 0.5]['Name']))
molecules_first_only = set(table_S6[table_S6['Predicted positive probability'] > 0.5]['Name']).difference(set(table_S6_predictions[table_S6_predictions['Predicted_positive_probability'] > 0.5]['Name']))
molecules_second_only = set(table_S6_predictions[table_S6_predictions['Predicted_positive_probability'] > 0.5]['Name']).difference(set(table_S6[table_S6['Predicted positive probability'] > 0.5]['Name']))

plot_venn_diagram(molecules_both_matching, molecules_first_only, molecules_second_only)
