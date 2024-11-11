import struct

def simulate_fild(edx_value, eax_value):
    # Combine edx and eax into a single 64-bit integer
    combined_value = (edx_value << 32) | eax_value
    # Convert the 64-bit integer to a double-precision floating point
    double_value = struct.unpack('d', struct.pack('Q', combined_value))[0]
    return double_value

# Example values for edx and eax
edx_value = 0x00081F2B
eax_value = 0xFF20A810

# Simulate the fild instruction
double_value = simulate_fild(edx_value, eax_value)

print("Double-Precision Floating-Point Value:", double_value)
