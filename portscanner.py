# Simple Port Scanner
import socket

# Define the target host and port range or specific ports
target_host = "127.0.0.1" # Replace with the target IP address
target_ports = [22, 21, 23, 25, 80, 443, 8080] # List of common ports to scan, can be modified

# Create a socket objective
def scan_port(target_host, target_ports):
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open on {target_host}")
# Run the port scanner
scan_port(target_host, target_ports)