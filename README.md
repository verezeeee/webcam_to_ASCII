# Webcam to ASCII Art

This project captures images from your webcam and converts them into ASCII art, which is displayed in the terminal. You can choose between colored and grayscale ASCII art.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pillow

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/verezeeee/webcam_to_ASCII.git
    ```

2. Navigate to the project directory:
    ```
    cd webcam_to_ASCII
    ```

3. Install the required packages:
    ```
    pip install opencv-python numpy pillow
    ```

## Usage

1. Run the script:
    ```
    python main.py
    ```

2. Press 'q' to quit the application.
3. Press 'c' to toggle between colored and grayscale ASCII art.

## How It Works

- The script captures frames from your webcam using OpenCV.
- Each frame is converted to an ASCII representation.
- The ASCII art is displayed in the terminal.
- The script continuously updates the ASCII art based on the live webcam feed.

## Functions

- `clear_screen()`: Clears the terminal screen based on the operating system.
- `get_terminal_size()`: Gets the current terminal size.
- `rgb_to_ansi(r, g, b)`: Converts RGB values to ANSI color codes.
- `image_to_ascii(image, width=None, height=None, colored=True)`: Converts an image to ASCII art.
- `main()`: Initializes the webcam, captures frames, converts them to ASCII art, and displays them in the terminal.

## License

This project is licensed under the MIT License.
