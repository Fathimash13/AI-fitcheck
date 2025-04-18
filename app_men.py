import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from image_utils import rate_outfit
from mood_mapper_men import get_style_tip
from caption_generator_men import generate_caption
from event_matcher import match_event
import io

st.set_page_config(page_title="AI FitCheck Men 👔", layout="centered")
st.title("👔 AI FitCheck – Men's Fit Rater + Vibe Matcher")
st.write("Upload your fit and get rated with a vibe match and caption.")

# 🖼️ Style Card Generator
def generate_style_card(image, mood, score, tip, caption, event):
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

    draw.text((x, y), "🧢 AI FitCheck: Men's Style Card", fill="black", font=font_title)
    y += spacing + 5

    draw.text((x, y), f"👟 Mood: {mood.capitalize()}", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"🔥 Rating: {score}/10", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"💡 Tip: {tip}", fill="black", font=font)
    y += spacing * 2

    draw.text((x, y), f"🎯 Event Match: {event}", fill="black", font=font_bold)
    y += spacing * 2

    draw.text((x, y), "📸 Caption:", fill="black", font=font_bold)
    y += spacing
    draw.text((x, y), f"{caption}", fill="black", font=font)

    y += spacing * 2
    draw.text((x, y), "💪 Powered by AI FitCheck Men", fill="gray", font=font)

    return card

# Upload + Inference
uploaded_file = st.file_uploader("Upload your outfit photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Look 🔍", use_container_width=True)

    score, mood = rate_outfit(image)
    tip = get_style_tip(mood)
    caption = generate_caption(mood, score, style="bold")
    event = match_event(mood)

    st.subheader(f"🔥 Rating: {score}/10")
    st.markdown(f"👟 **Mood Match:** {mood.capitalize()}")
    st.markdown(f"💡 *Style Tip:* {tip}")
    st.markdown(f"📸 *Caption:* \"{caption}\"")
    st.markdown(f"🎯 *Event:* {event}")

    # Download .txt
    style_card_text = f"""
    🧢 AI FitCheck – Men's Style Card
    --------------------------
    👟 Mood Match: {mood.capitalize()}
    🔥 Rating: {score}/10
    💡 Style Tip: {tip}
    🎯 Event Match: {event}
    📸 Caption: {caption}
    """
    st.download_button(
        label="📥 Download Style Card (.txt)",
        data=style_card_text,
        file_name="fitcheck_men_card.txt",
        mime="text/plain"
    )

    # Download .png
    style_card_img = generate_style_card(image, mood, score, tip, caption, event)
    buf = io.BytesIO()
    style_card_img.save(buf, format="PNG")
    byte_img = buf.getvalue()

    st.download_button(
        label="🖼️ Download Style Card (PNG)",
        data=byte_img,
        file_name="fitcheck_men_card.png",
        mime="image/png"
    )
