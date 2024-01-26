import time
import tkinter as tk
from tkinter import ttk
import supply_chain_blockchain as scb

def add_item():
    item_data = item_entry.get()
    new_block = scb.add_item_to_blockchain(item_data, scb.blockchain)
    scb.blockchain.append(new_block)
    update_display(new_block)
    item_entry.delete(0, tk.END)

def update_display(block):
    item_history.insert(tk.END, f"Item: {block.item_data} - Time: {time.ctime(block.timestamp)}\n")

root = tk.Tk()
root.title("Supply Chain Tracker")

ttk.Label(root, text="Enter Item Details:").pack()
item_entry = ttk.Entry(root)
item_entry.pack()

add_button = ttk.Button(root, text="Add/Update Item", command=add_item)
add_button.pack()

ttk.Label(root, text="Item History:").pack()
item_history = tk.Text(root, height=10, width=50)
item_history.pack()

root.mainloop()
