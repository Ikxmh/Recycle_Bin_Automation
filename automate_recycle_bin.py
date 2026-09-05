# File: automate_recycle_bin.py
# Main reason for this script is to automate the process of emptying the recycle bin on a Windows system. This can be useful for maintaining system performance and freeing up disk space.
#Revision History: 
#   v1.0 - Initial version: Added the functionality to empty the recycle bin and handle exceptions. (September 5, 2026)
import winshell


recycleBin = list(winshell.recycle_bin())

# Function to empty the recycle bin
def empty_recycle_bin():
    try:
        # Empty the recycle bin
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print("Recycle bin emptied successfully.")
    except Exception as e:
        print(f"An error occurred while emptying the recycle bin: {e} or it is already empty.")