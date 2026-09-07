# File: recycle_bin_rescheduler.py
# Main reason for this script is to automate scheduling the process of emptying the recycle bin.
#Revision History:
#   v1.0 - Initial version: Added variables to schedule the emptying of the recycle bin using Windows Task Scheduler. (September 7, 2026)

import os  
import sys
import win32com.client


def schedule_recycle_bin_emptying():

    # script path to automate_recycle_bin.py
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "automate_recycle_bin.py") # not sure if this is best practice? 

    # Create a Task Scheduler object
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    root_folder = scheduler.GetFolder("\\")

    # Wanna create a task for the task scheduler.
    task_def = scheduler.NewTask(0)
    
