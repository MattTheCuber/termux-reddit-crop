from pathlib import Path

from PIL import Image

input_dir = Path("/storage/emulated/0/Pictures/Reddit")
output_dir = Path("/storage/emulated/0/Pictures/Reddit_Cropped")

input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

for path in input_dir.iterdir():
    if path.suffix in [".png", ".jpg", ".jpeg"]:
        try:
            with Image.open(path) as img:
                width, height = img.size
                cutoff = height
                for y in reversed(range(height)):
                    pixel = img.getpixel((0, y))
                    if pixel[0:3] != (36, 36, 36):
                        cutoff = y + 1
                        break
                cropped_img = img.crop((0, 0, width, cutoff))
                if cropped_img.mode == "RGBA":
                    cropped_img = cropped_img.convert("RGB")
                cropped_img.save(path.parent.parent / output_dir.name / path.name)
                print(
                    f"Cropped off {height - cutoff} pixels ({height} -> {cutoff}) from {path}"
                )
        except Exception as e:
            print(f"Error processing {path}: {e}")

print("Done!")
