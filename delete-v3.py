import pyautogui
import time

def delete_message():
    # Move to the location of the message delete option
    # Coordinates will need to be adjusted based on your screen resolution and UI layout
    pyautogui.moveTo(1209, 630)  # Move the mouse to the message
    pyautogui.click(button='right')  # Right click the message
    time.sleep(0.5)  # Wait for the context menu to open
    pyautogui.moveTo(1325, 860)  # Move to 'Delete Message' in the context menu
    pyautogui.click()  # Click 'Delete Message'
    time.sleep(0.5)  # Wait for the delete confirmation dialog
    pyautogui.press('enter')  # Press 'Enter' to confirm deletion

# Example of running the delete function multiple times
if __name__ == '__main__':
    time.sleep(2)
    for _ in range(5000):  # Adjust the range for the number of messages
        
        delete_message()
        time.sleep(0.5)  # Wait 2 seconds before the next operation
