import os
from PIL import Image

def validate_image_file(image_path):
    """
    Validate that the provided file exists, is readable, and is a valid image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        bool: True if the file is valid, False otherwise.
    """
    if not os.path.exists(image_path):
        print(f"Error: File does not exist: {image_path}")
        return False

    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify that it is, indeed, an image
        return True
    except (IOError, SyntaxError) as e:
        print(f"Error: Invalid image file: {image_path}. {e}")
        return False

def validate_label_file(label_path):
    """
    Validate that the provided label file exists and contains valid content.

    Args:
        label_path (str): Path to the label file.

    Returns:
        bool: True if the label file is valid, False otherwise.
    """
    if not os.path.exists(label_path):
        print(f"Error: File does not exist: {label_path}")
        return False

    try:
        with open(label_path, "r") as file:
            content = file.read().strip()
            if not content:
                print(f"Error: Label file is empty: {label_path}")
                return False
            return True
    except Exception as e:
        print(f"Error: Unable to read label file: {label_path}. {e}")
        return False

def validate_data(image_path, label_path):
    """
    Validate both the image and the label file.

    Args:
        image_path (str): Path to the image file.
        label_path (str): Path to the label file.

    Returns:
        bool: True if both files are valid, False otherwise.
    """
    image_valid = validate_image_file(image_path)
    label_valid = validate_label_file(label_path)

    if not image_valid:
        print(f"Image validation failed for: {image_path}")
    if not label_valid:
        print(f"Label validation failed for: {label_path}")

    return image_valid and label_valid

if __name__ == "__main__":
    # Example usage
    image_path = "data/images/cat1.jpg"
    label_path = "data/labels/cat1.txt"

    if validate_data(image_path, label_path):
        print("Both image and label are valid.")
    else:
        print("Validation failed.")
