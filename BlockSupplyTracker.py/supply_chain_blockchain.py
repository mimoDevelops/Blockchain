import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, item_data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.item_data = item_data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, item_data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(item_data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def add_item_to_blockchain(item_data, blockchain):
    last_block = blockchain[-1]
    index = last_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, last_block.hash, timestamp, item_data)
    return Block(index, last_block.hash, timestamp, item_data, hash)

blockchain = [create_genesis_block()]
