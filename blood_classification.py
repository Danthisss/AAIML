import os
import random
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display
from datetime import datetime

# STEP 1: Folder paths for healthy and infected images
healthy_folder = r"C:\Users\preet\OneDrive\Desktop\AAIML\sample_blood_dataset\test\healthy"  # Change this to your folder path
infected_folder = r"C:\Users\preet\OneDrive\Desktop\AAIML\sample_blood_dataset\test\infected"  # Change this to your folder path

# STEP 2: Get list of all image files from both folders
healthy_images = [f for f in os.listdir(healthy_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
infected_images = [f for f in os.listdir(infected_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# STEP 3: Check if there are images in the folders
if not healthy_images and not infected_images:
    print("No images found in the folders.")
else:
    # STEP 4: Select a random image from either the healthy or infected folder
    if random.choice([True, False]):  # Randomly choose from healthy or infected
        random_image = random.choice(healthy_images)
        file_path = os.path.join(healthy_folder, random_image)
        label = "Healthy"
    else:
        random_image = random.choice(infected_images)
        file_path = os.path.join(infected_folder, random_image)
        label = "Infected"

    # STEP 5: Simulate confidence level (e.g., 85% for healthy, 75% for infected)
    confidence = random.uniform(70, 95)  # Simulating a random confidence percentage

    # STEP 6: Get image details (size, dimensions)
    img = Image.open(file_path)
    img_width, img_height = img.size
    file_size = os.path.getsize(file_path) / 1024  # Size in KB
    
    # STEP 7: Annotate the image
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()

    # Adding background for the text
    draw.rectangle((5, 5, 600, 100), fill="black")
    draw.text((10, 10), f"Prediction: {label}", font=font, fill="lime")
    draw.text((10, 40), f"Confidence: {confidence:.2f}%", font=font, fill="yellow")
    draw.text((10, 70), f"File: {random_image}", font=font, fill="white")
    draw.text((10, 100), f"Dimensions: {img_width}x{img_height}", font=font, fill="white")
    draw.text((10, 130), f"File Size: {file_size:.2f} KB", font=font, fill="white")
    draw.text((10, 160), f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", font=font, fill="white")

    # STEP 8: Display the image in notebook
    display(img)

    # STEP 9: Save the image if needed
    img.save("output.png")
    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.2f}%")
    print(f"Selected image: {random_image}")
    print(f"Dimensions: {img_width}x{img_height}")
    print(f"File Size: {file_size:.2f} KB")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Image displayed above. Saved as 'output.png'")
