import unittest
from src.rle import rle_compress, rle_decompress

class TestRLE(unittest.TestCase):

    def test_rle_compress(self):
        self.assertEqual(rle_compress("AAAABBBCCDAA"), "4A3B2C1D2A")

    def test_rle_decompress(self):
        self.assertEqual(rle_decompress("4A3B2C1D2A"), "AAAABBBCCDAA")

    def test_rle_full_cycle(self):
        original = "AAAABBBCCDAA"
        compressed = rle_compress(original)
        decompressed = rle_decompress(compressed)
        self.assertEqual(original, decompressed)

if __name__ == "__main__":
    unittest.main()
