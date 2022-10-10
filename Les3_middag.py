import time

current_time =  time.localtime()
hour = current_time.tm_hour

print(current_time.tm_hour,":",current_time.tm_min,":",current_time.tm_sec)
if hour >= 12 and current_time.tm_hour < 18:
    print("Het is middag.")
elif current_time.tm_hour < 12:
    print("Het is ochtend.")
elif current_time.tm_hour >= 18:
    print("Het is avond")