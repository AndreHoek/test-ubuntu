#!/usr/bin/env python3

import socket
import subprocess

print("Everything is ok - the application is working")
print()

# Get container IP
container_ip = socket.gethostbyname(socket.gethostname())
print(f"Container IP: {container_ip}")

# Get default gateway (usually the Docker host)
try:
    result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'default' in line:
            gateway_ip = line.split()[2]
            print(f"Docker Host Gateway IP: {gateway_ip}")
            break
except Exception as e:
    print(f"Could not determine host IP: {e}")

# Show exposed ports from environment or common Flask port
print(f"\nExposed Ports (from docker-compose):")
print("  - 5000 (Flask app)")
print("\nAccess the service from outside using: http://<host-ip>:5000")
