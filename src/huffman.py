import heapq

""" the heap node hold the frequency , the chraacter and the left and right child """
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
    def __eq__(self, other):
        return self.freq == other.freq



class HuffmanCoding:

    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}


    def create_frequency_table(self , text):
        """Create a frequency table from input data."""
        frequency_table = {}
        for char in text:
            if char in frequency_table:
                frequency_table[char] += 1
            else:
                frequency_table[char] = 1

        return frequency_table


    def build_heap(self , frequency):
        heap = []
        for key  in frequency:
            heapq.heappush(heap, HeapNode(key, frequency[key]))
        return heap


    def merge_nodes(self, heap):
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)
        return heapq.heappop(heap)


    def build_codes(self, root):
        self.build_codes_helper(root, "")


    def build_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.build_codes_helper(root.left, current_code + "0")
        self.build_codes_helper(root.right, current_code + "1")


    def get_encoded_text(self, text):
        return "".join([self.codes[char] for char in text])


    def compress(self, text):
        frequency = self.create_frequency_table(text)
        print(frequency)
        heap = self.build_heap(frequency)
        root = self.merge_nodes(heap)
        self.build_codes(root)
        return self.get_encoded_text(text)


    def decompress(self, compressed_text):
        current_code = ""
        decompressed_text = []
        for bit in compressed_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decompressed_text.append(self.reverse_mapping[current_code])
                current_code = ""
        return ''.join(decompressed_text)



if __name__ == "__main__":
    # Test your implementation here
    test = "The bird is the word"
    huffman = HuffmanCoding()
    compressed_text = huffman.compress(test)
    print("Compressed text:", compressed_text)
    decompressed_text = huffman.decompress(compressed_text)
    print("Decompressed text:", decompressed_text)
