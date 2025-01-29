from PIL import Image
import os

def compress_image(input_path, output_path, target_size=1500):
    # Open the image
    img = Image.open(input_path).convert("RGBA")  # Ensure transparency is maintained
    
    # Try saving in WebP format with lossless compression
    img.save(output_path, "WEBP", lossless=True)

    # Check file size
    file_size = os.path.getsize(output_path)
    print(f"Initial WebP size: {file_size} bytes")

    # If still too large, try reducing quality
    if file_size > target_size:
        quality = 100
        while file_size > target_size and quality > 0:
            img.save(output_path, "WEBP", lossless=True, quality=quality)
            file_size = os.path.getsize(output_path)
            print(f"Trying quality {quality}: {file_size} bytes")
            quality -= 5  # Reduce quality gradually

    # Final size check
    file_size = os.path.getsize(output_path)
    if file_size <= target_size:
        print(f"Compression successful: {file_size} bytes")
    else:
        print(f"Could not reach the target size, final size: {file_size} bytes")

# Example usage
compress_image("shapes.png", "new_shapes.webp")
