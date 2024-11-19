from Crypto.Cipher import AES
import base64

def decrypt_response(ciphertext: str, key: str, nonce: str):
    """Decrypt the AES-encrypted ciphertext."""
    ciphertext = base64.b64decode(ciphertext)
    key = base64.b64decode(key)
    nonce = base64.b64decode(nonce)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    response = cipher.decrypt(ciphertext)
    return response.decode('utf-8')
