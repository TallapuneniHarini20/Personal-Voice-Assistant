import parsedatetime
import threading
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def schedule_reminder(message, remind_at, speaker):
    cal = parsedatetime.Calendar()
    remind_at = cal.parseDT(remind_at)[0]

    current_time = time.time()
    time_difference = remind_at.timestamp() - current_time

    if time_difference > 0:
        print(
            f"Voice Assistant: Reminder scheduled for '{remind_at}' "
            f"with message: {message}"
        )
        speaker.speak(
            f"Reminder scheduled for {remind_at} with message {message}"
        )

        # Use a threading timer to schedule the reminder
        reminder_timer = threading.Timer(
            time_difference,
            remind,
            args=(message, speaker)
        )
        reminder_timer.start()

    else:
        print("Voice Assistant: Please provide a future time for the reminder.")
        speaker.speak("Please provide a future time for the reminder.")


def remind(message, speaker):
    print(f"Voice Assistant: Reminder: {message}")
    speaker.speak(f"Reminder: {message}")
