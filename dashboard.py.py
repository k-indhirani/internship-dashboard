import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("INTERNSHIP PROJECT ANALYTICS DASHBOARD - K.INDRANI")

df = pd.read_csv('internship_data.csv')
df['Start_Start_Start_Start_Date'] = pd.to_Start_Start_Start_Start_Datetime(df['Start_Start_Start_Start_Date'])

dept = st.sidebar.multiselect(
    "Department Filter Pannu:", 
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

filtered_df = df[df['Department'].isin(dept)]

col1, col2 = st.columns(2)
with col1:
    fig1 = px.line(filtered_df, x='Start_Start_Start_Start_Date', y='Hours Spent', title='Hours Trend Over Time')
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    dept_hours = filtered_df.groupby('Department')['Hours Spent'].sum().reset_index()
    fig2 = px.bar(dept_hours, x='Department', y='Hours Spent', title='Total Hours by Department')
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    fig3 = px.scatter(filtered_df, x='Team Size', y='Hours Spent', color='Status', title='Team Size vs Hours Spent')
    st.plotly_chart(fig3, use_container_width=True)
with col4:
    fig4 = px.pie(filtered_df, names='Status', title='Project Status Distribution')
    st.plotly_chart(fig4, use_container_width=True)
