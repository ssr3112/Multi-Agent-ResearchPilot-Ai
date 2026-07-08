# test_claim_extractor.py

from app.services.claim_extractor import extract_claims

sample_text = """
LangGraph is an orchestration framework for AI agents.
CrewAI supports role-based agent collaboration.
AutoGen was developed by Microsoft Research.
"""

claims = extract_claims(sample_text)

print(claims)