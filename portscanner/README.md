# 🔍 Python TCP Port Scanner

A simple TCP port scanner built in Python using the `socket` module. This project scans a target host for open TCP ports within a specified range and reports any open ports it discovers.

## Features

* Scan TCP ports on a target IP address
* Uses Python's built-in `socket` library
* Configurable socket timeout for faster scans
* Displays only open ports for clean output
* Proper exception handling to prevent crashes
* Automatically closes sockets after each connection attempt

## Technologies Used

* Python 3
* Socket Programming
* TCP Networking

## How It Works

The scanner:

1. Prompts the user for a target IP address.
2. Iterates through ports **1–1024**.
3. Creates a TCP socket for each port.
4. Attempts to establish a connection.
5. Reports ports that successfully accept a connection.
6. Closes the socket before moving to the next port.

## Example

```text
Enter IP address: 127.0.0.1

==================================================
PYTHON PORT SCANNER
==================================================
Target: 127.0.0.1
Scanning Started

Port open 80
Port open 443
```

## Project Structure

```text
port-scanner/
│── port_scanner.py
│── README.md
```

## Future Improvements

* Add multithreading for faster scanning
* Allow users to specify custom port ranges
* Display total scan time
* Support hostname resolution (e.g., google.com)
* Add IPv6 support
* Export scan results to a text file
* Improve terminal interface with colors and banners

## Disclaimer

This project was created for educational purposes to learn Python socket programming and basic networking concepts. Only scan systems and networks that you own or have explicit permission to test.

## Author

**Nish <3**
