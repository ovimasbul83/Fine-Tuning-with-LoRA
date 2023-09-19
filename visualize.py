import plotly.express as px
import pandas as pd
def visualize_bar(trainable_params,all_params):
    trainable_parameters = trainable_params
    total_parameters = all_params
    data = pd.DataFrame({'parameters': ['Trainable parameters', 'Total parameters'],
                        'Count': [trainable_parameters, total_parameters]})
    fig = px.bar(data, x='parameters', y='Count', text='Count', title='Trainable vs. Total parameters')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(
        xaxis_title='parameters',
        yaxis_title='Count',
        uniformtext_minsize=10,
        uniformtext_mode='hide'
    )

    fig.show()
def pie_chart(trainable_params,all_params):
    trainable_weights = trainable_params
    total_weights = all_params
    data = pd.DataFrame({'Weights': ['Trainable Weights', 'Total Weights'],
                        'Count': [trainable_weights, total_weights]})

    fig = px.pie(data, names='Weights', values='Count', title='Trainable vs. Total Weights')

    fig.show()