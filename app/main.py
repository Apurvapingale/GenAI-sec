from fastapi import FastAPI
from pydantic import BaseModel
from app.encryption import encrypt_response
from app.decryption import decrypt_response
from app.openai_client import get_groq_response

# Create the FastAPI app
app = FastAPI()

# Request and Response Models
class QuestionRequest(BaseModel):
    question: str

class EncryptedResponse(BaseModel):
    ciphertext: str
    key: str
    nonce: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Generate a response using groq model and encrypt the response.
    """
    try:
        # Get response from OpenAI
        response = get_groq_response(request.question)
        # Encrypt the response
        ciphertext, key, nonce = encrypt_response(response)
        return {"ciphertext": ciphertext, "key": key, "nonce": nonce}
    except Exception as e:
        return {"error": str(e)}

@app.post("/decrypt")
async def decrypt_data(encrypted: EncryptedResponse):
    """
    Decrypt the encrypted response using the provided ciphertext, key, and nonce.
    """
    try:
        # Decrypt the response
        original_response = decrypt_response(
            encrypted.ciphertext, encrypted.key, encrypted.nonce
        )
        return {"original_response": original_response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    """
    A root endpoint to verify the server is running.
    """
    return {"message": "Welcome to the Encryption-DC API!"}
