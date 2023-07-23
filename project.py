import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, password)
# Create the Tkinter window
window = tk.Tk()
window.title("Random Password Generator")
# Create the input widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()
# Create the generate button
generate_button = tk.Button(window, text="Generate Password", 
command=generate_password)
generate_button.pack()
# Create the output widget
output_label = tk.Label(window, text="Generated Password:")
output_label.pack()
output_text = tk.Text(window, height=1, width=30)
output_text.pack()
# Start the Tkinter event loop
window.mainloop()