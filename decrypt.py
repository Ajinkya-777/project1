from cryptography.fernet import Fernet
import os

key_file = "secret.key"
log_file = "encrypted_log.txt"

def decrypt_logs():
    if not os.path.exists(key_file):
        print(f"[!] Error: {key_file} not found. You need this to decrypt!")
        return
    if not os.path.exists(log_file):
        print(f"[!] Error: {log_file} not found. No data to decrypt.")
        return
    with open(key_file, "rb") as f:
        key = f.read()
    
    cipher = Fernet(key)
    print("--- DECRYPTED KEYSTROKE LOGS ---")
    print("-" * 30)
    
    with open(log_file, "rb") as f:
        for line in f:
            try:
                decrypted_data = cipher.decrypt(line.strip())
                print(decrypted_data.decode())
            except Exception as e:
                print(f"[!] Could not decrypt line: {e}")

if __name__ == "__main__":
    decrypt_logs()