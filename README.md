# project1
# 🛡️ Keylogger with Encrypted Data Exfiltration (PoC)

This is a **Proof-of-Concept (PoC)** keylogger built for educational and security research purposes. It demonstrates how keystrokes can be captured, encrypted using AES-128 (Fernet), and logged locally for simulated exfiltration.

## 🚀 Features
* **Live Keystroke Capture:** Monitors alphanumeric and special keys using `pynput`.
* **Authenticated Encryption:** Uses the `cryptography` library to ensure logs cannot be read without the `secret.key`.
* **Kill Switch:** Instantly stop the listener by pressing the `Esc` key.
* **Timestamped Logs:** Every captured key is logged with a precise date and time.
* **Decryption Tool:** Includes a separate script to safely decrypt and read captured data.

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.x installed. You will need to install the following dependencies:

```bash
pip install pynput cryptography

### 2. Usage
Run the Logger:

```Bash
python logger.py
The script will generate a secret.key (keep this safe!) and an encrypted_log.txt.

Stop the Logger:

Press the Esc key on your keyboard.

Decrypt the Logs:

```Bash
python decrypt.py

📂 Project Structure
logger.py: The main script that captures and encrypts keystrokes.

decrypt.py: A utility script to turn the encrypted gibberish back into readable text.

secret.key: (Auto-generated) The master key for encryption/decryption.

encrypted_log.txt: (Auto-generated) The encrypted data store.

⚠️ Ethical & Legal Warning
This project is for educational purposes only. The unauthorized monitoring of a computer system is illegal and unethical. This software should only be used on systems you own or have explicit, written permission to test. The developers assume no liability for misuse or damage caused by this program.

🛡️ Defensive Perspective
To protect against such tools:

Use a trusted Antivirus/EDR solution.

Regularly check Task Manager for unrecognized background processes.

Monitor your Startup Apps folder for suspicious scripts.
