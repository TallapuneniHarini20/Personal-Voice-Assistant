import requests
import win32com.client
import random

# Speaker setup
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# Function to tell a joke
def tell_joke():
    joke_api_url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(joke_api_url)
        joke_data = response.json()

        joke_setup = joke_data["setup"]
        joke_punchline = joke_data["punchline"]
        joke = f"{joke_setup} {joke_punchline}"

        print(f"Voice Assistant: Here's a joke for you:\n{joke}")
        speaker.speak("Here's a joke for you. " + joke_setup)
        speaker.speak(joke_punchline)

    except Exception as e:
        print(f"Voice Assistant: Sorry, I couldn't fetch a joke at the moment. Error: {e}")
        speaker.speak("Sorry, I couldn't fetch a joke at the moment.")


# Function to get a riddle
def get_riddle():
    riddles = [
        {
            "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "answer": "an echo"
        },
        {
            "question": "The more you take, the more you leave behind. What am I?",
            "answer": "footsteps"
        },
        {
            "question": "What has keys but can't open locks?",
            "answer": "a piano"
        },
        {
            "question": "The person who makes it, sells it. The person who buys it never uses it. What is it?",
            "answer": "a coffin"
        },
        {
            "question": "I'm tall when I'm young, and I'm short when I'm old. What am I?",
            "answer": "a candle"
        },
        {
            "question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
            "answer": "a map"
        },
        {
            "question": "I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
            "answer": "a keyboard"
        },
        {
            "question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "answer": "the letter m"
        },
        {
            "question": "I'm always hungry, I must always be fed. The finger I lick will soon turn red. What am I?",
            "answer": "a flame"
        },
        {
            "question": "I'm not alive, but I grow; I don't have lungs, but I need air. What am I?",
            "answer": "fire"
        },
        {
            "question": "I can be cracked, made, told, and played. What am I?",
            "answer": "a joke"
        },
        {
            "question": "I fly without wings. I cry without eyes. Wherever I go, darkness follows me. What am I?",
            "answer": "a cloud"
        },
        {
            "question": "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "answer": "pencil lead"
        },
        {
            "question": "What has a heart that doesn't beat?",
            "answer": "an artichoke"
        },
        {
            "question": "What has a head, a tail, is brown, and has no legs?",
            "answer": "a penny"
        }
    ]

    selected_riddle = random.choice(riddles)
    return {
        "question": selected_riddle["question"],
        "answer": selected_riddle["answer"]
    }


# Function to check riddle answer
def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()
