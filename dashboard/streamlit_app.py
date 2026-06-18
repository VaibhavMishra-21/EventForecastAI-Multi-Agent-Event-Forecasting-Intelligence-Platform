import streamlit as st

from workflows.forecasting_workflow import (
    run_forecast
)

st.title(
    "EventForecastAI"
)

topic = st.text_input(
    "Enter Event Topic"
)

if st.button("Forecast"):

    result = run_forecast(topic)

    st.subheader("Risk")
    st.write(result["risk"])

    st.subheader("Forecast")
    st.write(result["forecast"])

    st.subheader("Report")
    st.write(result["report"])
