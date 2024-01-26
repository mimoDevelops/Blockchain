import hashlib
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket
import threading

# Blockchain Logic
class Block:
    def __init__(self, index, previous_hash, timestamp, message, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.message = message
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, message):
    value = str(index) + str(previous_hash) + str(timestamp) + str(message)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(last_block, message):
    index = last_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, last_block.hash, timestamp, message)
    return Block(index, last_block.hash, timestamp, message, hash)

# GUI for Chat Application
def send_message():
    message = message_input.get()
    if message:
        new_block = create_new_block(blockchain[-1], message)
        blockchain.append(new_block)
        update_chat_display(new_block)
        message_input.delete(0, tk.END)

def update_chat_display(block):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"[{time.ctime(block.timestamp)}] {block.message}\n")
    chat_display.config(state=tk.DISABLED)

# Server function to handle incoming connections
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        message = client_socket.recv(1024).decode()
        client_socket.close()
        if message:
            new_block = create_new_block(blockchain[-1], message)
            blockchain.append(new_block)
            root.event_generate("<<NewMessage>>", when="tail", data=message)

# Event binding for updating the chat display from the server thread
def on_new_message(event):
    update_chat_display(blockchain[-1])

# Initialize Blockchain
blockchain = [create_genesis_block()]

# GUI Setup
root = tk.Tk()
root.title("Blockchain Chat Application")

chat_display = ScrolledText(root, state=tk.DISABLED, height=15)
chat_display.pack()

message_input = tk.Entry(root)
message_input.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Bind the new message event
root.bind("<<NewMessage>>", on_new_message)

# Start server thread
threading.Thread(target=server, daemon=True).start()

root.mainloop()
