# Define a bytes object containing UTF-8 encoded data
# utf8_bytes = b'%PDF-1.504172018'
# print(utf8_bytes)
# # Decode the bytes into a UTF-8 string
# hex_string = utf8_bytes.hex()

# # Print the decoded string
# print(hex_string)

# Define the input byte sequence
# input_bytes = b'%PDF-1.504172018'

# # Decode the bytes into a UTF-8 string (not text)
# utf8_string =  input_bytes.hex()

# # Print the decoded string
# print(utf8_string)

# Define the input hex string
# hex_string ="255044462d312e350a25d0d4c5d80a34"

# # Convert the hex string to bytes
# hex_bytes = bytes.fromhex(hex_string)

# # Decode the bytes to a UTF-8 string
# utf8_string = hex_bytes.decode('utf-8')

# # Print the human-readable string
# print(utf8_string)
def hex_to_human_readable(hex_string):
    try:
        # Convert the hex string to bytes
        hex_bytes = bytes.fromhex(hex_string)

        # Decode the bytes to a UTF-8 string
        utf8_string = hex_bytes.decode('utf-8')

        return utf8_string
    except ValueError as e:
        # Handle any exceptions (e.g., invalid hex string)
        return str(e)

# Example usage:
hex_string = "255044462d312e350a25d0d4c5d80a34"
result = hex_to_human_readable(hex_string)

if isinstance(result, str):
    print("Human-Readable String:", result)
else:
    print("Error:", result)