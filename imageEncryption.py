from PIL import Image
import random

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            random_x = random.randint(0, width - 1)
            random_y = random.randint(0, height - 1)
            pixels[i, j], pixels[random_x, random_y] = pixels[random_x, random_y], pixels[i, j]

    return image

def add_value_to_pixels(image, value):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (min(255, r + value), min(255, g + value), min(255, b + value))

    return image

def main():
    # Load an image
    image_path = "./samples/sample2.jpg"
    image = Image.open(image_path)
    
    operation = input("Choose an operation (swap/add): ").strip().lower()

    if operation == "swap":
        encrypted_image = swap_pixels(image)
    elif operation == "add":
        value = int(input("Enter the value to add to each pixel (0-255): "))
        encrypted_image = add_value_to_pixels(image, value)
    else:
        print("Invalid operation.")
        return

    # Save the encrypted image
    encrypted_image.save(r"outputs/encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

if __name__ == "__main__":
    main()
