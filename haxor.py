#!/usr/bin/env python3
import time
import random
import sys
print("Welcome 2 the supa real haxor program")
time.sleep(1)
found_ip = None
for _ in range(15):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    print(f"scanning ip {ip}")
    if found_ip is None and random.random() < 0.2:
        found_ip = ip
    time.sleep(random.uniform(0.1, 0.3))
if found_ip is None:
    found_ip = ip
    
print("Scan complete..")
print(f"Unsecure IP found at {found_ip}")
duration = 4
steps = 40
for i in range(steps + 1):
    percent = int(i * 100 / steps)
    bar = "#" * i + "-" * (steps - i)
    sys.stdout.write(f"\rInjecting: [{bar}] {percent}%")
    sys.stdout.flush()
    time.sleep(duration / steps)
print("\nInjection complete..")
time.sleep(1)
print(f"root access given at {found_ip}")
print(f"Access the site here or however the network chuck viewer larps as a hacker: http://localhost:8501")
