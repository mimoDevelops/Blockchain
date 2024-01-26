import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import time

# Blockchain Logic
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

# Document Hash Calculation
def calculate_document_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

# GUI Code
def upload_document():
    file_path = filedialog.askopenfilename()
    if file_path:
        document_hash = calculate_document_hash(file_path)
        add_block(document_hash)
        messagebox.showinfo("Document Uploaded", "Your document has been securely uploaded to the blockchain.")

def add_block(data):
    global blockchain, previous_block
    block_to_add = create_new_block(previous_block, data)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    update_blockchain_display()

def update_blockchain_display():
    blockchain_display.config(state=tk.NORMAL)
    blockchain_display.delete(1.0, tk.END)
    for block in blockchain:
        blockchain_display.insert(tk.END, f"Block #{block.index} at {time.ctime(block.timestamp)}:\nHash: {block.hash}\n\n")
    blockchain_display.config(state=tk.DISABLED)

# Initialize Blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# GUI Setup
root = tk.Tk()
root.title("Document Verification System")

upload_button = tk.Button(root, text="Upload Document", command=upload_document)
upload_button.pack()

blockchain_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=15)
blockchain_display.pack()

root.mainloop()
