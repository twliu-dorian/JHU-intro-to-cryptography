#!/usr/bin/python3
from Crypto.Cipher import AES

plaintext = bytearray.fromhex('255044462d312e350a25d0d4c5d80a34')
ciphertext = bytearray.fromhex('d06bf9d0dab8e8ef880660d2af65aa82')
iv = bytearray.fromhex('09080706050403020100A2B2C2D2E2F2')

with open('key_dict.txt') as f:
    keys = f.readlines()

for key in keys:
    key = key.rstrip('\n')
    aes_key = bytearray.fromhex(key)
    cipher = AES.new(key=aes_key, mode=AES.MODE_CBC, iv=iv)
    
    pt = cipher.encrypt(plaintext)
    if pt == ciphertext:
        print("find the key:", key)
        exit(0)
