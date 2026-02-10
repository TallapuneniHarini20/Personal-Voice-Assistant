import webbrowser
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def play_specified_song(song_name):
    search_query = f"{song_name} official audio"
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)
    print(f"Voice Assistant: Playing '{song_name}' on YouTube.")
    speaker.speak(f"Playing {song_name} on YouTube.")


def watch_specified_movie(movie_name):
    search_query = f"{movie_name} movie"
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)
    print(f"Voice Assistant: Playing '{movie_name}' on YouTube.")
    speaker.speak(f"Playing {movie_name} on YouTube.")


def play_specified_video(video_name):
    search_query = f"{video_name} official video"
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)
    print(f"Voice Assistant: Playing '{video_name}' on YouTube.")
    speaker.speak(f"Playing {video_name} on YouTube.")
