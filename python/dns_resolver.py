import socket

domain = input("Enter domain: ")
print(f"IP: {socket.gethostbyname(domain)}")