# mood_mapper.py

import random

# Dictionary mapping fashion moods to style tips
mood_tips = {
    "casual outfit": [
        "Try layering with a denim jacket for effortless vibes.",
        "Add white sneakers to complete the chill look.",
        "Minimal jewelry = maximum impact."
    ],
    "formal wear": [
        "A sleek watch or clutch will elevate the elegance.",
        "Don’t forget to steam/iron—it makes all the difference!",
        "Pointed shoes = power move."
    ],
    "streetwear": [
        "Bold sneakers or high-tops can change the game.",
        "Try mixing neutral tones with one loud statement piece.",
        "Chunky accessories or sunglasses for the win."
    ],
    "business attire": [
        "Tuck in your shirt for a sharper look.",
        "Try subtle prints to show personality without losing professionalism.",
        "Add a statement belt or heels."
    ],
    "party dress": [
        "Strappy heels + glittery clutch = ✨",
        "Statement earrings take it to the next level.",
        "Try a bold lip color to complete the party mood."
    ],
    "sportswear": [
        "Match your socks or shoes with an accent color in your fit.",
        "Layer a cropped hoodie for dimension.",
        "Add a sporty cap or hairband for extra flair."
    ],
    "vintage look": [
        "Mix textures like suede and denim for a true vintage vibe.",
        "Add retro shades or a bandana to seal the deal.",
        "Earth tones or pastels work beautifully here."
    ],
    "boho style": [
        "Try layered necklaces or ankle boots.",
        "Fringe or tassel bags complete the look.",
        "Add a floppy hat if you’re feeling extra 🌻"
    ],
    "edgy fashion": [
        "Add dark lipstick or eyeliner for maximum edge.",
        "Mix leather with metal accessories.",
        "A distressed piece adds attitude."
    ],
    "minimalist fashion": [
        "Stick to neutral colors for a sleek finish.",
        "Focus on clean lines and high-quality fabric.",
        "A single statement piece (bag, boots) goes a long way."
    ]
}

def get_style_tip(mood: str) -> str:
    mood = mood.lower()
    tips = mood_tips.get(mood, ["You're already slaying. Keep it up! 🔥"])
    return random.choice(tips)
