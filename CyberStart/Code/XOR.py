a = 0xB105F00D
b = 0xAAA8400A
bitwise_xor = a ^ b  # ^ is used for XOR binary
hex_string = hex(bitwise_xor) # Call built in hex() function
print(hex_string)