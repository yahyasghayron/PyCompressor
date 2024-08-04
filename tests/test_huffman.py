import unittest
from src.huffman import HuffmanCoding

class TestHuffman(unittest.TestCase):

    def test_huffman_compress_decompress(self):
        original_string = "AAAABBBCCDAA"
        huffman = HuffmanCoding()
        compressed_string = huffman.compress(original_string)
        decompressed_string = huffman.decompress(compressed_string)
        self.assertEqual(original_string, decompressed_string)

if __name__ == "__main__":
    unittest.main()

