from PIL import Image
import os

def resize_and_rename(input_dir):
    """
    Resizes and renames images in a given directory and its subdirectories.

    Args:
        input_dir: The path to the input directory.
    """

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)

                # Load the image
                with Image.open(file_path) as img:
                    # Resize to 72x72 and save with "@3x" suffix
                    img_72 = img.resize((72, 72))
                    new_file_path_72 = os.path.join(root, f"{os.path.splitext(file)[0]}@3x{os.path.splitext(file)[1]}")
                    img_72.save(new_file_path_72)

                    # Duplicate the image and resize to 48x48, then save with "@2x" suffix
                    img_48 = img.resize((48, 48))
                    new_file_path_48 = os.path.join(root, f"{os.path.splitext(file)[0]}@2x{os.path.splitext(file)[1]}")
                    img_48.save(new_file_path_48)

# Example usage:
input_directory = "images"
resize_and_rename(input_directory)
