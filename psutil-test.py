#!/usr/bin/env python3

import psutil

print("CPU load:")
print(psutil.cpu_percent(interval=1, percpu=True))

print("Virtual memory:")
print(psutil.virtual_memory())
