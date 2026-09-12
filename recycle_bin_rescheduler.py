# File: recycle_bin_rescheduler.py
# Main reason for this script is to automate scheduling the process of emptying the recycle bin.
#Revision History:
#   v1.0 - Initial version: Added variables to schedule the emptying of the recycle bin using Windows Task Scheduler. (September 7, 2026)

import os  
import sys
import win32com.client


def schedule_recycle_bin_emptying():

    # script path to automate_recycle_bin.py
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "automate_recycle_bin.py") 
    script_path = os.path.join(script_dir, "automate_recycle_bin.py")  

    # Get the path to the Python executable
    pythonw_path = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")

    # Create a Task Scheduler object
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    root_folder = scheduler.GetFolder("\\")

    # Wanna create a task for the task scheduler.
    task_def = scheduler.NewTask(0)

    # Set the task's properties
    task_def.RegistrationInfo.Description = "Automated Recycle Bin Emptying"
    task_def.RegistrationInfo.Author = "Automated Recycle Bin Script"

    settings = task_def.Settings
    settings.Enabled = True
    settings.StartWhenAvailable = True
    settings.Hidden = False

    trigger = task_def.Triggers.Create(4)  # 4 = Monthly trigger
    trigger.StartBoundary = "2026-10-11T00:00:00"  # Set the start date and time
    trigger.MonthsOfYear = 4095  # Set to all months to run the task
    trigger.DaysOfMonth = 1  # Set the day of the month to run the task

    action = task_def.Actions.Create(0)  # 0 = Execute action
    action.Path = pythonw_path 
    action.Arguments = f'"{script_path}"'  # Pass the script path as an argument
    action.WorkingDirectory = script_dir  # Set the working directory to the script's directory

    task_name = "Automated Recycle Bin Emptying"


    # Register the task
    root_folder.RegisterTaskDefinition(
        task_name,
        task_def,
        6, 
        None,  # No user
        None,  # No password
        3,  # Run with highest privileges
    )

    print(f"Task '{task_name}' has been scheduled successfully to run monthly on the 1st day of each month at 00:00.")


if __name__ == "__main__":
    try:
        schedule_recycle_bin_emptying()
    except Exception as e:
        print(f"An error occurred while scheduling the task: {e}")
        