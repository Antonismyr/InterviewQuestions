# Import your libraries
import pandas as pd

# Start writing code
sf_transactions['created_atYearMonth'] = sf_transactions['created_at'].dt.to_period('M')
monthly_revenue = sf_transactions.groupby('created_atYearMonth')['value'].sum().reset_index().sort_values(by='created_atYearMonth')

percentage_change = monthly_revenue.copy()
percentage_change['Montly Percentage Change'] = percentage_change['value'].pct_change()*100
percentage_change['Montly Percentage Change'] = percentage_change['Montly Percentage Change'].round(2).dropna()
percentage_change = percentage_change[['created_atYearMonth', 'Montly Percentage Change']]