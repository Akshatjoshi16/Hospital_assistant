import os
from langchain_groq import ChatGroq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api=os.environ.get("GROQ")


llm=ChatGroq(
    api_key=api,
    model_name="llama-3.3-70b-versatile",
    temperature=0,

)

# client=Groq(api_key=api)

# async def generate_groq_stream(query:Query):
#     completion=client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role":"user","content":query.user_input}],
#         stream=True
#     )

#     for chunk in completion:
#         content=chunk.choices[0].delta.content
#         if content:
#             yield content
