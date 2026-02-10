import time
import winsound as ws
import threading


def set_alarm(hour, minute):
    current_time = time.localtime()

    alarm_time = time.struct_time((
        current_time.tm_year,
        current_time.tm_mon,
        current_time.tm_mday,
        int(hour),
        int(minute),
        0, 0, 0, 0
    ))

    if alarm_time > current_time:
        time_difference = time.mktime(alarm_time) - time.mktime(current_time)
        print(f"Alarm set for {hour}:{minute}")

        # Create a separate thread to wait until alarm time
        alarm_thread = threading.Thread(
            target=sleep_until_alarm,
            args=(time_difference,)
        )
        alarm_thread.start()

    else:
        print("Invalid time. Please provide a future time.")


def sleep_until_alarm(time_difference):
    # Sleep until the alarm time is reached
    time.sleep(time_difference)

    # Play the alarm sound
    frequency = 3500   # Hertz
    duration = 2000    # milliseconds
    ws.Beep(frequency, duration)

    print("Alarm!")
