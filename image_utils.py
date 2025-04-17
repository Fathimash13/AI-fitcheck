from PIL import Image
import torch
import clip
import torchvision.transforms as transforms

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Fashion mood labels
fashion_labels = [
    "casual outfit",
    "formal wear",
    "streetwear",
    "business attire",
    "party dress",
    "sportswear",
    "vintage look",
    "boho style",
    "edgy fashion",
    "minimalist fashion"
]

@torch.no_grad()
def rate_outfit(image: Image.Image):
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(label) for label in fashion_labels]).to(device)

    image_features = model.encode_image(image_input)
    text_features = model.encode_text(text_inputs)

    logits_per_image, _ = model(image_input, text_inputs)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()[0]

    # Top label and scaled score
    top_idx = probs.argmax()
    label = fashion_labels[top_idx]
    score = round(float(probs[top_idx]) * 10, 1)

    return score, label

