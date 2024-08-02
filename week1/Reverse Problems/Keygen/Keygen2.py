param1 = "abcd"
param2 = "abcd"

part1 = 0
part4 = 32
part2 = 8
part3 = 39
ivar4 = 2
ivar3 = 4

concat_str = param1 + param2
str_len = len(concat_str)

i = 0
if str_len > 0:
    while (i < str_len):
        if str_len <= ivar4:
            ivar4 = 0
        if ivar3 < 0:
            ivar = str_len - 1
        bvar1 = ord(concat_str[i])
        part1 = part1 + bvar1
        part4 = part4 + ord(concat_str[ivar4]) * bvar1
        if i + 1 < str_len:
            part2 = part2 - ord(concat_str[i + 1]) * ord(concat_str[ivar3])
        part3 = part3 + ((ord(concat_str[ivar3]) | bvar1) & ord(concat_str[ivar4]))
        ivar4 += 1
        ivar3 -= 1
        i += 1

print(f"Formatted Output: {part1:03}-{part2:03}-{part3:03}-{part4:03}")