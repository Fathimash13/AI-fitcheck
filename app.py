import streamlit as st
from PIL import Image
from image_utils import rate_outfit
from mood_mapper import get_style_tip
from caption_generator import generate_caption


st.set_page_config(page_title="AI FitCheck 👗", layout="centered")

st.title("👗 AI FitCheck – Outfit Rater + Mood Matcher")
st.write("Upload your outfit photo and get a fit score and mood match!")

# Upload image
uploaded_file = st.file_uploader("Upload an outfit photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Look 🔍", use_container_width=True)


    # ✅ Get outfit rating and fashion mood using CLIP
    score, mood = rate_outfit(image)

    # ✅ Get tip based on detected mood
    tip = get_style_tip(mood)

    # ✅ Get GPT-powered caption
    caption = generate_caption(mood, score, style="sassy")

    st.subheader(f"✨ Rating: {score}/10")
    st.markdown(f"🧠 **Mood Match:** {mood.capitalize()}")
    st.markdown(f"💡 *Style Tip:* {tip}")
    st.markdown(f"📸 *Insta Caption:* \"{caption}\"")
