from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Replace this key with your own Fernet key (should be 32 URL-safe base64-encoded bytes)
key = "b'Nxtzx4tSZleX5t5-q5DqcUersM5RR=UhgRdt65CdtWA='"
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = encrypt_data(message, cipher_suite)
    return render_template('index.html', output=f'Encrypted: {encrypted_message.decode("utf-8")}')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message'].encode()
    decrypted_message = decrypt_data(encrypted_message, cipher_suite)
    return render_template('index.html', output=f'Decrypted: {decrypted_message}')

def encrypt_data(data, cipher_suite):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, cipher_suite):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

if __name__ == '__main__':
    app.run()