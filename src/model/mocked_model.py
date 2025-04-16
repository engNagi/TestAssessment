import random
import os
import imghdr

class SimpleCatDogModel:
    """
    A mock model to simulate predictions for 'cat' or 'dog'.
    """

    def __init__(self):
        self.classes = ["cat", "dog"]

    def validate_image(self, image_path):
        """
        Validate that the image path exists and is a valid image file.

        Args:
            image_path (str): Path to the image file.

        Raises:
            ValueError: If the image path does not exist or is not a valid image.
        """
        
        if not os.path.exists(image_path):
            raise ValueError(f"The file '{image_path}' does not exist.")
        
        
        if imghdr.what(image_path) not in ["jpeg", "png", "bmp", "gif"]:
            raise ValueError(f"The file '{image_path}' is not a valid image.")
    
    def predict(self, image_path):
        """
        Simulate predicting whether an image contains a cat or a dog.

        Args:
            image_path (str): Path to the image file.

        Returns:
            dict: A dictionary with a simulated label and confidence.
        """
        
        self.validate_image(image_path)

        # Simulated prediction
        label = random.choice(self.classes)  # Randomly choose 'cat' or 'dog'
        confidence = round(random.uniform(0.8, 1.0), 2)  # Randomly generate high confidence
        return {"label": label, "confidence": confidence}
