import os

# Define directories
image_dir = "data/images"
label_dir = "data/labels"

# Ensure the label directory exists
os.makedirs(label_dir, exist_ok=True)

# Define labels for the images
labels = {
    "cat1.jpg": "cat",
    "cat2.jpg": "cat",
    "dog1.jpg": "dog",
    "dog2.jpg": "dog",
}

# Generate label files
for image_name, label in labels.items():
    label_file = os.path.join(label_dir, f"{os.path.splitext(image_name)[0]}.txt")
    with open(label_file, "w") as file:
        file.write(label)

print(f"Label files created in {label_dir}")
import torch
import torchvision.transforms as transforms
from PIL import Image

class SimpleCatDogModel:
    def __init__(self, model_path=None):
        """
        Initialize the model. If a model_path is provided, it loads a pre-trained model.
        Otherwise, it initializes a simple feedforward neural network.
        """
        if model_path:
            self.model = torch.load(model_path)
        else:
            # Initialize a simple model for demonstration purposes
            self.model = torch.nn.Sequential(
                torch.nn.Linear(3 * 224 * 224, 128),
                torch.nn.ReLU(),
                torch.nn.Linear(128, 2),  # Output layer for 2 classes: cat and dog
                torch.nn.Softmax(dim=1)
            )
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def predict(self, image_path):
        """
        Predict whether the input image is a cat or a dog.

        Args:
            image_path (str): Path to the image file.

        Returns:
            dict: A dictionary containing the label and confidence.
        """
        # Load and preprocess the image
        image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        # Perform inference
        with torch.no_grad():
            outputs = self.model(input_tensor)

        # Get the predicted class and confidence
        confidence, predicted_class = torch.max(outputs, 1)
        class_map = {0: "cat", 1: "dog"}
        return {
            "label": class_map[predicted_class.item()],
            "confidence": confidence.item()
        }

    def save_model(self, save_path):
        """
        Save the trained model to a file.

        Args:
            save_path (str): Path to save the model.
        """
        torch.save(self.model, save_path)

if __name__ == "__main__":
    # Example usage
    model = SimpleCatDogModel()
    prediction = model.predict("data/images/cat1.jpg")
    print(prediction)
