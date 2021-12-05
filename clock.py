from os import system
import basicFunctions as basic
from datetime import date, datetime
import time

#clock program
while True:
    now = datetime.now()
    basic.clearConsole()
    print("Console Clock ")

    current_date = now.date()
    current_time = now.strftime("%H:%M:%S")
    print("Current Date: ", current_date)
    print("Current Time: ", current_time)
    time.sleep(1)