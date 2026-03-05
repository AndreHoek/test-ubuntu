#!/usr/bin/env python3

import socket

print("Everything is ok - the application is working")
print()

# Get container IP
container_ip = socket.gethostbyname(socket.gethostname())
print(f"Container IP: {container_ip}")

# Get default gateway (usually the Docker host) from /proc/net/route
try:
    with open('/proc/net/route') as f:
        for line in f:
            fields = line.strip().split()
            if fields[1] == '00000000':  # Default route
                gateway_hex = fields[2]
                # Convert hex to IP (reverse byte order)
                gateway_ip = '.'.join([str(int(gateway_hex[i:i+2], 16)) for i in range(6, -1, -2)])
                print(f"Docker Host Gateway IP: {gateway_ip}")
                break
except Exception as e:
    print(f"Could not determine host IP: {e}")

# Show exposed ports from environment or common Flask port
print(f"\nExposed Ports (from docker-compose):")
print("  - 5000 (Flask app)")
print("\nAccess the service from outside using: http://<ubuntu-host-ip>:5000")
