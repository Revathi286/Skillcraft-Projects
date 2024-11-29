from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image from the specified path."""
    return Image.open(image_path).convert('RGB')  # Convert to RGB mode

def save_image(image, output_path):
    """Save the image to the specified output path."""
    image.save(output_path)

def swap_pixels(image):
    """Swap the pixel values of the image."""
    pixels = np.array(image)
    # Swapping pixels (for simplicity, we swap the first pixel with the last)
    pixels[0], pixels[-1] = pixels[-1], pixels[0]
    return Image.fromarray(pixels)

def apply_math_operation(image, operation):
    """Apply a mathematical operation to each pixel."""
    pixels = np.array(image)
    if operation == 'add':
        # Add 50 to each pixel value (clamped to 255)
        pixels = np.clip(pixels + 50, 0, 255)
    elif operation == 'subtract':
        # Subtract 50 from each pixel value (clamped to 0)
        pixels = np.clip(pixels - 50, 0, 255)
    elif operation == 'multiply':
        # Multiply each pixel value by 1.2 (clamped to 255)
        pixels = np.clip(pixels * 1.2, 0, 255)
    elif operation == 'divide':
        # Divide each pixel value by 1.2 (clamped to 255)
        pixels = np.clip(pixels / 1.2, 0, 255)
    return Image.fromarray(pixels.astype(np.uint8))

def encrypt_image(input_path, output_path, operation):
    """Encrypt the image using the specified operation."""
    image = load_image(input_path)
    
    # Swap pixels
    image = swap_pixels(image)
    
    # Apply mathematical operation
    image = apply_math_operation(image, operation)
    
    # Save the encrypted image
    save_image(image, output_path)

if __name__ == "__main__":
    input_image_path = 'bgs.jpg'  # Specify your input image path
    output_image_path = 'encrypted_image13.png'  # Specify your output image path

    # Ask user for the operation they want to perform
    print("Choose a mathematical operation to apply to the image:")
    print("1. Add 50 to each pixel")
    print("2. Subtract 50 from each pixel")
    print("3. Multiply each pixel by 1.2")
    print("4. Divide each pixel by 1.2")
    
    operation_choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    # Map user choice to operation
    if operation_choice == '1':
        operation = 'add'
    elif operation_choice == '2':
        operation = 'subtract'
    elif operation_choice == '3':
        operation = 'multiply'
    elif operation_choice == '4':
        operation = 'divide'
    else:
        print("Invalid choice. Defaulting to 'add'.")
        operation = 'add'
    
    encrypt_image(input_image_path, output_image_path, operation)
    print(f"Image encrypted and saved to {output_image_path}")