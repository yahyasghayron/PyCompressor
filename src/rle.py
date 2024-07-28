def rle_compress(data):
    compressed = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1
        compressed.append(f"{count}{data[i]}")
        i += 1
    return ''.join(compressed)

def rle_decompress(data):
    decompressed = []
    i = 0
    while i < len(data):
        count = 0
        while i < len(data) and data[i].isdigit():
            count = count * 10 + int(data[i])
            i += 1
        decompressed.append(data[i] * count)
        i += 1
    return ''.join(decompressed)

if __name__ == "__main__":
    test_string = "AAAABBBCCDAA"
    compressed = rle_compress(test_string)
    print("Compressed:", compressed)
    decompressed = rle_decompress(compressed)
    print("Decompressed:", decompressed)
    assert test_string == decompressed, "Error: The decompressed string does not match the original"
