from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def set_system_volume(volume):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    volume_interface.SetMasterVolumeLevelScalar(volume, None)


def change_volume(direction):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume_interface.GetMasterVolumeLevelScalar()

    if direction == "up":
        new_volume = min(1.0, current_volume + 0.1)
    elif direction == "down":
        new_volume = max(0.0, current_volume - 0.1)
    else:
        new_volume = current_volume

    volume_interface.SetMasterVolumeLevelScalar(new_volume, None)
