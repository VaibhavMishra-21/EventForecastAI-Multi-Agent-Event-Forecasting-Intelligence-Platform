from services.gemini_service import generate

class TrendAgent:

    def analyze(self, data, news):

        prompt = f"""
        Historical Data:

        {data}

        News Summary:

        {news}

        Identify important trends.
        """

        return generate(prompt)
