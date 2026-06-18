class RiskAgent:

    def assess(self, forecast):

        text = forecast.lower()

        if "high probability" in text:
            return "HIGH"

        elif "moderate" in text:
            return "MEDIUM"

        return "LOW"
