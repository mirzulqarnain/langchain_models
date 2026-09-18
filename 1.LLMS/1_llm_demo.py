from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenRouter(
    model="openrouter/free", temperature = 1.5 
)

result = llm.invoke("suggest me 5 Pakistani names")

print(result.content) 