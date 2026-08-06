import os
import pandas as pd
import streamlit as st
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Student Academic Risk Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Academic Risk Dashboard")
st.markdown("Interactive dashboard for analyzing student performance and academic risk.")

# ==========================================================
# LOAD DATA
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "featured_final_marks.csv"
)

INSIGHTS_PATH = os.path.join(
    BASE_DIR,
    "output",
    "summaries",
    "business_insights.csv"
)

df = pd.read_csv(DATA_PATH)

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.header("Filters")

risk = st.sidebar.multiselect(
    "Academic Risk",
    options=df["Academic_Risk"].unique(),
    default=df["Academic_Risk"].unique()
)

attendance = st.sidebar.multiselect(
    "Attendance Category",
    options=df["Attendance_Category"].unique(),
    default=df["Attendance_Category"].unique()
)

grade = st.sidebar.multiselect(
    "Performance Grade",
    options=df["Performance_Grade"].unique(),
    default=df["Performance_Grade"].unique()
)

filtered_df = df[
    (df["Academic_Risk"].isin(risk)) &
    (df["Attendance_Category"].isin(attendance)) &
    (df["Performance_Grade"].isin(grade))
]

# ==========================================================
# KPI CARDS
# ==========================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Students",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Final Marks",
        round(filtered_df["Final Exam Marks (out of 100)"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Attendance",
        round(filtered_df["Attendance (%)"].mean(), 2)
    )

with col4:
    high_risk = (
        filtered_df["Academic_Risk"] == "High Risk"
    ).sum()

    st.metric(
        "High Risk Students",
        high_risk
    )

# ==========================================================
# CHARTS
# ==========================================================

st.subheader("Visualizations")

left, right = st.columns(2)

with left:

    fig = px.bar(
        filtered_df["Academic_Risk"]
        .value_counts()
        .reset_index(),
        x="Academic_Risk",
        y="count",
        title="Academic Risk Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.bar(
        filtered_df["Performance_Grade"]
        .value_counts()
        .reset_index(),
        x="Performance_Grade",
        y="count",
        title="Performance Grade Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

left, right = st.columns(2)

with left:

    fig = px.scatter(

        filtered_df,

        x="Attendance (%)",

        y="Final Exam Marks (out of 100)",

        color="Academic_Risk",

        title="Attendance vs Final Marks"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    corr = filtered_df.select_dtypes("number").corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# DATASET
# ==========================================================

st.subheader("Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ==========================================================
# BUSINESS INSIGHTS
# ==========================================================

st.subheader("Business Insights")

if os.path.exists(INSIGHTS_PATH):

    insights = pd.read_csv(INSIGHTS_PATH)

    for i, row in insights.iterrows():

        st.success(
            row["Business Insights"]
        )

else:

    st.warning(
        "Run Business Insights script first."
    )