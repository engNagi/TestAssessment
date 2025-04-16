import os
import pytest
from src.utils.data_validator import validate_image_file, validate_label_file, validate_data

# Define paths and extensions
IMAGE_FOLDER = "data/images/"
LABEL_FOLDER = "data/labels/"
IMAGE_EXTENSIONS = [".jpg", ".png", ".jpeg", ".bmp", ".gif"]

@pytest.mark.parametrize("image_path", [
    os.path.join(root, file)
    for root, _, files in os.walk(IMAGE_FOLDER)
    for file in files
    if any(file.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)
])
def test_image_files(image_path):
    """Test that all image files in the folder are valid."""
    assert validate_image_file(image_path), f"Invalid image: {image_path}"

@pytest.mark.parametrize("label_path", [
    os.path.join(root, file)
    for root, _, files in os.walk(LABEL_FOLDER)
    for file in files
    if file.lower().endswith(".txt")
])
def test_label_files(label_path):
    """Test that all label files in the folder are valid."""
    assert validate_label_file(label_path), f"Invalid label: {label_path}"

@pytest.mark.parametrize("image_path,label_path", [
    (os.path.join(root, file), os.path.join(LABEL_FOLDER, os.path.splitext(file)[0] + ".txt"))
    for root, _, files in os.walk(IMAGE_FOLDER)
    for file in files
    if any(file.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)
])
def test_image_and_label_pair(image_path, label_path):
    """Test that each image has a corresponding valid label."""
    assert validate_data(image_path, label_path), f"Invalid pair: {image_path}, {label_path}"