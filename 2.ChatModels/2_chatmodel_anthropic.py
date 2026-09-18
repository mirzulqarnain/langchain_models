from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() 

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro"
)

result = model.invoke("Write a poem about a lonely computer.and also tell me whats the capital of Pakistan")    

print(result.content)