# main_app.py

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from image_utils import rate_outfit
from event_matcher import match_event
import io

# Style modules
import caption_generator
import mood_mapper
import caption_generator_men
import mood_mapper_men

# Setup
st.set_page_config(page_title="AI FitCheck – Choose Your Vibe", layout="centered")

# 💅 Add custom silk fashion background + layout
st.markdown("""
    <style>
    body {
        background-image: url('https://i.ibb.co/pBDjYbH/silk-bg.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 3rem;
        border-radius: 25px;
        max-width: 900px;
        margin: 4rem auto;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
        color: #E91E63;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        text-align: center;
    }

    .stRadio > div {
        flex-direction: row;
        justify-content: center;
        gap: 2rem;
    }

    .stButton>button {
        background-color: #E91E63;
        color: white;
        border-radius: 30px;
        padding: 0.5rem 1.3rem;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #d81b60;
        transform: scale(1.03);
    }

    .stFileUploader, .stDownloadButton {
        background-color: #FFF0F5;
        border: 2px dashed #E91E63;
        border-radius: 12px;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("✨ AI FitCheck")
st.subheader("Choose your fit analysis experience:")

# Style selection
style_type = st.radio(
    "Pick your vibe:",
    ["👗 AI FitCheck (All Styles)", "👔 AI FitCheck for Men"],
    horizontal=True
)

# Image uploader
uploaded_file = st.file_uploader("Upload your outfit photo", type=["jpg", "jpeg", "png"])

# Style Card Generator
def generate_style_card(image, mood, score, tip, caption, event, title="AI FitCheck Style Card"):
    base = image.convert("RGB").resize((500, 500))
    card = Image.new("RGB", (500, 800), "white")
    card.paste(base, (0, 0))
    draw = ImageDraw.Draw(card)

    try:
        font = ImageFont.truetype("arial.ttf", 18)
        font_bold = ImageFont.truetype("arialbd.ttf", 20)
        font_title = ImageFont.truetype("arialbd.ttf", 24)
    except:
        font = font_bold = font_title = ImageFont.load_default()

    draw.line((0, 500, 500, 500), fill="lightgray", width=2)

    y = 510
    x = 20
    spacing = 30

    draw.text((x, y), f"✨ {title}", fill="black", font=font_title)
    y += spacing + 5
    draw.text((x, y), f"👗 Mood: {mood.capitalize()}", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"🌟 Rating: {score}/10", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"💡 Tip: {tip}", fill="black", font=font)
    y += spacing * 2
    draw.text((x, y), f"🎯 Event: {event}", fill="black", font=font_bold)
    y += spacing * 2
    draw.text((x, y), "📸 Caption:", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"{caption}", fill="black", font=font)
    y += spacing * 2
    draw.text((x, y), f"🪄 Powered by {title}", fill="gray", font=font)

    return card

# Process uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Look 🔍", use_container_width=True)

    score, mood = rate_outfit(image)

    # Gender-specific logic
    if style_type == "👔 AI FitCheck for Men":
        tip = mood_mapper_men.get_style_tip(mood)
        caption = caption_generator_men.generate_caption(mood, score)
        title = "AI FitCheck – Men's Style Card"
    else:
        tip = mood_mapper.get_style_tip(mood)
        caption = caption_generator.generate_caption(mood, score)
        title = "AI FitCheck Style Card"

    event = match_event(mood)

    # Display results
    st.subheader(f"✨ Rating: {score}/10")
    st.markdown(f"🧠 **Mood Match:** {mood.capitalize()}")
    st.markdown(f"💡 *Style Tip:* {tip}")
    st.markdown(f"📸 *Insta Caption:* \"{caption}\"")
    st.markdown(f"🎯 *Event Match:* {event}")

    # Download text
    style_card_text = f"""
    🔍 {title}
    --------------------------
    👗 Mood Match: {mood.capitalize()}
    ✨ Rating: {score}/10
    💡 Style Tip: {tip}
    🎯 Event Match: {event}
    📸 Caption: {caption}
    """
    st.download_button(
        label="📥 Download Style Card (.txt)",
        data=style_card_text,
        file_name="fitcheck_card.txt",
        mime="text/plain"
    )

    # Download image
    style_card_img = generate_style_card(image, mood, score, tip, caption, event, title)
    buf = io.BytesIO()
    style_card_img.save(buf, format="PNG")
    byte_img = buf.getvalue()

    st.download_button(
        label="🖼️ Download Style Card (PNG)",
        data=byte_img,
        file_name="fitcheck_card.png",
        mime="image/png"
    )
