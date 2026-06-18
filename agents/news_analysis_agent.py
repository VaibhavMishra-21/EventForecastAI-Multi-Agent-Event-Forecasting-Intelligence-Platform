from services.gemini_service import generate

class NewsAnalysisAgent:

    def summarize(self, topic):

        prompt = f"""
        Summarize major news themes
        related to:

        {topic}

        Give concise insights.
        """

        return generate(prompt)
