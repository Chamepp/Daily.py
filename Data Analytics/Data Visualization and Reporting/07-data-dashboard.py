import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('your_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Interactive Data Dashboard'),
    
    # Add dropdown for selecting a variable
    dcc.Dropdown(
        id='variable-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0]
    ),
    
    # Add scatter plot for visualizing selected variable
    dcc.Graph(id='scatter-plot')
])

# Define the callback function to update the scatter plot
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('variable-dropdown', 'value')]
)
def update_scatter_plot(selected_variable):
    fig = px.scatter(df, x=selected_variable, y='target_variable')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

