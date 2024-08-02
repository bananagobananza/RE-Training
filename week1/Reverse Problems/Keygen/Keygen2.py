def compute_parts(param1, param2, param3, param4):
    str_len1 = len(param1)
    str_len2 = len(param2)
    if str_len1 >= 33 or str_len2 >= 65 or param4 <= 15:
        return 0

    concat_str = param1 + param2
    str_len = len(concat_str)

    part1 = 0
    part4 = 32
    part2 = 8
    part3 = 39
    ivar3 = 2
    ivar2 = 4

    for i in range(str_len):
        if str_len <= ivar3:
            ivar3 = 0
        if ivar2 < 0:
            ivar2 = str_len - 1

        bvar1 = ord(concat_str[i])
        part1 += bvar1
        part4 += ord(concat_str[ivar3]) * bvar1
        if i + 1 < str_len:
            part2 -= ord(concat_str[i + 1]) * ord(concat_str[ivar2])

        part3 += (ord(concat_str[ivar2]) | bvar1) & ord(concat_str[ivar3])

        ivar3 += 1
        ivar2 -= 1

    # Ensure parts are in the range 0-255
    part1 &= 0xFF
    part2 &= 0xFF
    part3 &= 0xFF
    part4 &= 0xFF

    formatted_string = "{:03d}-{:03d}-{:03d}-{:03d}".format(part1, part2, part3, part4)
    return formatted_string

param1 = "abcdef"
param2 = "abcd"
param3 = None
param4 = 256
result = compute_parts(param1, param2, param3, param4)
print(result)

# 020-242-055-076