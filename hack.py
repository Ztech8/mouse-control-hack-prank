# Import necessary libraries
import pyautogui
import webbrowser
import time

# URL of the YouTube website
url = 'https://www.youtube.com/'

# Open the web browser and navigate to the specified URL
webbrowser.open(url)

# Pause for 3 seconds to allow the web page to load
time.sleep(3)

# Move the mouse to the specified coordinates (943, 135) and click
pyautogui.moveTo(943, 135, 3)
pyautogui.click()

# Pause for 1 second to allow the click action to take effect
time.sleep(1)

# Type the specified text ('never gonna give you up') with a 0.25-second interval between each keystroke
pyautogui.typewrite('never gonna give you up', interval=0.25)

# Pause for 0.5 seconds
time.sleep(0.5)

# Simulate pressing the 'Enter' key
pyautogui.hotkey('Enter')
