
from PIL import Image
import os

def extract_dominant_colors(image_path, num_colors=5):
    img = Image.open(image_path)
    img = img.convert("RGB")
    img = img.resize((100, 100))  # Resize for faster processing

    colors = img.getcolors(img.size[0] * img.size[1])
    if colors is None:
        return []

    # Sort colors by count (most frequent first)
    colors.sort(key=lambda x: x[0], reverse=True)

    dominant_colors = []
    for count, color in colors[:num_colors]:
        dominant_colors.append(color)
    return dominant_colors

image_files = [
    '/home/ubuntu/upload/IMG_5491.jpg',
    '/home/ubuntu/upload/IMG_0494.jpg',
    '/home/ubuntu/upload/IMG_0479.jpg',
    '/home/ubuntu/upload/IMG_0482(1).jpg',
    '/home/ubuntu/upload/IMG_0600.jpg',
    '/home/ubuntu/upload/IMG_0505.jpg'
]

all_dominant_colors = []
for img_file in image_files:
    colors = extract_dominant_colors(img_file)
    all_dominant_colors.extend(colors)

# Remove duplicates and sort for consistency
all_dominant_colors = sorted(list(set(all_dominant_colors)))

print("Cores dominantes encontradas:")
for color in all_dominant_colors:
    print(f"RGB: {color}")



