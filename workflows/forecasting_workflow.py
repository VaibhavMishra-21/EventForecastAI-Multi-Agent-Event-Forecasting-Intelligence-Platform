from agents.data_collector_agent import DataCollectorAgent
from agents.news_analysis_agent import NewsAnalysisAgent
from agents.trend_agent import TrendAgent
from agents.forecasting_agent import ForecastingAgent
from agents.risk_agent import RiskAgent
from agents.supervisor_agent import SupervisorAgent

collector = DataCollectorAgent()
news_agent = NewsAnalysisAgent()
trend_agent = TrendAgent()
forecast_agent = ForecastingAgent()
risk_agent = RiskAgent()
supervisor = SupervisorAgent()


def run_forecast(topic):

    data = collector.collect(topic)

    news = news_agent.summarize(topic)

    trends = trend_agent.analyze(
        data,
        news
    )

    forecast = forecast_agent.forecast(
        topic,
        trends
    )

    risk = risk_agent.assess(
        forecast
    )

    report = supervisor.finalize(
        topic,
        trends,
        forecast,
        risk
    )

    return {
        "data": data,
        "news": news,
        "trends": trends,
        "forecast": forecast,
        "risk": risk,
        "report": report
    }
