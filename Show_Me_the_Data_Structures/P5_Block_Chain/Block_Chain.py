import time
import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.data}{self.timestamp}{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if self.head is None:
            self.head = Block(data, "0")
        else:
            current = self.head
            while current.next:
                current = current.next
            new_block = Block(data, current.hash)
            current.next = new_block

    def print_blocks(self):
        current_block = self.head
        while current_block:
            print(f"Timestamp: {current_block.timestamp}")
            print(f"Data: {current_block.data}")
            print(f"SHA256 Hash: {current_block.hash}")
            print(f"Prev Hash: {current_block.previous_hash}")
            print("\n")
            current_block = current_block.next

# Example usage
blockchain = Blockchain()
blockchain.add_block("Head Block")
blockchain.add_block("Second Block")
blockchain.add_block("Third Block")
blockchain.add_block("")
blockchain.add_block("Hello, I am Ha. I am from Vietnam")
blockchain.print_blocks()
# timestamp is the time a block created. It's unique so there can not be two different block with same timestamp