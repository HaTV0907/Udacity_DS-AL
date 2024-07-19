import heapq
from collections import defaultdict
import pdb

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    # handle empty string
    if len(data) == 0:
        return None

    frequency_table = defaultdict(int)
    for char in data:
        frequency_table[char] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    # valid the input param
    if None == frequency_table:
        return []
    heap = []
    for char, freq in frequency_table.items():
        node = Node(char, freq)
        heapq.heappush(heap, node)
    if len(heap) == 1:
        return heapq.heappop(heap)
    while len(heap) > 1:
        # get the least frequennt char in most left node
        left_node = heapq.heappop(heap)
        # next to the right node
        right_node = heapq.heappop(heap)
        # construct merged node
        merged_freq = left_node.freq + right_node.freq
        merged_node = Node(None, merged_freq)
        merged_node.left = left_node
        merged_node.right = right_node
        # push merged node to heap
        heapq.heappush(heap, merged_node)
    # return lowest frequency node
    return heapq.heappop(heap)

def build_encoding_table(root):
    encoding_table = {}
    # handle the case that huffman tree has only one node
    if root.left == None and root.right == None:
        encoding_table[root.char] = "0"
        return encoding_table
    # other cases
    def traverse(node, code):
        if node.char:
            encoding_table[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    traverse(root, "")
    return encoding_table

def huffman_encoding(data):
    # Check if the data is empty
    # pdb.set_trace()
    if len(data) == 0:
        return "", []

    frequency_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)

    encoded_data = ""
    for char in data:
        encoded_data += encoding_table[char]

    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree
    # handle the case that huffman tree has only one node
    # pdb.set_trace()
    if encoded_data != "":
        if huffman_tree.left == None and huffman_tree.right == None:
            for bit in encoded_data:
                decoded_data +=huffman_tree.char
            return decoded_data
    # other cases
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data

def test_huffman_encoding():
    test_cases = [
        ("The bird is the word", "Basic Example"),
        ("", "Edge Case - Empty String"),
        ("It is not the failure, just a challenge", "Mixed Characters"),
        ("aaaaaa", "Edge Case - Single Character Repeated"),
        ("a" * 10000, "Edge Case - Large Input")
    ]

    for data, description in test_cases:
        print(f"Test Case: {description}\nData        : {data}")
        encoded_data, tree = huffman_encoding(data)
        print(f"Encoded Data: {encoded_data}")
        decoded_data = huffman_decoding(encoded_data, tree)
        print(f"Decoded Data: {decoded_data}")
        assert data == decoded_data, f"Test failed for: {description}"
        print("Test passed!\n")

# Example usage
if __name__ == "__main__":

    test_huffman_encoding()


