
import random

TONES = {
    "romantic": [
        "A whisper of devotion in this diff.",
        "Code written under candlelight."
    ],
    "dramatic": [
        "Let the heavens witness this refactor!"
    ],
    "soft": [
        "Just smoothing the edges."
    ],
    "chaotic": [
        "It works. Ship it."
    ]
}

def affirmation():
    return random.choice(sum(TONES.values(), []))

def poetic(tone):
    return random.choice(TONES.get(tone, TONES["romantic"]))
