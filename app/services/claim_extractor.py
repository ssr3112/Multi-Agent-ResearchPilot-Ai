from app.services.llm_service import llm


def extract_claims(text: str):

    prompt = f"""
    You are a research analyst.

    Extract the 3 most important factual claims from the text.

    Rules:
    - Return one claim per line
    - Do not number the claims
    - Do not add explanations

    Text:
    {text}
    """

    response = llm.invoke(prompt)

    claims = []

    for line in response.content.split("\n"):

        line = line.strip()

        if line:

            line = line.lstrip("1234567890.- ")

            claims.append(line)

    return claims