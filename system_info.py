import platform
import socket
import psutil
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Function to get system information
def get_system_info():
    system_info = platform.uname()
    print("Voice Assistant: System Information:")
    speaker.speak("System Information")

    print(f" System: {system_info.system}")
    speaker.speak(f"System {system_info.system}")

    print(f" Node Name: {system_info.node}")
    speaker.speak(f"Node Name {system_info.node}")

    print(f" Release: {system_info.release}")
    speaker.speak(f"Release {system_info.release}")

    print(f" Version: {system_info.version}")
    speaker.speak(f"Version {system_info.version}")

    print(f" Machine: {system_info.machine}")
    speaker.speak(f"Machine {system_info.machine}")

    print(f" Processor: {system_info.processor}")
    speaker.speak(f"Processor {system_info.processor}")


# Function to get network information
def get_network_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(
        f"Voice Assistant: Network Information - "
        f"Host Name: {host_name}, IP Address: {ip_address}"
    )
    speaker.speak(
        f"Network Information. Host Name {host_name}. "
        f"IP Address {ip_address}"
    )


# Function to get disk usage
def get_disk_usage():
    partitions = psutil.disk_partitions()
    print("Voice Assistant: Disk Usage:")
    speaker.speak("Disk Usage")

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        print(
            f" Partition {partition.device}: "
            f"Total: {usage.total / (1024 ** 3):.2f} GB, "
            f"Used: {usage.used / (1024 ** 3):.2f} GB, "
            f"Free: {usage.free / (1024 ** 3):.2f} GB"
        )
        speaker.speak(
            f"Partition {partition.device}. "
            f"Total {usage.total / (1024 ** 3):.2f} gigabytes. "
            f"Used {usage.used / (1024 ** 3):.2f} gigabytes. "
            f"Free {usage.free / (1024 ** 3):.2f} gigabytes"
        )


# Function to get CPU usage
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    print("Voice Assistant: CPU Usage:")
    speaker.speak("CPU Usage")

    for i, usage in enumerate(cpu_usage, start=1):
        print(f" Core {i}: {usage}%")
        speaker.speak(f"Core {i} usage {usage} percent")


# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    print(
        f"Voice Assistant: Memory Usage - "
        f"Total: {memory.total / (1024 ** 3):.2f} GB, "
        f"Used: {memory.used / (1024 ** 3):.2f} GB, "
        f"Free: {memory.available / (1024 ** 3):.2f} GB"
    )
    speaker.speak(
        f"Memory usage. Total {memory.total / (1024 ** 3):.2f} gigabytes. "
        f"Used {memory.used / (1024 ** 3):.2f} gigabytes. "
        f"Free {memory.available / (1024 ** 3):.2f} gigabytes"
    )


# Function to get battery status (for laptops)
def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            print(
                f"Voice Assistant: Battery Status - "
                f"Percentage: {battery.percent}%, "
                f"Power Plugged In: {battery.power_plugged}"
            )
            speaker.speak(
                f"Battery percentage {battery.percent} percent. "
                f"Power plugged in {battery.power_plugged}"
            )
        else:
            print("Voice Assistant: Battery information not available.")
            speaker.speak("Battery information not available")
    except Exception as e:
        print(f"Voice Assistant: Error retrieving battery status - {e}")
        speaker.speak("Error retrieving battery status")


# Function to get CPU temperature
def get_cpu_temperature():
    try:
        temperature = psutil.sensors_temperatures()
        cpu_temperature = (
            temperature["coretemp"][0].current
            if "coretemp" in temperature
            else None
        )

        if cpu_temperature:
            print(f"Voice Assistant: CPU Temperature: {cpu_temperature}°C")
            speaker.speak(
                f"CPU temperature {cpu_temperature} degrees Celsius"
            )
        else:
            print("Voice Assistant: CPU temperature information not available.")
            speaker.speak("CPU temperature information not available")
    except Exception as e:
        print(f"Voice Assistant: Error retrieving CPU temperature - {e}")
        speaker.speak("Error retrieving CPU temperature")
