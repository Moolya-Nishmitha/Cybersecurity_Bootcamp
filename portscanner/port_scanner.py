import socket
target_ip=input("Enter IP address: ")
print("=" * 50)
print("PYTHON PORT SCANNER")
print("=" * 50)
print(f"Target: {target_ip}")
print("Scanning Started")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((target_ip, port))
        print(f"port open {port}")
        
    except (ConnectionRefusedError, socket.timeout, OSError):
        pass
    finally:
        s.close()
