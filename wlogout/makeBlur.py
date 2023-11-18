from PIL import Image, ImageFilter
import os
import subprocess

def capture_and_blur_screenshot(output_path):
    # Use grim to capture the screenshot and save it as a temporary file in the same directory
    temp_file = os.path.join(os.path.dirname(output_path), "screenshot_temp.png")
    subprocess.run(["grim", temp_file])

    # Open the temporary screenshot file
    screenshot = Image.open(temp_file)

    # Apply a blur effect
    blurred_screenshot = screenshot.filter(ImageFilter.GaussianBlur(8))
    blurred_screenshot.save(output_path)
    # Save


if __name__ == "__main__":
    # Specify the output path for the blurred screenshot
    output_path = "/home/wynvern/.config/wlogout/screenshot/blurred_screenshot.png"

    # Create the output directory if it doesn't exist
    output_directory = os.path.dirname(output_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    print("proceeding to take screenshot...")
    # Capture screenshot, apply blur, and save
    capture_and_blur_screenshot(output_path)
