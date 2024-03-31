import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,roc_curve, auc, r2_score
from repo_path import repo_path

def load_external_data_1287_random_eos30gr_output(repo_path):
    external_data_1287_random_eos30gr_output_path = os.path.join(repo_path, 'data/eos30gr/external_data_1287_random_eos30gr_output.csv')
    external_data_1287_random_eos30gr_output = pd.read_csv(external_data_1287_random_eos30gr_output_path)
    return external_data_1287_random_eos30gr_output

def load_external_data_1287_random(repo_path):
    external_data_1287_random_path = os.path.join(repo_path, 'data/eos30gr/external_dataset_1287_random.csv')
    external_data_1287_random = pd.read_csv(external_data_1287_random_path)
    return external_data_1287_random


def map_to_label(prediction):
    if prediction > 0.5:
        return 1
    else:
        return 0

repo_path = repo_path()

external_data_1287_random_eos30gr_output = load_external_data_1287_random_eos30gr_output(repo_path)
st.subheader("Predictions recieved from eos30gr model,it took approx 3 hours to get result(Google collab)")
st.write(external_data_1287_random_eos30gr_output)

external_data_1287_random = load_external_data_1287_random(repo_path)

external_data_1287_random_eos30gr_output['predictions_label_0.5'] = external_data_1287_random_eos30gr_output['activity10'].apply(lambda x: map_to_label(x))

real_labels = external_data_1287_random['class']
predicted_labels = external_data_1287_random_eos30gr_output['predictions_label_0.5']

cm = confusion_matrix(real_labels, predicted_labels)

heatmap = go.Heatmap(
    z=cm,
    x=['Predicted 0', 'Predicted 1'],  
    y=['True 0', 'True 1'],             
    colorscale='Blues',
    colorbar=dict(title='Count'),       
    hoverinfo='z',                      
    showscale=True,                     
    xgap=1,                             
    ygap=1,                             
    text=cm,                            
    hovertemplate='True: %{y}<br>Predicted: %{x}<br>Count: %{text}',
    zmin=0                              
)

layout = go.Layout(
    title='Confusion Matrix',
    xaxis=dict(title='Predicted Label'),
    yaxis=dict(title='Real Label')
)

fig = go.Figure(data=[heatmap], layout=layout)
st.plotly_chart(fig)

TP = cm[1, 1]
TN = cm[0, 0]
FP = cm[0, 1]
FN = cm[1, 0]

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = sensitivity = TP / (TP + FN)
specificity = TN / (TN + FP)
negative_predictive_value = TN / (TN + FN)
balanced_accuracy = (sensitivity + specificity) / 2
mcc = (TP * TN - FP * FN) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5
f1_score = 2 * precision * recall / (precision + recall)

metrics_dict = {
    "Accuracy": accuracy,
    "Sensitivity": sensitivity,
    "Specificity": specificity,
    "Precision / Positive Predictive Value": precision,
    "Recall": recall,
    "Negative Predictive Value": negative_predictive_value,
    "Balanced Accuracy": balanced_accuracy,
    "Matthew's Correlation Coefficient": mcc,
    "F1 Score": f1_score,
}
equations_dict = {
    "Accuracy": "(TP + TN) / (TP + TN + FP + FN)",
    "Sensitivity": "TP / (TP + FN)",
    "Specificity": "TN / (TN + FP)",
    "Precision / Positive Predictive Value": "TP / (TP + FP)",
    "Recall": "TP / (TP + FN)",
    "Negative Predictive Value": "TN / (TN + FN)",
    "Balanced Accuracy": "(Sensitivity + Specificity) / 2",
    "Matthew's Correlation Coefficient": "(TP * TN - FP * FN) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5",
    "F1 Score": "2 * Precision * Recall / (Precision + Recall)",
}

metrics_df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['Value'])

metrics_df['Equation'] = [equations_dict[metric] for metric in metrics_df.index]
st.subheader("Evaluation Metrics")
st.write(metrics_df)

fpr, tpr, thresholds = roc_curve(external_data_1287_random['class'], external_data_1287_random_eos30gr_output['predictions_label_0.5'])
auroc = auc(fpr, tpr)
r2 = r2_score(external_data_1287_random['class'], external_data_1287_random_eos30gr_output['predictions_label_0.5'])

roc_curve_trace = go.Scatter(
    x=fpr,
    y=tpr,
    mode='lines',
    line=dict(color='blue', width=2),
    name=f'ROC curve (AUROC = {auroc:.2f})'
)


diagonal_line_trace = go.Scatter(
    x=[0, 1],
    y=[0, 1],
    mode='lines',
    line=dict(color='gray', dash='dash'),
    name='Diagonal Reference'
)

fig = go.Figure(data=[roc_curve_trace, diagonal_line_trace])

fig.update_layout(
    title='Receiver Operating Characteristic (ROC) Curve',
    xaxis=dict(title='False Positive Rate'),
    yaxis=dict(title='True Positive Rate'),
    legend=dict(x=0.98, y=0.02, bordercolor='black', borderwidth=1),
    margin=dict(l=50, r=50, t=50, b=50),
)

fig.add_annotation(
    x=0.98,
    y=0.85,
    text=f'AUROC: {auroc:.4f}<br>R2 value: {r2:.4f}',
    showarrow=False,
    bgcolor='black',
    bordercolor='black',
    borderwidth=1,
    font=dict(size=10)
)

st.write(fig)
st.write(f"AUROC: {auroc:.4f}")
st.write(f"R2 value: {r2:.4f}")
