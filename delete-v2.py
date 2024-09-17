import pyautogui
import time

def delete_message():
    # Move to the location of the message delete option
    # Coordinates will need to be adjusted based on your screen resolution and UI layout
    pyautogui.moveTo(390, 632)  # Move the mouse to the message
    pyautogui.click(button='right')  # Right click the message
    time.sleep(0.5)  # Wait for the context menu to open
    pyautogui.moveTo(467, 850)  # Move to 'Delete Message' in the context menu
    pyautogui.click()  # Click 'Delete Message'
    time.sleep(0.5)  # Wait for the delete confirmation dialog
    pyautogui.press('enter')  # Press 'Enter' to confirm deletion

# Example of running the delete function multiple times
for _ in range(30):  # Adjust the range for the number of messages
    time.sleep(0.5)
    delete_message()
    #time.sleep(2)  # Wait 2 seconds before the next operation
