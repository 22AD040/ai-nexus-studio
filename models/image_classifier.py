from transformers import pipeline
from PIL import Image

classifier = pipeline("image-classification")

def classify_image(image):
    results = classifier(image)
    return results[:3]