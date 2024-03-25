import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os
from repo_path import repo_path

def load_data(repo_path):
    eos30gr_output_path = os.path.join(repo_path, 'data/eos30gr/eos30gr_output_data.csv')
    eos30gr_output = pd.read_csv(eos30gr_output_path)
    eos30gr_output.dropna(inplace=True)
    eos30gr_output['activity10'] = (eos30gr_output['activity10'] * 100).round(2).astype(int)
    return eos30gr_output

def plot_histogram(eos30gr_output):
    fig = px.histogram(eos30gr_output, x='activity10', nbins=10, title='Distribution of Model Predictions (Probabilities)', labels={'activity10': 'Probability'}, opacity=0.75)
    fig.update_layout(
        bargap=0.1,
        xaxis=dict(title='Probability'),
        yaxis=dict(title='Frequency'),
        font=dict(family='Arial', size=12),
    )
    st.plotly_chart(fig)

def plot_histograms_above_below_80(eos30gr_output):
    above_or_equal_80 = eos30gr_output[eos30gr_output['activity10'] >= 80]
    below_80 = eos30gr_output[eos30gr_output['activity10'] < 80]

    fig_above_80 = px.histogram(above_or_equal_80, x='activity10', nbins=10, title='Distribution of Model Predictions (Probabilities) - Greater than or Equal to 80')
    fig_below_80 = px.histogram(below_80, x='activity10', nbins=10, title='Distribution of Model Predictions (Probabilities) - Less than 80')

    for fig in [fig_above_80, fig_below_80]:
        fig.update_layout(
            bargap=0.1,
            xaxis=dict(title='Probability'),
            yaxis=dict(title='Frequency'),
            font=dict(family='Arial', size=12),
        )

    st.plotly_chart(fig_above_80)
    st.plotly_chart(fig_below_80)

def plot_pie_chart(eos30gr_output):
    above_or_equal_80_count = len(eos30gr_output[eos30gr_output['activity10'] >= 80])
    below_80_count = len(eos30gr_output[eos30gr_output['activity10'] < 80])

    fig = px.pie(names=['Greater than or Equal to 80', 'Less than 80'], values=[above_or_equal_80_count, below_80_count],
                 title='Frequency Comparison of Model Predictions')

    st.plotly_chart(fig)

def plot_top_20_smiles(eos30gr_output):
    top_20_smiles = eos30gr_output.sort_values(by='activity10', ascending=False).head(20)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=top_20_smiles['input'],
        x=top_20_smiles['activity10'],
        orientation='h',
        marker=dict(color='skyblue'),
        text=top_20_smiles['activity10'],
        textposition='inside',
        hoverinfo='none'
    ))

    fig.update_layout(
        title='Top 20 SMILES with Top Probability',
        xaxis=dict(title='Probability'),
        yaxis=dict(title='Standardized SMILES'),
        height=600,
        width=800,
        margin=dict(l=100, r=50, t=50, b=50),
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig)

def plot_bottom_20_smiles(eos30gr_output):
    bottom_20_smiles = eos30gr_output.sort_values(by='activity10', ascending=True).head(20)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=bottom_20_smiles['input'],
        x=bottom_20_smiles['activity10'],
        orientation='h',
        marker=dict(color='skyblue'),
        text=bottom_20_smiles['activity10'],
        textposition='inside',
        hoverinfo='none'
    ))

    fig.update_layout(
        title='Bottom 20 SMILES with minimal Probability',
        xaxis=dict(title='Probability'),
        yaxis=dict(title='Standardized SMILES'),
        height=600,
        width=800,
        margin=dict(l=100, r=50, t=50, b=50),
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig)


def plot_probabilities_scatter(eos30gr_output):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=eos30gr_output['activity10'],
        y=eos30gr_output.index,
        mode='markers',
        marker=dict(color='skyblue', opacity=0.7),
        hovertemplate='Probability: %{x}<br>Index: %{y}',
    ))

    fig.update_layout(
        title='Probabilities Scatter Plot',
        xaxis=dict(title='Probability'),
        yaxis=dict(title='Index'),
        height=600,
        width=800,
        margin=dict(l=100, r=50, t=50, b=50),
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )

    st.plotly_chart(fig)

def plot_probability_ranges_pie(eos30gr_output):
    bins = range(0, eos30gr_output['activity10'].max() + 11, 10)  
    eos30gr_output['activity10_bin'] = pd.cut(eos30gr_output['activity10'], bins=bins, right=False)

    frequency = eos30gr_output['activity10_bin'].value_counts().sort_index()

    fig = go.Figure(go.Pie(
        labels=[f'{bin.left}-{bin.right-1}' for bin in frequency.index],
        values=frequency,
        hole=0.3,
        textinfo='percent+label',
        marker=dict(colors=px.colors.qualitative.Set1),
        sort=False
    ))

    fig.update_layout(
        title='Frequency of Models in Probability Ranges',
        height=600,
        width=800,
        margin=dict(l=100, r=50, t=50, b=50),
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig)

def plot_molecules_per_activity10_probability(eos30gr_output):
    grouped_eos30gr_output = eos30gr_output.groupby('activity10').size().reset_index(name='count')

    fig = go.Figure(go.Bar(
        x=grouped_eos30gr_output['activity10'],
        y=grouped_eos30gr_output['count'],
        marker=dict(color='skyblue'),
        text=grouped_eos30gr_output['count'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Number of Molecules per Activity10 Probability',
        xaxis=dict(title='Activity10 Probability'),
        yaxis=dict(title='Number of Molecules'),
        height=600,
        width=800,
        margin=dict(l=100, r=50, t=50, b=50),
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig)

def main(repo_path):
    eos30gr_output = load_data(repo_path)
    plot_histogram(eos30gr_output)
    plot_histograms_above_below_80(eos30gr_output)
    plot_pie_chart(eos30gr_output)
    plot_top_20_smiles(eos30gr_output)
    plot_bottom_20_smiles(eos30gr_output)
    plot_probabilities_scatter(eos30gr_output)
    plot_probability_ranges_pie(eos30gr_output)
    plot_molecules_per_activity10_probability(eos30gr_output)

repo_path = repo_path()
st.subheader("Predictions recieved from eos30gr model,it took approx 20 minutes to get result(local M1 air)")
eos30gr_output_path = os.path.join(repo_path,'data/eos30gr/eos30gr_output_data.csv')
eos30gr_output = pd.read_csv(eos30gr_output_path)
st.write(eos30gr_output)  
main(repo_path)
