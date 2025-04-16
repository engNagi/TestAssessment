import os
from PIL import Image

def load_image(image_path):
    """
    Load an image from a file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        PIL.Image.Image or None: Loaded image object if successful, None otherwise.
    """
    if not os.path.exists(image_path):
        print(f"Error: File does not exist: {image_path}")
        return None

    try:
        return Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error: Unable to load image: {image_path}. {e}")
        return None

def save_image(image, save_path):
    """
    Save a PIL Image object to a specified path.

    Args:
        image (PIL.Image.Image): The image object to save.
        save_path (str): Path where the image will be saved.

    Returns:
        bool: True if the image was saved successfully, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Error: Unable to save image: {save_path}. {e}")
        return False

def list_files_in_directory(directory, extensions=None):
    """
    List all files in a directory with optional filtering by extensions.

    Args:
        directory (str): Path to the directory.
        extensions (list or None): List of file extensions to filter by (e.g., [".jpg", ".png"]).

    Returns:
        list: List of file paths matching the criteria.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory does not exist: {directory}")
        return []

    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions is None or any(file.lower().endswith(ext) for ext in extensions):
                all_files.append(os.path.join(root, file))

    return all_files

def read_text_file(file_path):
    """
    Read the contents of a text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the file as a string, or an empty string if an error occurs.
    """
    if not os.path.exists(file_path):
        print(f"Error: File does not exist: {file_path}")
        return ""

    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error: Unable to read file: {file_path}. {e}")
        return ""

def write_text_file(file_path, content):
    """
    Write content to a text file.

    Args:
        file_path (str): Path to the text file.
        content (str): Content to write to the file.

    Returns:
        bool: True if the file was written successfully, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error: Unable to write to file: {file_path}. {e}")
        return False

if __name__ == "__main__":
    # Example usage
    directory = "C:/Users/eng-m/Desktop/Workspace/orbem-ai-testing-challenge/data/images"
    image_files = list_files_in_directory(directory, extensions=[".jpg", ".png"])
    print("Found image files:", image_files)

    # Load an image
    if image_files:
        image = load_image(image_files[0])
        if image:
            print("Image loaded successfully.")

    # Save the image
    if image:
        save_path = "output/saved_image.jpg"
        if save_image(image, save_path):
            print(f"Image saved to {save_path}")
