# TODO: "Manually" Pulls data from this website:
#  https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/sdwis_fed_reports_public/200
#  Since there isn't an API for retrieving data from their database, I made
#  this program to auto-click and download all of our necessary datasets.
import pyautogui
import time
from pynput.mouse import Listener


# Used to figure out x,y positions of your mouse clicks for your automator.
def figureOutClickPositions():
    def on_click(x, y, button, pressed):
        if button == button.left and pressed:
            print(f"Clicked at position (x={x}, y={y})")

    # Start listening for mouse clicks
    with Listener(on_click=on_click) as listener:
        listener.join()


# Runs mouse automator indefinitely.
def runAutomator():
    time.sleep(4)  # Gives you time to open chrome

    while True:
        pyautogui.moveTo(1547, 1735, duration=0.25)  # Go to position to select new state
        pyautogui.scroll(-24)  # Scroll to next state
        pyautogui.moveTo(1547, 1735, duration=0.25)  # Mouse jiggle LuL
        pyautogui.click()  # Select new state
        time.sleep(1)

        pyautogui.moveTo(3596, 773, duration=0.25)  # Queries our preferences
        pyautogui.click()
        time.sleep(15)  # Waits for query to finish

        pyautogui.moveTo(3469, 1368, duration=0.25)  # Downloads report
        pyautogui.click()
        time.sleep(15)  # Waits for download to finish

        pyautogui.moveTo(3526, 1051, duration=0.25)  # Gets us back to home screen
        pyautogui.click()

        # Wait, in case human overwrite is wanted
        time.sleep(4)


# TODO: This is main.
# figureOutClickPositions()  # Figures out the positions of your clicks.
runAutomator()  # After figuring out positions of your clicks & adding it to the code, run this to automate mouse.
