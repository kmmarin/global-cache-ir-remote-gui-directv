Global Caché IR Remote GUI

A Python Tkinter-based GUI for sending IR commands over TCP/IP using a Global Caché networked IR device (like iTach). This app is pre-configured for DirecTV commands but can be easily adapted for other IR-controlled devices.

Features

Graphical remote control interface

Configurable Host and Port (with defaults)

Dropdown selection for IR port (1, 2, 3)

Modular command mapping for easy extension

Requirements

Python 3.6+

Tkinter (usually bundled with Python)

Usage

Clone the repository:

git clone https://github.com/YOUR_USERNAME/global-cache-ir-remote-gui.git
cd global-cache-ir-remote-gui

Run the script:

python3 3remotes.py

In the GUI:

Set the IP and port of your Global Caché device

Select IR Port (1, 2, or 3)

Click a button to send the corresponding IR command

Customization

Modify the commands dictionary in 3remotes.py to map button labels to your specific IR command strings.

IR commands must follow Global Caché's sendir format.

Example IR Command:

commands = {
    "Power": "sendir,1:{},1,38000,1,1,340,170,..."
}

Use {} as a placeholder for the selected IR port.

License

MIT License

Credits

Developed by Kevin M.
Inspired by the need for a simple, network-based remote for DirecTV control.
