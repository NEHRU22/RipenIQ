import os
import tensorflow as tf
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "banana_model.keras")

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = [
    "overripe",
    "ripe",
    "rotten",
    "unripe"
]

BANANA_INFO = {
    "overripe": {
        "shelf_life": "1-2 day",
        "recommendation": "Consume today or tommorow or feed to any animal"
    },
    "ripe": {
        "shelf_life": "3-4 days",
        "recommendation": "Best time to consume"
    },
    "rotten": {
        "shelf_life": "Expired",
        "recommendation": "Do not consume"
    },
    "unripe": {
        "shelf_life": "6-8 days",
        "recommendation": "Store at room temperature away from fruit bugs"
    }
}

def predict_banana(image_path):

    image = Image.open(image_path).convert("RGB")
    image = image.resize((224,224))

    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    preds = model.predict(image, verbose=0)

    idx = np.argmax(preds)

    prediction = CLASS_NAMES[idx]

    confidence = float(np.max(preds) * 100)

    return {
        "prediction": prediction,
        "confidence": round(confidence,2),
        "shelf_life": BANANA_INFO[prediction]["shelf_life"],
        "recommendation": BANANA_INFO[prediction]["recommendation"]
    }
