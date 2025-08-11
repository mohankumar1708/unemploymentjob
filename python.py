import plotly.express as px
from plotly.offline import plot

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 1. Unemployment rate trend over time
fig1 = px.line(df, x='date', y='unemployment_rate', color='location',
               title='Unemployment Rate Over Time')

# 2. Job postings by location
fig2 = px.bar(df.groupby('location', as_index=False)['job_postings'].sum(),
              x='location', y='job_postings', title='Total Job Postings by Location')

# 3. College degree percentage vs unemployment rate
fig3 = px.scatter(df, x='college_degree_percentage', y='unemployment_rate',
                  color='location', size='job_postings',
                  title='College Degree % vs Unemployment Rate')

# 4. Average age by location
fig4 = px.box(df, x='location', y='average_age', title='Average Age Distribution by Location')

# Combine into dashboard HTML
dashboard_html = """
<html>
<head><title>Job Market & Unemployment Trends Dashboard</title></head>
<body>
<h1>Job Market & Unemployment Trends - Data Analysis Dashboard</h1>
""" + \
plot(fig1, output_type='div') + \
plot(fig2, output_type='div') + \
plot(fig3, output_type='div') + \
plot(fig4, output_type='div') + \
"""
</body>
</html>
"""

# Save the dashboard
dashboard_path = "/mnt/data/job_market_dashboard.html"
with open(dashboard_path, "w") as f:
    f.write(dashboard_html)

dashboard_path