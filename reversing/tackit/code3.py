import struct

hex_data = (
    "42d20000 42de0000 42e00000 42d80000 42d60000 42d40000 42d00000 42ce0000 "
    "42cc0000 42c80000 42e60000 42c20000 42f40000 42f00000 42c60000 42ec0000 "
    "42c40000 42dc0000 42da0000 42da0000 42dc0000 42cc0000 42cc0000 42400000 "
    "42440000 42f40000 42d80000 42d60000 42d40000 42d00000 42ce0000 42cc0000 "
    "42c80000 42e60000 42c20000 42e20000 42ee0000 42ca0000 42e40000 42e80000 "
    "42f20000 42ea0000 42d20000 42de0000 42e00000"
)

# Remove spaces and split the string into individual hex values
hex_values = hex_data.split()

# Function to convert hex to wchar_t (wide character)
def hex_to_wchar(hex_str):
    # Convert hex string to little-endian unsigned short (2 bytes)
    value = int(hex_str, 16)
    return struct.pack('<H', value).decode('utf-16le')

# Convert all hex values to wide characters
wide_chars = [hex_to_wchar(hex_val) for hex_val in hex_values]

# Join wide characters into a single string
decoded_string = ''.join(wide_chars)

# Print the decoded string
print(decoded_string)
