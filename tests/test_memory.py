

from app.tools.memory import (
    save_report
)

sample_report = """
AI Agent Framework Research

LangGraph is widely used for agent orchestration.

CrewAI supports role-based collaboration.
"""

save_report(
    sample_report
)

print("Report Saved")