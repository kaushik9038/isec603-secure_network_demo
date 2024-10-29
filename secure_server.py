import os
import socket
import ssl
import subprocess

# Define localhost server communication information
HOST = 'localhost'
PORT = 5005
CERTIFICATE_FILE = "server.pem"

# This function will generate a server.pem certificate file if it doesnt exist
def gen_cert():
    if not os.path.exists(CERTIFICATE_FILE):
        print("No Certificate file found. Generating a self-signed certificate...")
        subprocess.run([
            "openssl", "req", "-new", "-x509", "-days", "365", "-nodes",
            "-out", CERTIFICATE_FILE, "-keyout", CERTIFICATE_FILE,
            "-subj", "/C=CAN/P=Alberta/L=Calgary/O=Organization/OU=Department/CN=localhost"
        ])
        print("New Server Certificate has been generated successfully.")
    else:
        print("Server Certificate file already exists.")

# The gen_cert() function is called
gen_cert()

# Loading the SSL certificate and key
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTIFICATE_FILE, keyfile=CERTIFICATE_FILE)

# Creating a TCP socket for stream based connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    # Wrapping the socket with SSL
    with context.wrap_socket(sock, server_side=True) as ssock:
        ssock.bind((HOST, PORT))
        ssock.listen(5)
        print(f"The Secure server is ready for communication and is listening on {HOST}:{PORT}...")

        while True:
            # Here once client connection is received then this section does the acknowledgement
            client_socket, client_address = ssock.accept()
            print(f"Request to establish connection received from {client_address}")
            with client_socket:
                data = client_socket.recv(1024)
                print(f"Secure connection between the server and client has been achieved, data received from client: {data.decode()}")
                client_socket.sendall(b"Welcome to the secure connection between the client and the server!")
