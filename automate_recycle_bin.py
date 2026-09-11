# File: automate_recycle_bin.py
# Main reason for this script is to automate scheduling the process of emptying the recycle bin.
#Revision History: 
#   v1.0 - Initial version: Added the functionality to empty the recycle bin and handle exceptions. (September 5, 2026)
# Added the main function to call the empty_recycle_bin function when the script is executed directly. (September 7, 2026)
import os
import winshell

# Function to empty the recycle bin
def empty_recycle_bin():

    for item in winshell.recycle_bin():

        try:
            original_path = item.original_filename()
            if original_path.lower().endswith(('.mp4', '.mkv')):
                bin_file_path = item.real_filename()

                if (bin_file_path and os.path.isfile(bin_file_path)):
                    os.remove(bin_file_path)
                    print(f"Deleted: {bin_file_path}")
                else:
                    print(f"File not found in recycle bin: {bin_file_path}")
        except FileNotFoundError:
            print(f"File not found in recycle bin: {item.real_filename()}")
        except Exception as e:
            print(f"Error processing item: {e}")

if __name__ == "__main__":
    empty_recycle_bin()