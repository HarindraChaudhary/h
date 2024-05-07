string = "Hello World"
for char in string:
    xor_result = ord(char) ^ 127
    and_result = ord(char) & 127
    print("XOR result for", char, "is", xor_result)
    print("AND result for", char, "is", and_result)
