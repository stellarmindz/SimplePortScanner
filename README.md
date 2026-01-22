# SimplePortScanner
A simple network utility written in Python to scan for open ports. This script allows users to input any IP address and timeout duration to check network availability.
Simple Port Scanner

A basic Python script to check for open ports on a specific IP address using the socket library.
📝 Description

This script "knocks" on a list of common network ports (like 80, 443, and 22). If a port answers, the script marks it as open. It is designed to be a lightweight tool for learning network basics.
🚀 How to Use

    Open portscanner.py and change the target_host to the IP address you want to scan.

    Run the script using your terminal or command prompt:
    Bash

    python portscanner.py

⚙️ How it Works

The script uses a for loop to go through your list of ports:

    It creates a TCP socket.

    It waits up to 1 second for a response.

    If the connection is successful (result == 0), it prints the open port to your screen.

⚠️ Important Note

Authorized use only: Only scan your own devices or networks where you have permission.
