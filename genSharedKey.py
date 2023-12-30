from Crypto.Cipher import AES
from hashlib import sha256
import os

# AES暗号化関数
def aes_encrypt(shared_secret, plaintext):
  aes_key = sha256(shared_secret).digest()
  cipher = AES.new(aes_key, AES.MODE_EAX)
  ciphertext, tag = cipher.encrypt_and_digest(plaintext)
  return cipher.nonce, ciphertext, tag

# AES復号化関数
def aes_decrypt(shared_secret, nonce, ciphertext, tag):
    # 共有秘密鍵からAESキーを導出
    aes_key = sha256(shared_secret).digest()
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext