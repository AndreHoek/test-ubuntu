#!/usr/bin/env python3

import socket
import urllib.request

print("Testing connectivity to outside world from container...")
print()

# Test 1: Socket connection to 8.8.8.8 (Google DNS)
print("Test 1: Connecting to 8.8.8.8 (Google DNS)...")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex(('8.8.8.8', 53))
    sock.close()
    
    if result == 0:
        print("✓ SUCCESS: Can reach 8.8.8.8 on port 53")
    else:
        print("✗ FAILED: Cannot reach 8.8.8.8 on port 53")
except Exception as e:
    print(f"✗ ERROR: {e}")

print()

# Test 2: HTTP request to a public site
print("Test 2: HTTP request to google.com...")
try:
    response = urllib.request.urlopen('http://google.com', timeout=5)
    print(f"✓ SUCCESS: HTTP request worked (Status: {response.status})")
except Exception as e:
    print(f"✗ FAILED: {e}")

print()

# Test 3: DNS resolution
print("Test 3: DNS resolution of google.com...")
try:
    ip = socket.gethostbyname('google.com')
    print(f"✓ SUCCESS: Resolved google.com to {ip}")
except Exception as e:
    print(f"✗ FAILED: {e}")

print()
print("Connectivity tests completed.")
