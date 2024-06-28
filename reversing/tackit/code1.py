hex_data = (
    "42d20000 42de0000 42e00000 42d80000 42d60000 42d40000 42d00000 42ce0000 "
    "42cc0000 42c80000 42e60000 42c20000 42f40000 42f00000 42c60000 42ec0000 "
    "42c40000 42dc0000 42da0000 42da0000 42dc0000 42cc0000 42cc0000 42400000 "
    "42440000 42f40000 42d80000 42d60000 42d40000 42d00000 42ce0000 42cc0000 "
    "42c80000 42e60000 42c20000 42e20000 42ee0000 42ca0000 42e40000 42e80000 "
    "42f20000 42ea0000 42d20000 42de0000 42e00000"
)

# Remove spaces and convert the hex string to bytes
hex_values = hex_data.split()
bytes_data = bytes.fromhex(''.join(hex_values))

# Try to decode the bytes using UTF-8 encoding
try:
    decoded_string = bytes_data.decode('utf-8')
    print(f"Decoded string (UTF-8): {decoded_string}")
except UnicodeDecodeError:
    print("Failed to decode using UTF-8.")

# You can try other encodings if UTF-8 fails, such as 'latin-1' or 'utf-16'
try:
    decoded_string = bytes_data.decode('latin-1')
    print(f"Decoded string (Latin-1): {decoded_string}")
except UnicodeDecodeError:
    print("Failed to decode using Latin-1.")

try:
    decoded_string = bytes_data.decode('utf-16')
    print(f"Decoded string (UTF-16): {decoded_string}")
except UnicodeDecodeError:
    print("Failed to decode using UTF-16.")
