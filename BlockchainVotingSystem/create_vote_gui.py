import tkinter as tk
import BlockVoting

def create_vote_statement():
    statement = statement_entry.get()
    # Logic to add the statement to the blockchain
    # Logic to send the statement to other users (this requires networking code)
    print(f"Created vote statement: {statement}")

# GUI Setup for Creating Vote
root = tk.Tk()
root.title("Create Voting Statement")

statement_entry = tk.Entry(root)
statement_entry.pack()

create_statement_button = tk.Button(root, text="Create Statement", command=create_vote_statement)
create_statement_button.pack()

root.mainloop()
