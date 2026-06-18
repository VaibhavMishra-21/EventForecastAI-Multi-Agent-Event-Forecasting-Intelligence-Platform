from typing import TypedDict

class ForecastState(TypedDict):
    event_query: str
    collected_data: str
    news_summary: str
    trends: str
    forecast: str
    risk: str
    final_report: str
