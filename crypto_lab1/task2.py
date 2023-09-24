from Crypto.Cipher import AES
import time
import random

# Define the time range
start_time = "2018-04-17 21:08:49"
end_time = "2018-04-17 23:08:49"
KEYSIZE = 16
# Convert start and end times to timestamps
start_timestamp = int(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S")))
end_timestamp = int(time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S")))

# Initialize a list to store AES keys
aes_keys = []

# Number of AES keys to generate per timestamp
keys_per_timestamp = 1

for t in range(start_timestamp, end_timestamp+1, 1):  # within a 2-hour window
    random.seed(t)
    key=[]
    for i in range(KEYSIZE):
        key.append(random.randint(0, 255))
        # print("{:02x}".format(key[i]), end="")
    print(key,"\n")
    aes_key = bytes(key)
    print(aes_key)
    aes_keys.append(key)

data = bytearray.fromhex('255044462d312e350a25d0d4c5d80a34')
ciphertext = bytearray.fromhex('d06bf9d0dab8e8ef880660d2af65aa82')
iv = bytearray.fromhex('09080706050403020100A2B2C2D2E2F2')

# key=bytsearray.fromhex('95fa2030e73ed3f8da761b4eb805dfd7')
# cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
# guess = cipher.encrypt(data)
# if guess == ciphertext:
#     print("find the key:", key)
for k in aes_keys:
    # key = bytearray.fromhex(k)
    cipher = AES.new(key=k, mode=AES.MODE_CBC, iv=iv)
    guess = cipher.encrypt(data)
    if guess == ciphertext:
        print("find the key:", k)
        exit(0)

print("cannot find the key!")


