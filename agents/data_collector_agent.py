class DataCollectorAgent:

    def collect(self, query):

        return f"""
        Historical event information related to:
        {query}

        Data collected from local event records.
        """
