import pandas as pd
import os
import plotly.graph_objs as go
import plotly.express as px
import streamlit as st

def load_data(repo_path):
    table_S7_path = os.path.join(repo_path, 'data/eos30gr/Table S7.xlsx')
    table_S7_output_from_local_model_eos30gr_path = os.path.join(repo_path, 'data/eos30gr/table_S7_output_from_local_model_eos30gr.csv')

    table_S7 = pd.read_excel(table_S7_path, skiprows=1)
    table_S7_predictions = pd.read_csv(table_S7_output_from_local_model_eos30gr_path)
    return table_S7, table_S7_predictions

def process_data(table_S7, table_S7_predictions):
    table_S7_predictions.drop(columns='key', inplace=True)
    table_S7_predictions.rename(columns={'activity10': 'Predicted_positive_probability', 'input': 'smiles'}, inplace=True)
    table_S7_predictions = pd.merge(table_S7_predictions, table_S7[['DrugBank ID', 'Name', 'ATC category']], left_index=True, right_index=True)
    desired_columns_order = ['DrugBank ID', 'Name', 'ATC category', 'smiles', 'Predicted_positive_probability']
    table_S7_predictions = table_S7_predictions[desired_columns_order]
    table_S7_predictions['Predicted_negative_probability'] = 1 - table_S7_predictions['Predicted_positive_probability']
    return table_S7_predictions

def plot_positive_probability_comparison(table_S7, table_S7_predictions):
    fig_positive = go.Figure()
    fig_positive.add_trace(go.Scatter(
        x=table_S7.index,
        y=table_S7['Predicted positive probability'],
        mode='lines',
        name='Original Research data (Positive probability)',
        line=dict(color='blue')
    ))
    fig_positive.add_trace(go.Scatter(
        x=table_S7_predictions.index,
        y=table_S7_predictions['Predicted_positive_probability'],
        mode='lines',
        name='Predicted positive data',
        line=dict(color='red')
    ))
    fig_positive.update_layout(
        xaxis=dict(title='Index'),
        yaxis=dict(title='Probability'),
        title='Comparison of Research paper and predicted positive probability',
        legend=dict(x=0, y=1.0),
        height=600,
        width=800
    )
    return fig_positive

def plot_negative_probability_comparison(table_S7, table_S7_predictions):
    fig_negative = go.Figure()
    fig_negative.add_trace(go.Scatter(
        x=table_S7.index,
        y=table_S7['Predicted negative probability'],
        mode='lines',
        name='Original Research data (Negative probability)',
        line=dict(color='blue')
    ))
    fig_negative.add_trace(go.Scatter(
        x=table_S7_predictions.index,
        y=table_S7_predictions['Predicted_negative_probability'],
        mode='lines',
        name='Predicted negative data',
        line=dict(color='red')
    ))
    fig_negative.update_layout(
        xaxis=dict(title='Index'),
        yaxis=dict(title='Probability'),
        title='Comparison of Research paper and predicted negative probability',
        legend=dict(x=0, y=1.0),
        height=600,
        width=800
    )
    return fig_negative

def main(repo_path):
    st.subheader("Predictions recieved from eos30gr model,it took approx 3-5 minutes to get result(local M1 air)")
    table_S7, table_S7_predictions = load_data(repo_path)
    st.write(table_S7_predictions)

    table_S7_predictions = process_data(table_S7, table_S7_predictions)

    fig_positive = plot_positive_probability_comparison(table_S7, table_S7_predictions)

    fig_negative = plot_negative_probability_comparison(table_S7, table_S7_predictions)

    st.plotly_chart(fig_positive)
    st.plotly_chart(fig_negative)

main('/Users/adhivp/Desktop/Ersilia_tasks')  # Replace with your actual repo path
