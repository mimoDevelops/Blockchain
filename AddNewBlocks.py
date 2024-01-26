import hashlib
import time
import tkinter as tk
from tkinter import scrolledtext, END

# Blockchain code
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(last_block, data):
    index = last_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, last_block.hash, timestamp, data)
    return Block(index, last_block.hash, timestamp, data, hash)

def add_block(data):
    global blockchain, previous_block
    block_to_add = create_new_block(previous_block, data)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    update_blockchain_display()

def update_blockchain_display():
    blockchain_display.config(state=tk.NORMAL)
    blockchain_display.delete(1.0, END)
    for block in blockchain:
        blockchain_display.insert(END, f"Block #{block.index}\nHash: {block.hash}\nData: {block.data}\n\n")
    blockchain_display.config(state=tk.DISABLED)

# Initialize blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# GUI code
root = tk.Tk()
root.title("Simple Blockchain Application")

blockchain_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=10)
blockchain_display.pack()

data_entry = tk.Entry(root)
data_entry.pack()

add_block_button = tk.Button(root, text="Add Block", command=lambda: add_block(data_entry.get()))
add_block_button.pack()

update_blockchain_display()

root.mainloop()
