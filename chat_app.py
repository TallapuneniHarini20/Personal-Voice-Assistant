import wikipedia
import pyttsx3


def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        print("Voice Assistant:", summary)
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Multiple results found. Please be more specific. {e}")
        return f"Multiple results found. Please be more specific. {e}"

    except wikipedia.exceptions.PageError as e:
        print(f"Sorry, I couldn't find any information on {query}. {e}")
        return f"Sorry, I couldn't find any information on {query}. {e}"


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
