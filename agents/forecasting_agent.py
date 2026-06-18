from services.gemini_service import generate

class ForecastingAgent:

    def forecast(self, topic, trends):

        prompt = f"""
        Topic:

        {topic}

        Trends:

        {trends}

        Estimate future developments
        and probability ranges.

        Educational forecasting only.
        """

        return generate(prompt)
