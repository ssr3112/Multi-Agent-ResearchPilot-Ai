from app.agents.researcher import researcher_agent
from app.agents.extractor import extractor_agent
from app.agents.fact_checker import fact_checker_agent

state = {
    "query": "Latest AI Agent Frameworks",
    "logs": []
}

state = researcher_agent(state)

state = extractor_agent(state)

state = fact_checker_agent(state)

print(
    state["verified_claims"][:3]
)