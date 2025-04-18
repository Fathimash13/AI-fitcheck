# mood_mapper_men.py

import random

style_tips = {
    "streetwear": [
        "Layer a bomber jacket over basics.",
        "Try color contrast with sneakers."
    ],
    "business attire": [
        "Sharp cuts + navy = boardroom power.",
        "Add a watch. Subtle but strong."
    ],
    "casual outfit": [
        "Rolled sleeves level up basics.",
        "Go neutral with a pop of color."
    ],
    "ethnic wear": [
        "Pair that kurta with mojaris.",
        "Layered bandhgalas = timeless drip."
    ],
    "sportswear": [
        "Compression wear under mesh = elite.",
        "Gym-to-street done right."
    ],
    "party wear": [
        "Add a chain or bracelet for edge.",
        "Leather shoes > sneakers tonight."
    ],
    "minimalist fashion": [
        "Stick to 2 tones. Let fit speak.",
        "Tailored always wins."
    ]
}

def get_style_tip(mood: str) -> str:
    mood = mood.lower()
    return random.choice(style_tips.get(mood, ["Confidence is the best fit."]))
