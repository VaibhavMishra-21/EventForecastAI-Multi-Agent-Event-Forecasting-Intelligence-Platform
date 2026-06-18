from workflows.forecasting_workflow import (
    run_forecast
)

topic = input(
    "Forecast Topic: "
)

result = run_forecast(topic)

print("\nRisk Level:")
print(result["risk"])

print("\nForecast:")
print(result["forecast"])

print("\nFinal Report:")
print(result["report"])
