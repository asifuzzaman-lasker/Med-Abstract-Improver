from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.prompt import build_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def improve_abstract(text, style):

    prompt = build_prompt(text, style)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
