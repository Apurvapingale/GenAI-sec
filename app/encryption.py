from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes

def encrypt_response(response: str):
    """Encrypt the response using AES encryption."""
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(response.encode('utf-8'))
    return (
        base64.b64encode(ciphertext).decode('utf-8'),
        base64.b64encode(key).decode('utf-8'),
        base64.b64encode(nonce).decode('utf-8')
    )
