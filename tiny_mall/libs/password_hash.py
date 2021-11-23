import os
import hashlib

sep = '$'
iterations = 100000
hash_name = 'sha256'
name = f'pbkdf2_{hash_name}'


def hash(password: str):
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        hash_name,
        password.encode('utf-8'),
        salt,
        iterations
    )
    return sep.join([name, str(iterations), salt.hex(), key.hex()])


def verify(plain_password: str, hashed_password: str):
    if not hashed_password.startswith(name):
        raise ValueError(f"not a valid {name} hash")
    [_, iterations, salt, key] = hashed_password.split(sep)
    new_key = hashlib.pbkdf2_hmac(
        hash_name,
        plain_password.encode('utf-8'),
        bytes.fromhex(salt),
        int(iterations),
    )
    return new_key.hex() == key
