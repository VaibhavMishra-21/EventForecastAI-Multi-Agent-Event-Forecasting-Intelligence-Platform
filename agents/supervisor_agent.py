from services.gemini_service import generate

class SupervisorAgent:

    def finalize(
        self,
        topic,
        trends,
        forecast,
        risk
    ):

        prompt = f"""
        Topic:
        {topic}

        Trends:
        {trends}

        Forecast:
        {forecast}

        Risk:
        {risk}

        Create a structured forecast report.

        Sections:
        - Executive Summary
        - Key Drivers
        - Risk Analysis
        - Forecast Outlook
        """

        return generate(prompt)
