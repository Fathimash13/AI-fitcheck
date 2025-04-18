# event_matcher.py

import random

# Mapping moods to events globally + culturally inclusive
event_map = {
    "casual outfit": [
        "Perfect for a weekend coffee run ☕",
        "Ready for a Sunday brunch 🌞",
        "Chill day with friends incoming 🎧"
    ],
    "formal wear": [
        "Boardroom ready 💼",
        "Perfect for a corporate dinner 🍽️",
        "Nailing the networking game 🔥"
    ],
    "streetwear": [
        "Made for a music festival 🎵",
        "Street style spotlight 🔥",
        "Snap-worthy city stroll 📸"
    ],
    "business attire": [
        "Nailing that client pitch 🧠",
        "Job interview perfection ✅",
        "Work hard, slay harder 💼"
    ],
    "party dress": [
        "Party mode: activated 🕺🏽",
        "Perfect for a club night 💃",
        "Dancing till sunrise ✨"
    ],
    "sportswear": [
        "Gym fit = game fit 💪",
        "Athleisure queen 👟",
        "Weekend hike vibes ⛰️"
    ],
    "vintage look": [
        "Retro brunch with the crew 🍵",
        "Thrift shop photoshoot ready 📸",
        "Old soul, new slay 💅"
    ],
    "boho style": [
        "Perfect for a beach festival 🏖️",
        "Boho wedding guest goals 💐",
        "Indie concert approved 🎶"
    ],
    "edgy fashion": [
        "Night out in Tokyo style ✨",
        "K-pop concert or cosplay con? ✔️",
        "For when you run the underground scene 🎤"
    ],
    "minimalist fashion": [
        "Gallery date in Seoul 🎨",
        "Modern dinner in the city 🍷",
        "Fashion week but make it minimalist 🖤"
    ],
    # South & East Asian cultural fits
    "ethnic wear": [
        "Mehendi night ready 🌿",
        "Diwali vibes unlocked ✨",
        "Wedding guest goals – desi edition 💍",
        "Perfect for a sangeet 💃"
    ],
    "saree look": [
        "Classic elegance for a puja 🕉️",
        "Reception-ready glamour 💎",
        "Traditional & trending for Eid 💫"
    ],
    "fusion wear": [
        "Perfect for Indo-western college fest 🎤",
        "Modern twist to tradition at Navratri 🪔",
        "Wedding cocktail party material 🍸"
    ],
    "hanbok/cheongsam inspired": [
        "Lunar New Year ready 🧧",
        "K-drama romance date vibes 🎥",
        "Cultural festival glam 💫"
    ]
}

def match_event(mood: str) -> str:
    mood = mood.lower()
    options = event_map.get(mood, ["Style works anywhere you go 🌍"])
    return random.choice(options)
