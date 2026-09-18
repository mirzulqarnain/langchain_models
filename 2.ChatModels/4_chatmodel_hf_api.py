from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from dotenv import load_dotenv
load_dotenv()

 
llm = HuggingFaceEndpoint(

    repo_id="meta-llama/Llama-3.3-70B-Instruct:novita",
    task= "text-generation"
)


model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of Pakistan and tell me about the model Im using rn")

print(result.content)