import pytest
from src.services.mock_service import MockService

# TODO is to test the mock service in all possible scenarios
# - Success case
# - Invalid image path
# - Load image failure
# - Prediction failure bacause of invalid image type
# - Prediction failure because of model error

# Define test data
VALID_IMAGE_PATH = "C:/Users/eng-m/Desktop/Workspace/orbem-ai-testing-challenge/data/images/cat1.jpg"
INVALID_IMAGE_PATH = "data/images/invalid.txt"
NON_EXISTENT_IMAGE_PATH = "data/images/non_existent.jpg"

@pytest.fixture
def service():
    """
    Fixture to initialize the MockService.
    """
    return MockService()

def test_send_image_success(service, mocker):
    """
    Test the full workflow for a valid image.
    """
    # Mock dependencies
    mocker.patch("src.model.mocked_model.SimpleCatDogModel.predict", return_value={
        "label": "cat",
        "confidence": 0.95
    })

    # Call the service
    response = service.send_image(VALID_IMAGE_PATH)

    # Assertions
    assert response["status"] == "success"
    assert response["data"]["label"] == "cat"
    assert 0.8 <= response["data"]["confidence"] <= 1.0

def test_send_image_invalid_path(service):
    """
    Test the service with an invalid image path.
    """
    response = service.send_image(None)
    assert response["status"] == "error"
    assert response["error_code"] == 400
    assert "Invalid image path" in response["message"]

def test_send_image_load_failure(service, mocker):
    """
    Test the service when the image cannot be loaded.
    """
    # Mock dependencies
    mocker.patch("src.utils.helpers.load_image", return_value=None)

    # Call the service
    response = service.send_image(NON_EXISTENT_IMAGE_PATH)

    # Assertions
    assert response["status"] == "error"
    assert response["error_code"] == 404
    assert "Unable to load image" in response["message"]

def test_send_image_prediction_failure(service, mocker):
    """
    Test the service when the model prediction fails.
    """
    # Mock dependencies
    mocker.patch("src.utils.helpers.load_image", return_value="mocked_image")
    mocker.patch("src.model.mocked_model.SimpleCatDogModel.predict", side_effect=Exception("Prediction error"))

    # Call the service
    response = service.send_image(VALID_IMAGE_PATH)
    print(response)

    # Assertions
    assert response["status"] == "error"
    assert "Prediction error" in response["message"]