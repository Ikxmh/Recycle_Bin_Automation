# File: automate_recycle_bin.py
# Main reason for this script is to automate scheduling the process of emptying the recycle bin.
#Revision History: 
#   v1.0 - Initial version: Added the functionality to empty the recycle bin and handle exceptions. (September 5, 2026)
# Added the main function to call the empty_recycle_bin function when the script is executed directly. (September 7, 2026)
import winshell


# Function to empty the recycle bin
def empty_recycle_bin():
    try:
        # Empty the recycle bin
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        print("Recycle bin emptied successfully.")
    except Exception as e:
        print(f"An error occurred while emptying the recycle bin: {e} or it is already empty.")

if __name__ == "__main__":
    empty_recycle_bin()