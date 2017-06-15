import sys
import subprocess

proc = subprocess.Popen(["python.exe", "C:\\MPI\\brute.py", "9743a66f914cc249efca164485a19c5c", "3", "4"])
print proc.communicate()
