from PIL import Image
import os

def resize_and_rename(input_dir):
    """
    Resizes and renames images in a given directory and its subdirectories,
    excluding specific subdirectories, and deletes the original images.

    Args:
        input_dir: The path to the input directory.
    """
    exclude_dir = os.path.join(input_dir, "images", "platforms")  # Define the subdirectory to exclude

    for root, _, files in os.walk(input_dir):
        if exclude_dir in root:  # Skip the excluded directory
            continue

        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)

                try:
                    # Load the image
                    with Image.open(file_path) as img:
                        # Resize to 72x72 and save with "@3x" suffix
                        img_72 = img.resize((72, 72))
                        new_file_path_72 = os.path.join(root, f"{os.path.splitext(file)[0]}@3x{os.path.splitext(file)[1]}")
                        img_72.save(new_file_path_72)

                        # Resize to 48x48 and save with "@2x" suffix
                        img_48 = img.resize((48, 48))
                        new_file_path_48 = os.path.join(root, f"{os.path.splitext(file)[0]}@2x{os.path.splitext(file)[1]}")
                        img_48.save(new_file_path_48)

                    # Delete the original file
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

# Example usage:
input_directory = "images"
resize_and_rename(input_directory)
