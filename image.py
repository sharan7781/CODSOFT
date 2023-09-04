import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load pre-trained ResNet for feature extraction
image_feature_extractor = hub.load("https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/5")

# Load pre-trained captioning model (LSTM or transformer)

def load_and_preprocess_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet_v2.preprocess_input(image)
    return image

def extract_image_features(image_path):
    image = load_and_preprocess_image(image_path)
    image = tf.expand_dims(image, axis=0)
    features = image_feature_extractor(image)
    return features

def generate_caption(image_path):
    image_features = extract_image_features(image_path)
    # Use the captioning model to generate captions

def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image(file_path)
        generate_caption(file_path)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

root = tk.Tk()
root.title("Image Captioning AI")

browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack()

image_label = tk.Label(root)
image_label.pack()

caption_label = tk.Label(root, text="Generated Caption:")
caption_label.pack()

generated_caption = tk.Label(root, text="")
generated_caption.pack()

root.mainloop()
