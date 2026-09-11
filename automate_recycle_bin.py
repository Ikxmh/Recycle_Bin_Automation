# File: automate_recycle_bin.py
# Main reason for this script is to automate scheduling the process of emptying the recycle bin.
#Revision History: 
#   v1.0 - Initial version: Added the functionality to empty the recycle bin and handle exceptions. (September 5, 2026)
# Added the main function to call the empty_recycle_bin function when the script is executed directly. (September 7, 2026)
import os
import winshell

for item in winshell.recycle_bin():
    original_path = item.original_filename()

# Function to empty the recycle bin
def empty_recycle_bin():

    if original_path.lower().endswith(('.mp4', '.mkv')):
        try:
            # Empty the recycle bin
            item.ultraandestory()
            print("Recycle bin emptied successfully.")
        except Exception as e:
            print(f"An error occurred while emptying the recycle bin: {e} or it is already empty.")

if __name__ == "__main__":
    empty_recycle_bin()