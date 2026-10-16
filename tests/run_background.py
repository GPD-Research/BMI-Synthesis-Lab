import subprocess
import os

proc = subprocess.Popen(["python3", "tests/sleep_done.py"])
print(f"Started process PID: {proc.pid}")