time = int(input("What is current time in Hours?"))
alarm = int(input("How many hours would you like to wait until the alarm?"))

alarmHour = (time + alarm) % 24
            
print(f"Time of alarm is {alarmHour}")

