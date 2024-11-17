# 🖼️ Image Encryption Tool

This project is a **simple image encryption tool** that manipulates pixels in an image to encrypt it. The tool supports two operations:
- **Swapping Pixel Values**: Randomly swaps pixel positions.
- **Adding a Value to Pixels**: Applies a mathematical operation to each pixel by increasing its RGB values.

## ✨ Features

- **Swap Pixels**: Randomly exchanges pixel positions to obfuscate the image.
- **Add Value to Pixels**: Adds a user-specified value to each pixel's RGB components while maintaining valid pixel ranges (0-255).

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- `Pillow` library (`pip install pillow`)

### 🔧 How to Use
1. Place your image file in the samples folder.
2. Run the script:
```bash
python encrypt_image.py
```
3. Choose an operation:
- swap: Randomly swaps pixel values.
- add: Adds a specified value to the RGB components of each pixel.
4. When prompted, enter a value between 0-255 for the add operation.
5. The encrypted image will be saved in the outputs folder as encrypted_image.png.
## 📂 Project Structure
- `encrypt_image.py:` Main script for encryption.
- `samples/:` Folder containing input images.
- `outputs/:` Folder where encrypted images are saved.
  
## 📸 Example Usage
### Original Image
![sample2](https://github.com/user-attachments/assets/34c2659a-824c-4be7-b2ca-dffbc49ae448)

### Encrypted Image 
![encrypted_image](https://github.com/user-attachments/assets/b5874a25-9288-4c05-84a1-c06f04cab979)


