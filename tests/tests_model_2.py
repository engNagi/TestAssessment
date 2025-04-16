import pytest
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

@pytest.fixture
def mock_valid_image(mocker):
    """
    Fixture to mock valid image behavior.
    """
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value="jpeg")

@pytest.fixture
def mock_invalid_image(mocker):
    """
    Fixture to mock invalid image behavior.
    """
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=True)
    mocker.patch("src.model.mocked_model.imghdr.what", return_value=None)

@pytest.fixture
def mock_non_existent_image(mocker):
    """
    Fixture to mock non-existent image behavior.
    """
    mocker.patch("src.model.mocked_model.os.path.exists", return_value=False)

def test_validate_image_success(model, mock_valid_image):
    """
    Test that valid image files pass validation.
    """
    try:
        model.validate_image(VALID_IMAGE_PATH)
    except ValueError:
        pytest.fail("validate_image raised ValueError unexpectedly!")

def test_validate_image_does_not_exist(model, mock_non_existent_image):
    """
    Test that invalid or non-existent files raise a ValueError.
    """
    # Test non-existent file
    with pytest.raises(ValueError, match="does not exist"):
        model.validate_image(NON_EXISTENT_IMAGE_PATH)


def test_validate_image_failure_invalid_image_file(model, mock_invalid_image):
    """
    Test that invalid or non-existent files raise a ValueError.
    """
    # Test invalid file type
    with pytest.raises(ValueError, match="not a valid image"):
        model.validate_image(INVALID_IMAGE_PATH)

def test_predict_output(model, mock_valid_image):
    """
    Test that the prediction output contains valid keys and values.
    """
    prediction = model.predict(VALID_IMAGE_PATH)
    assert "label" in prediction
    assert prediction["label"] in ["cat", "dog"]
    assert "confidence" in prediction
    assert 0.8 <= prediction["confidence"] <= 1.0

def test_predict_randomness(model, mock_valid_image):
    """
    Test that predictions are randomized between 'cat' and 'dog'.
    """
    labels = {model.predict(VALID_IMAGE_PATH)["label"] for _ in range(10)}
    assert "cat" in labels
    assert "dog" in labels