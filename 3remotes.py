import socket
import tkinter as tk
from tkinter import ttk

# Initialize main GUI
root = tk.Tk()
root.title("DirecTV Remote")

# StringVars for dropdown and connection fields
selected_port = tk.StringVar(value="1")
host_var = tk.StringVar(value="172.20.50.49")
port_var = tk.StringVar(value="4998")

# Top Frame: IR Port selector
frame_top = tk.Frame(root)
frame_top.grid(row=0, column=0, columnspan=3, pady=(10, 0))
tk.Label(frame_top, text="Select IR Port:").pack(side="left", padx=5)
port_selector = ttk.Combobox(frame_top, textvariable=selected_port, values=["1", "2", "3"], state="readonly", width=5)
port_selector.pack(side="left")
port_selector.current(0)
# Command map: Button label -> IR command with placeholder {}
commands = {
    "1": "sendir,1:{},14,38000,1,1,230,46,46,46,23,23,23,23,23,23,23,23,23,46,23,23,23,46,23,1143,115,43",
    "2": "sendir,1:{},4,39000,1,1,232,46,46,46,23,23,23,23,23,23,23,23,46,23,23,23,46,23,23,1155,116,44",
    "3": "sendir,1:{},5,38000,1,1,230,46,46,46,23,23,23,23,23,23,23,23,46,46,23,23,46,46,23,1143,115,43",
    "4": "sendir,1:{},7,39000,1,1,232,46,46,46,23,23,23,23,23,23,23,46,23,23,23,23,46,46,23,1155,116,44",
    "5": "sendir,1:{},8,38000,1,1,230,46,46,46,23,23,23,23,23,23,23,46,23,46,23,46,23,23,23,1143,115,43",
    "6": "sendir,1:{},9,39000,1,1,232,47,47,47,23,23,23,23,23,23,23,47,47,23,23,47,23,47,23,1155,116,44",
    "7": "sendir,1:{},10,39000,1,1,232,46,46,46,23,23,23,23,23,23,23,46,46,46,23,46,46,23,23,1155,116,44",
    "8": "sendir,1:{},11,39000,1,1,232,46,46,46,23,23,23,23,23,23,46,23,23,23,23,46,46,23,23,1155,116,44",
    "9": "sendir,1:{},12,38000,1,1,230,46,46,46,23,23,23,23,23,23,46,23,23,46,23,46,46,46,23,1143,115,43",
    "0": "sendir,1:{},13,39000,1,1,232,46,46,46,23,23,23,23,23,46,23,23,23,46,23,46,46,23,23,1155,116,44",
    "Play": "sendir,1:{},62,39000,1,1,232,46,46,46,23,23,23,23,46,46,23,23,23,23,46,46,46,46,23,1155,116,44",
    "Guide": "sendir,1:{},71,39000,1,1,232,46,46,46,23,23,23,23,46,23,46,23,23,23,23,23,23,23,23,1155,116,44",
    "Exit": "sendir,1:{},74,38000,1,1,229,45,45,45,22,22,22,22,45,22,22,45,45,22,45,45,45,45,22,1143,114,45,45,45,22,22,22,22,45,22,22,45,45,22,45,45,45,45,22,1143",
    "Back": "sendir,1:{},75,39000,1,1,232,46,46,46,23,23,23,23,46,23,23,46,46,46,23,23,23,23,23,1155,116,44",
    "Menu": "sendir,1:{},76,39000,1,1,232,46,46,46,23,23,23,23,46,23,23,23,23,23,46,23,46,23,23,1155,116,44",
    "Info": "sendir,1:{},77,38000,1,1,230,46,46,46,23,23,23,23,46,23,46,46,46,23,23,46,23,46,23,1143,115,43",
    "Up": "sendir,1:{},82,39000,1,1,231,46,46,46,23,23,23,23,46,23,23,23,23,46,46,23,46,46,23,1143,115,46,46,46,23,23,23,23,46,23,23,23,23,46,46,23,46,46,23,1143",
    "Down": "sendir,1:{},83,39000,1,1,229,45,45,45,22,22,22,22,45,22,22,22,45,22,45,45,22,22,22,1164,114,45,45,45,22,22,22,22,45,22,22,22,45,22,45,45,22,22,22,1164",
    "Left": "sendir,1:{},84,39000,1,1,231,46,46,46,23,23,23,23,46,23,23,23,46,46,46,46,23,46,23,1143,115,46,46,46,23,23,23,23,46,23,23,23,46,46,46,46,23,46,23,1143",
    "Right": "sendir,1:{},85,38000,1,1,231,46,46,46,23,23,23,23,46,23,23,46,23,23,46,46,23,46,23,1143,115,46,46,46,23,23,23,23,46,23,23,46,23,23,46,46,23,46,23,1143",
    "Select": "sendir,1:{},86,39000,1,1,232,46,46,46,23,23,23,23,46,23,23,46,23,46,46,46,46,23,23,1155,116,44",
    "Ch Up": "sendir,1:{},87,39000,1,1,231,46,46,46,23,23,23,23,23,23,46,46,23,46,46,23,46,23,23,1143,115,46,46,46,23,23,23,23,23,23,46,46,23,46,46,23,46,23,23,1143",
    "Ch Dn": "sendir,1:{},88,38000,1,1,231,46,46,46,23,23,23,23,23,23,46,46,46,23,46,23,46,46,23,1143,115,46,46,46,23,23,23,23,23,23,46,46,46,23,46,23,46,46,23,1143",
    "Previous": "sendir,1:{},89,38000,1,1,230,46,46,46,23,23,23,23,23,23,46,46,46,46,46,46,23,23,23,1143,115,43",
    "Dash": "sendir,1:{},90,38000,1,1,230,46,46,46,23,23,23,23,23,46,23,23,46,23,23,46,46,46,23,1143,115,43",
    "Enter": "sendir,1:{},91,39000,1,1,233,46,46,46,23,23,23,23,23,46,23,23,46,46,46,23,23,23,23,1155,116,44"
}

# Command sender function
def send_command(ir_command_template):
    host = host_var.get()
    try:
        port = int(port_var.get())
    except ValueError:
        print("Invalid port number")
        return

    ir_command = ir_command_template.format(selected_port.get())

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall((ir_command + "\r").encode())
            response = s.recv(1024)
            print("Response:", response.decode())
    except Exception as e:
        print(f"Error: {e}")

# Main button layout
layout = [
    ["Guide", "Exit", "Info"],
    ["Menu", "Up", "Back"],
    ["Left", "Down", "Right"],
    ["Previous", "Select", "Enter"],
    ["Ch Up", "Ch Dn", "Dash"],
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["0", "Play"]
]

for r, row in enumerate(layout, start=1):
    for c, label in enumerate(row):
        if label in commands:
            tk.Button(
                root,
                text=label,
                width=10,
                height=2,
                command=lambda cmd=commands[label]: send_command(cmd)
            ).grid(row=r, column=c, padx=5, pady=5)

# Bottom Frame: Host and Port input
connection_frame = tk.Frame(root)
connection_frame.grid(row=r+1, column=0, columnspan=3, pady=(10, 10))

tk.Label(connection_frame, text="Host:").pack(side="left", padx=5)
tk.Entry(connection_frame, textvariable=host_var, width=15).pack(side="left")

tk.Label(connection_frame, text="Port:").pack(side="left", padx=5)
tk.Entry(connection_frame, textvariable=port_var, width=6).pack(side="left")

# Run GUI
root.mainloop()
