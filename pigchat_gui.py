import tkinter as tk
import pigtime
import pigchat

def encrypt_text():
    input_text = entry.get("1.0", tk.END).strip()  
    timestamp = pigtime.get_pig_timestamp()
    output_text = pigchat.pigchat_emoji_encrypt(timestamp, input_text)
    entry.delete("1.0", tk.END)  
    entry.insert("1.0", output_text)

def decrypt_text():
    input_text = entry.get("1.0", tk.END).strip()  
    timestamp = pigtime.get_pig_timestamp()
    output_text = pigchat.pigchat_emoji_decrypt(timestamp, input_text)
    entry.delete("1.0", tk.END)  
    entry.insert("1.0", output_text)

root = tk.Tk()
root.title("Pigchat Converter")
root.minsize(400, 300)

def make_expanding(widget):
    widget.pack(expand=True, fill='both')

entry = tk.Text(root, width=50, height=15, wrap=tk.WORD)  
make_expanding(entry)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_text, bg="lightblue", fg="black")
encrypt_button.pack(side=tk.LEFT, padx=5, expand=True, fill='both')
decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_text, bg="lightgreen", fg="black")
decrypt_button.pack(side=tk.LEFT, padx=5, expand=True, fill='both')

root.mainloop()







