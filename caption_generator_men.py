# caption_generator_men.py

import random

caption_templates = {
    "streetwear": [
        "Hood up, game on. 🎧",
        "Outfit louder than my playlist.",
        "Walk like the sidewalk’s yours."
    ],
    "business attire": [
        "CEO mode: activated 💼",
        "Boardroom fit, battle ready.",
        "Sharp lines, sharper mindset."
    ],
    "casual outfit": [
        "Basic but never boring.",
        "Comfy fit. Confident walk.",
        "Low effort. High impact."
    ],
    "ethnic wear": [
        "Sherwani supremacy 💥",
        "Desi & deadly 🕌",
        "Kurtas > everything today."
    ],
    "sportswear": [
        "Built different. Lift heavier 💪",
        "Run it. Rep it. Rock it.",
        "Athleisure? Nah. Athle-king."
    ],
    "party wear": [
        "Black shirt, big night.",
        "Dress code: jaw drop.",
        "Party fit: secured 🔥"
    ],
    "minimalist fashion": [
        "Monochrome menace.",
        "No flex. Just finesse.",
        "Minimal moves. Max impact."
    ]
}

def generate_caption(mood: str, score: float, style: str = "bold") -> str:
    mood = mood.lower()
    return random.choice(caption_templates.get(mood, ["Just the right drip."]))
