import socket
import struct
import time
from pynput import keyboard

# UDP Setup
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Track active key states
pressed_keys = set()

def on_press(key):
    try:
        # Normalize char keys to lowercase
        if hasattr(key, 'char') and key.char is not None:
            pressed_keys.add(key.char.lower())
        else:
            pressed_keys.add(key)
        # print(key.char.lower())
    except Exception:
        pass

def on_release(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            pressed_keys.discard(key.char.lower())
        else:
            pressed_keys.discard(key)
    except Exception:
        pass

# Start non-blocking global keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print(f"Streaming keyboard state to Simulink on {UDP_IP}:{UDP_PORT}...")
print("Controls: W/S = Pitch | A/D = Roll")
print("Press Ctrl+C in terminal to stop.")

try:
    while True:
        # Axis 1: Forward / Backward (+1, 0, -1)
        fwd = 0.0
        if 'w' in pressed_keys:
            fwd += 0.07 #change this parameter to get control over sensitivity
        if 's' in pressed_keys:
            fwd -= 0.07 #change this parameter to get control over sensitivity

        # Axis 2: Left / Right Steering (-1, 0, +1)
        steer = 0.0
        if 'd' in pressed_keys:
            steer -= 0.07 #change this parameter to get control over sensitivity
        if 'a' in pressed_keys:
            steer += 0.07 #change this parameter to get control over sensitivity

        # Pack two doubles ('dd') -> [Forward, Steering]
        packed_data = struct.pack('dd', fwd, steer)
        sock.sendto(packed_data, (UDP_IP, UDP_PORT))

        # 200 Hz update loop (5 ms period)
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nStopping UDP stream...")
    sock.close()
    listener.stop()