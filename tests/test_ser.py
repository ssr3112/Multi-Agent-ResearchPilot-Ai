from app.agents.researcher import researcher_agent

state = {
    "query": "Latest AI Agent Frameworks",
    "logs": []
}

result = researcher_agent(state)

print(result["logs"])