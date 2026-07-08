from app.services.llm_service import llm

response = llm.invoke("What is Artificial Intelligence?")

print(response.content)