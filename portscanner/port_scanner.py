import socket
target_ip=input("Enter IP address: ")
print("scanning for ports")

for i in range(20, 101):
    print(i)
    s = socket.socket()

    try:
        s.connect((target_ip,i))
        print(f"port open {i}")
        
    except:
        print(f"port closed {i}")
    finally:
        s.close()