from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = Llama(model_path="./models/llama2_7b_chat_uncensored.ggmlv3.q4_0.bin", verbose=True, n_ctx=2048, n_gpu_layers=50)

class InferenceRequest(BaseModel):
    prompt: str

@app.post("/complete")
def perform_inference(request: InferenceRequest):
    output = llm(
        request.prompt,
        max_tokens=768,
        stop=["Q:", "\n"],
        echo=True,
    )
    print(output)
    return {"data": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
