# Save the current content of the app.py code from the canvas into a downloadable file
app_code = """
# STEP 1: Load and process sample data
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample Data
months = [f"Month {i}" for i in range(1, 13)]
free_users = np.round(np.linspace(10000, 15000, 12))
conversion_rate = np.linspace(0.05, 0.08, 12)
paid_users = np.round(free_users * conversion_rate)
total_users = free_users + paid_users

ad_arpu = 0.5
sub_arpu = 10

ad_revenue = free_users * ad_arpu
sub_revenue = paid_users * sub_arpu
total_revenue = ad_revenue + sub_revenue

cogs = total_revenue * 0.1  # 10% COGS
opex = np.full(12, 8000)
net_profit = total_revenue - cogs - opex

ltv = (sub_arpu * 12) * conversion_rate
cac = np.linspace(2, 5, 12)
gross_margin = (total_revenue - cogs) / total_revenue

# Create DataFrame
df = pd.DataFrame({
    'Month': months,
    'Free Users': free_users,
    'Paid Users': paid_users,
    'Total Users': total_users,
    'Ad Revenue': ad_revenue,
    'Sub Revenue': sub_revenue,
    'Total Revenue': total_revenue,
    'COGS': cogs,
    'OPEX': opex,
    'Net Profit': net_profit,
    'LTV': ltv,
    'CAC': cac,
    'Gross Margin': gross_margin
})

# STEP 2: Launch Dash App
app = dash.Dash(__name__)
app.title = "Freemium App Financial Dashboard"

app.layout = html.Div([
    html.H1("📊 Freemium App KPI Dashboard"),
    dcc.Dropdown(
        id='metric',
        options=[
            {'label': col, 'value': col} for col in ['Free Users', 'Paid Users', 'Total Revenue', 'Net Profit', 'LTV', 'CAC', 'Gross Margin']
        ],
        value='Total Revenue'
    ),
    dcc.Graph(id='line-chart'),
    html.H3("📈 Revenue Breakdown"),
    dcc.Graph(
        figure=px.bar(df, x='Month', y=['Ad Revenue', 'Sub Revenue'], title="Revenue Composition", barmode='stack')
    )
])

@app.callback(
    Output('line-chart', 'figure'),
    Input('metric', 'value')
)
def update_chart(selected_metric):
    fig = px.line(df, x='Month', y=selected_metric, title=f"{selected_metric} Over Time")
    return fig

if __name__ == '__main__':
    app.run(debug=False)
"""

# Save to file
file_path = "/mnt/data/app.py"
with open(file_path, "w") as f:
    f.write(app_code)

file_path
