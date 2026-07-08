from app.agents.researcher import researcher_agent
from app.agents.extractor import extractor_agent

state = {
    "query": "Latest AI Agent Frameworks",
    "logs": []
}

state = researcher_agent(state)

state = extractor_agent(state)

print("Number of Articles:")
print(len(state["extracted_content"]))

print("\nKeys:")
print(state["extracted_content"][0].keys())

print("\nNumber of Chunks:")
print(len(state["extracted_content"][0]["chunks"]))

print("\nFirst Chunk Preview:")
print(state["extracted_content"][0]["chunks"][0][:1000])