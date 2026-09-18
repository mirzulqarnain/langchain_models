from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenRouter(
    model="google/gemma-4-31b-it:free"
)

result = llm.invoke("Write a poem about a lonely computer.and also tell me whats the capital of Pakistan")

print(result.content) 