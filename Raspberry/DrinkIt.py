#Logging notifications from ssh log

import time
import subprocess
import select

def main():
    f = subprocess.Popen(['tail', '-F', "/var/log/auth.log"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll(1):
            line = f.stdout.readline()
            line.strip("\\s+")
            line_data = line.split()
            username = line_data[10]

