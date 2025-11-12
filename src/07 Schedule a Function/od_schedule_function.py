import time
import threading

def schedule_function(scheduled_time, function, message):
    while True:
      if time.time() >= scheduled_time:
         function(message) 
         break
      else:
         time.sleep(1)

def schedule_function_in_thread(scheduled_time, function, *args, **kwargs):
    delay = max(0, scheduled_time - time.time())
    print(f"{function.__name__}() scheduled for {time.ctime(scheduled_time)}")
    threading.Timer(delay, function, args=args, kwargs=kwargs).start()

schedule_function(time.time() + 2, print, 'Howdy!')         

schedule_function_in_thread(time.time() + 2, print, 'Howdy!')         
