# caption_generator.py

import random

# Caption ideas based on mood and style
caption_templates = {
    "casual outfit": [
        "Serving soft looks and chill vibes 😌",
        "Comfy, cool, and totally in control.",
        "Laid-back never looked so good 👟"
    ],
    "formal wear": [
        "Dressed to impress 💼✨",
        "Classy with a hint of boss energy 💅",
        "Elegance is the only option tonight."
    ],
    "streetwear": [
        "Outfit louder than my playlist 🎧",
        "Street style royalty reporting in 👑",
        "Walkin’ like I own the sidewalk 🖤"
    ],
    "business attire": [
        "Coffee in one hand, confidence in the other ☕💼",
        "CEO vibes even before 9 AM.",
        "Boardroom baddie mode: ON 🔥"
    ],
    "party dress": [
        "Too glam to give a damn 💃",
        "Sparkles, sass, and a whole lotta slay ✨",
        "This dress? Yeah, it *chose* me."
    ],
    "sportswear": [
        "Sweat but make it fashion 💦🔥",
        "Leg day fit check 🏋️‍♀️",
        "Athleisure is a lifestyle."
    ],
    "vintage look": [
        "Straight outta the time machine 📼",
        "Old soul, fresh style 👗",
        "Retro vibes only 🕶️"
    ],
    "boho style": [
        "Boho mood, barefoot soul 🌻",
        "Layers, lace, and lovely things ☮️",
        "Channeling flower child energy."
    ],
    "edgy fashion": [
        "Built this look from bricks and attitude 🔥",
        "Dark mode: activated ⚡",
        "Edgy is my aesthetic 🖤"
    ],
    "minimalist fashion": [
        "Less, but better ✨",
        "Monochrome mood today 🧊",
        "Simplicity is my statement."
    ]
}

def generate_caption(mood: str, score: float, style: str = "sassy") -> str:
    mood = mood.lower()
    if mood in caption_templates:
        return random.choice(caption_templates[mood])
    else:
        return "Just me and my fit, doing our thing 💁‍♀️"
