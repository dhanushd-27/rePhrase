from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
)

system_prompt = """
You are a text transformation engine.
Return only the transformed text.
No explanations. No formatting.
Preserve meaning unless intent changes it.
"""

def invoke_model(intent: str, text: str, style: str):
    prompt = f"""
    {system_prompt}

    Intent: {intent}
    Text: {text}
    Style: {style}
    """
    response = model.invoke(prompt)
    return response.content
