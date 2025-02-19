import tkinter as tk
from tkinter import simpledialog, messagebox
from encrypt import encryption, img
from decrypt import decryption

# Define global variables to store encryption results
encrypted_msg = None
password = None
c = None

def catch_encryption():
    global encrypted_msg, password, c
    msg = simpledialog.askstring("Input", "Enter the secret message:")
    passcode = simpledialog.askstring("Input", "Enter the password:")
    if msg and passcode:
        encrypted_msg, password, c = encryption(msg, passcode)
        print("Encryption successful!")

def catch_decryption():
    if encrypted_msg and password and c:
        input_password = simpledialog.askstring("Input", "Enter the password for decryption:")
        decrypted_message = decryption(img, encrypted_msg, password, c, input_password)
        if decrypted_message == "YOU ARE NOT auth":
            messagebox.showerror("Error", "YOU ARE NOT auth")
        else:
            messagebox.showinfo("Decrypted Message", decrypted_message)
    else:
        messagebox.showwarning("Warning", "No encrypted message found. Please encrypt a message first.")

def gui_new():
    root = tk.Tk()
    root.title("STEGANOGRAPHY")
    root.geometry("300x200")

    tk.Button(root, text="Encrypt", command=catch_encryption).pack(pady=10)
    tk.Button(root, text="Decrypt", command=catch_decryption).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    gui_new()