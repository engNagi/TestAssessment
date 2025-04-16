import pytest
import pytest_mock
import os
from src.model.mocked_model import SimpleCatDogModel

# Define a valid image path for testing
VALID_IMAGE_PATH = "data/images/sample.jpg"
INVALID_IMAGE_PATH = "data/images/invalid.txt"
NON_EXISTENT_IMAGE_PATH = "data/images/non_existent.jpg"

@pytest.fixture
def model():
    """
    Fixture to initialize the mocked model.
    """
    return SimpleCatDogModel()

def test_validate_image_success(model, mocker):
    """
    Test that valid image files pass validation.
    """

    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value="jpeg")

    try:
        model.validate_image(VALID_IMAGE_PATH)
    except ValueError:
        pytest.fail("validate_image raised ValueError unexpectedly!")

def test_validate_image_failure(model, mocker):
    """
    Test that invalid or non-existent files raise a ValueError.
    """
    # Test non-existent file
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=False)
    with pytest.raises(ValueError, match="does not exist"):
        model.validate_image(NON_EXISTENT_IMAGE_PATH)

    # Test invalid file type
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value=None)
    with pytest.raises(ValueError, match="not a valid image"):
        model.validate_image(INVALID_IMAGE_PATH)

def test_predict_output(model, mocker):
    """
    Test that the prediction output contains valid keys and values.
    """
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value="jpeg")
    prediction = model.predict(VALID_IMAGE_PATH)
    assert "label" in prediction
    assert prediction["label"] in ["cat", "dog"]
    assert "confidence" in prediction
    assert 0.8 <= prediction["confidence"] <= 1.0

def test_predict_randomness(model, mocker):
    """
    Test that predictions are randomized between 'cat' and 'dog'.
    """
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value="jpeg")
    labels = {model.predict(VALID_IMAGE_PATH)["label"] for _ in range(10)}
    assert "cat" in labels
    assert "dog" in labels