import socket
import time

HOST = '172.20.50.49'
PORT = 4998

# List of IR commands (you must add the \r at the end of each)
commands = [
    "sendir,1:1,74,38000,1,1,229,45,45,45,22,22,22,22,45,22,22,45,45,22,45,45,45,45,22,1143,114,45,45,45,22,22\r",
    "sendir,1:2,74,38000,1,1,229,45,45,45,22,22,22,22,45,22,22,45,45,22,45,45,45,45,22,1143,114,45,45,45,22,22\r",
    "sendir,1:3,74,38000,1,1,229,45,45,45,22,22,22,22,45,22,22,45,45,22,45,45,45,45,22,1143,114,45,45,45,22,22\r"
]

def send_ir_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            print(f"Sent: {command.strip()} | Response: {response.strip()}")
    except Exception as e:
        print(f"Error sending command: {e}")

# Loop forever
while True:
    for cmd in commands:
        send_ir_command(cmd)
        time.sleep(3)  # wait 3 seconds between commands

    print("Cycle complete. Waiting 5 minutes...\n")
    time.sleep(5 * 60)  # wait 5 minutes
