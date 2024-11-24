from PIL import Image
import os

def process_images(input_dir):
    """
    Duplicates images in a directory and its subdirectories, excludes specific subdirectories,
    and processes them based on the given requirements.

    Args:
        input_dir: The path to the input directory.
    """
    for root, _, files in os.walk(input_dir):
        # Exclude specific subdirectories
        if any(excluded in root for excluded in ["images/group_dms", "images/platforms"]):
            continue  # Skip these directories and their contents

        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)

                try:
                    # Load the image
                    with Image.open(file_path) as img:
                        # Create a duplicate with @3x suffix (unchanged)
                        new_file_path_3x = os.path.join(root, f"{os.path.splitext(file)[0]}@3x{os.path.splitext(file)[1]}")
                        img.save(new_file_path_3x)

                        # Create another duplicate with @2x suffix (cropped)
                        width, height = img.size
                        crop_amount = width // 3  # Remove one-third of the width
                        img_cropped = img.crop((0, 0, width - crop_amount, height))
                        new_file_path_2x = os.path.join(root, f"{os.path.splitext(file)[0]}@2x{os.path.splitext(file)[1]}")
                        img_cropped.save(new_file_path_2x)

                    # Delete the original file
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

# Example usage:
input_directory = "images"
process_images(input_directory)
