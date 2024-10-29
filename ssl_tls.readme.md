# Secure Server-Client Communication using Python and SSL/TLS

## Overview
This Python project demonstrates secure communication between a server and a client using the SSL/TLS (Secure Socket Layer/Transport Layer Security) protocol over a TCP (Transmission Control Protocol) socket connection. The implementation includes two primary functions, `run_server()` and `run_client()`, designed to run the server and client, respectively. Additionally, a helper function, `generate_certificate()`, ensures the availability of an SSL certificate for secure encryption. SSL/TLS encrypts the communication channel, ensuring data integrity and confidentiality between the server and client.

## Key Components and Functionality

### 1. `gen_cert()`
This function verifies the presence of the `server.pem` certificate file, containing both a self-signed SSL certificate and a private key necessary for secure communication. If `server.pem` is missing, the function uses the `subprocess` module to run an OpenSSL command, generating a self-signed certificate.

- **OpenSSL Command Execution**: The command `openssl req -new -x509 -days 365 -nodes -out server.pem -keyout server.pem -subj "/C=US/ST=State/L=City/O=Organization/OU=Department/CN=localhost"` generates a new certificate valid for 365 days. The `-nodes` flag ensures the private key isn’t encrypted, making it easier to access within the server code.
- **Certificate Details**: The `-subj` flag specifies the required fields directly, avoiding user prompts for each field. Here, `CN=localhost` sets the hostname, making the certificate suitable for local testing.

**Outcome**: The `gen_cert()` function provides the server with a `server.pem` file, enabling secure, encrypted communication.


## Security Mechanisms

- **SSL/TLS Encryption**: Using SSL/TLS ensures all communication between the server and client is encrypted, preventing unauthorized interception and eavesdropping.
- **Certificate Authentication**: The server uses a self-signed certificate (`server.pem`) to authenticate itself to the client, ensuring the client only connects to a verified, trusted server.
- **Data Integrity and Confidentiality**: SSL/TLS encryption guarantees that data exchanged between the server and client remains untampered during transmission.

## Example Output

Upon execution, the server output confirms the setup of a secure server and the receipt of a client connection, while the client output confirms a successful secure connection and displays the server’s response.
# Secure Network Demo

This project demonstrates a secure client-server communication setup using Python. The `secure_client.py` and `secure_server.py` scripts enable the establishment of a secure, encrypted connection between a client and server, simulating secure data exchange.

## Overview

The server establishes a secure connection over `localhost:5005` using an SSL certificate, allowing encrypted communication between the client and server. The client connects to the server, exchanges messages, and then terminates the connection after successful communication.

## Server Output

To start the secure server, execute the following command:
```bash
/usr/bin/python3 /Users/kaushikmazumder/PycharmProjects/isec603-secure_network_demo/secure_server.py
The client server has established secure connection with the secure server.
The client server received data from server: Welcome to the secure connection between the client and the server!



## Client Output

To start the secure client, execute the following command:
```bash
/usr/bin/python3 /Users/kaushikmazumder/PycharmProjects/isec603-secure_network_demo/secure_client.py
The client server has established a secure connection with the secure server.
The client server received data from server: Welcome to the secure connection between the client and the server!
