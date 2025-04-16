from src.utils.helpers import load_image
from src.model.mocked_model import SimpleCatDogModel

class MockService:
    """
    A mock service simulating interaction with a mocked "AI model".
    This service takes an image path, uses the SimpleCatDogModel to predict whether the image
    contains a cat or a dog, and returns a simulated API-like response.
    """

    def __init__(self):
        """Initialize the mock service with a simulated AI model for predictions."""
        self.model = SimpleCatDogModel()

    def send_image(self, image_path):
        """
        Simulate sending an image to the service and receiving a response.

        Args:
            image_path (str): Path to the image file.

        Returns:
            dict: A dictionary simulating an API response with the label and confidence.
        """
        # Validate the image path
        if not image_path or not isinstance(image_path, str):
            return {
                "status": "error",
                "error_code": 400,
                "message": "Invalid image path provided."
            }

        # Load the image
        image = load_image(image_path)
        if image is None:
            return {
                "status": "error",
                "error_code": 404,
                "message": f"Unable to load image: {image_path}"
            }

        # Use the model to make a prediction
        prediction = self.model.predict(image_path)

        # Simulate an API response
        return {
            "status": "success",
            "data": {
                "label": prediction["label"],
                "confidence": prediction["confidence"]
            }
        }

if __name__ == "__main__":
    service = MockService()
    response = service.send_image("data/images/cat1.jpg")
    print(response)
