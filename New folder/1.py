import pyautogui
import time

# Give some time to focus on the text input field
time.sleep(5)

# Text to print
text_to_print = ("*Happy BirthDay Janu*")

# Number of times to print the text
num_prints = 500


for i in range(num_prints):
    pyautogui.typewrite(text_to_print + '\n')