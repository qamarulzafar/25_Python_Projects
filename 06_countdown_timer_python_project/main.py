# countdown_timer_python_project


import time

print("Countdown Timer")
seconds = int(input('Enter Time in Seconds:'))


while seconds > 0 :
    mins, secs = divmod(seconds, 60)
    timer = f'{mins:02d}: {secs:02d}'
    print("Time Left:", timer, end='\r')
    time.sleep(1)
    seconds -= 1

print('\n Times up ! ')