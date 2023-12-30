from ecdsa import SigningKey, SECP256k1, ECDH

# 鍵ペアXの生成
private_key_x = SigningKey.generate(curve=SECP256k1)
public_key_x = private_key_x.get_verifying_key()

# 鍵ペアYの生成
private_key_y = SigningKey.generate(curve=SECP256k1)
public_key_y = private_key_y.get_verifying_key()

# メッセージの署名
message = b"Hello, world!"
signature = private_key_x.sign(message)
print("署名:", signature.hex())

# 署名の検証
assert public_key_x.verify(signature, message)

# パーティーXでECDHの初期化と共有秘密鍵の生成
ecdh_x = ECDH(curve=SECP256k1)
ecdh_x.load_private_key(private_key_x)
ecdh_x.load_received_public_key(public_key_y)
shared_secret_x = ecdh_x.generate_sharedsecret_bytes()

# パーティーYでECDHの初期化と共有秘密鍵の生成
ecdh_y = ECDH(curve=SECP256k1)
ecdh_y.load_private_key(private_key_y)
ecdh_y.load_received_public_key(public_key_x)
shared_secret_y = ecdh_y.generate_sharedsecret_bytes()

# 共有秘密鍵が同じであることの確認
assert shared_secret_x == shared_secret_y
print("Shared Key:", shared_secret_x.hex())