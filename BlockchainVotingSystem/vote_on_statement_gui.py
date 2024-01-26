import tkinter as tk
import BlockVoting

def vote_on_statement():
    vote = vote_entry.get()
    # Logic to record the vote on the blockchain
    print(f"Voted: {vote}")

# GUI Setup for Voting
root = tk.Tk()
root.title("Vote on Statement")

vote_entry = tk.Entry(root)
vote_entry.pack()

vote_button = tk.Button(root, text="Vote", command=vote_on_statement)
vote_button.pack()

root.mainloop()
