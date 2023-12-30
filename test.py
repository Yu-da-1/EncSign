from main import private_key_x, public_key_x, shared_secret_x
from genSharedKey import aes_encrypt, aes_decrypt

#署名のテスト
def test_signature():
  message = b"Test message for signature"
  signature = private_key_x.sign(message)
  assert public_key_x.verify(signature, message)
  print("Success test")

#暗号化、復号化テスト
def test_encryption():
  plaintext = b"Test message for encryption"
  nonce, ciphertext, tag = aes_encrypt(shared_secret_x, plaintext)
  decrypted_message = aes_decrypt(shared_secret_x, nonce, ciphertext, tag)
  print("Success enc, dec")

test_signature()
test_encryption()