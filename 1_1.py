from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch

# Inicialização do FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Verifica se uma GPU está disponível
device = 0 if torch.cuda.is_available() else -1

# Carregar o pipeline do GPT-2
generator = pipeline('text-generation', model='gpt2', device=device)

@app.post("/generate/")
async def generate_text(input: TextInput):
    generated = generator(input.text, max_length=50, num_return_sequences=1)
    return {"input": input.text, "output": generated[0]['generated_text']}