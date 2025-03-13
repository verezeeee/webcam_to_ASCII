#generate a script that will turn my webcam image into ASCII art

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import os
import shutil  # For getting terminal size

def clear_screen():
    """Clear the terminal screen based on OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    """Get the current terminal size"""
    terminal_size = shutil.get_terminal_size()
    # Subtract 1 from height to prevent scrolling
    return terminal_size.columns, terminal_size.lines - 1

def rgb_to_ansi(r, g, b):
    """Convert RGB values to ANSI color code"""
    return f"\033[38;2;{r};{g};{b}m"

def image_to_ascii(image, width=None, height=None, colored=True):
    """Convert an image to ASCII art"""
    # Get terminal size if width or height not provided
    if width is None or height is None:
        term_width, term_height = get_terminal_size()
        width = width or term_width
        height = height or term_height
    
    # Convert to PIL Image
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # Calculate dimensions to maintain aspect ratio and fit terminal
    img_aspect_ratio = pil_img.height / pil_img.width
    term_aspect_ratio = height / width
    
    if img_aspect_ratio > term_aspect_ratio:
        # Image is taller than terminal proportion
        new_height = height
        new_width = int(new_height / img_aspect_ratio / 0.55)  # Adjust for character aspect ratio
    else:
        # Image is wider than terminal proportion
        new_width = width
        new_height = int(new_width * img_aspect_ratio * 0.55)  # Adjust for character aspect ratio
    
    # Ensure we don't exceed terminal dimensions
    new_width = min(new_width, width)
    new_height = min(new_height, height)
    
    # Resize image
    pil_img = pil_img.resize((new_width, new_height))
    
    # ASCII characters from dark to light
    ascii_chars = "@%#*+=-:. "
    
    # Get pixel data
    pixels = np.array(pil_img)
    
    # Create grayscale version for ASCII mapping
    gray_img = pil_img.convert("L")
    gray_pixels = np.array(gray_img)
    
    # Generate ASCII art with colors
    if colored:
        lines = []
        for y in range(len(gray_pixels)):
            line = ""
            for x in range(len(gray_pixels[y])):
                # Get grayscale value for ASCII character selection
                gray_val = gray_pixels[y][x]
                # Get RGB values for color
                r, g, b = pixels[y][x]
                # Add colored ASCII character
                char_idx = min(gray_val // 25, len(ascii_chars) - 1)
                line += rgb_to_ansi(r, g, b) + ascii_chars[char_idx]
            lines.append(line)
        # Add reset code at the end
        ascii_str = "\n".join(lines) + "\033[0m"
    else:
        # Fallback to grayscale if color not requested
        ascii_str = "\n".join("".join(ascii_chars[min(pixel // 25, len(ascii_chars) - 1)] for pixel in row) for row in gray_pixels)
    
    return ascii_str

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Press 'q' to quit, 'c' to toggle color...")
    time.sleep(2)  # Give user time to read the message
    
    # Color mode flag
    colored = True
    
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Failed to capture image")
                break
            
            # Mirror the frame horizontally
            frame = cv2.flip(frame, 1)
            
            # Get current terminal size
            term_width, term_height = get_terminal_size()
            
            # Convert to ASCII with current terminal dimensions
            ascii_art = image_to_ascii(frame, term_width, term_height, colored)
            
            # Clear screen and display ASCII art
            clear_screen()
            print(ascii_art)
            
            # Check for key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                # Toggle color mode
                colored = not colored
                
    finally:
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
