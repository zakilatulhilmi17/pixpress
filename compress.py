from PIL import Image
from pathlib import Path
import shutil

def batch_compress(input_dir, output_dir, quality=85):
    input_dir  = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    exts = {".jpg", ".jpeg", ".png", ".webp"}
    files = [f for f in input_dir.iterdir() if f.suffix.lower() in exts]

    if not files:
        print("No images found in the folder!")
        return

    print(f"Found {len(files)} image(s). Compressing...\n")

    for img_path in files:
        try:
            before = img_path.stat().st_size / 1024
            out = output_dir / img_path.name

            img = Image.open(img_path)
            if img.mode == "RGBA":
                img = img.convert("RGB")

            # Try saving at given quality
            img.save(out, optimize=True, quality=quality)
            after = out.stat().st_size / 1024

            # If output is bigger, just copy the original instead
            if after >= before:
                shutil.copy2(img_path, out)
                print(f"  {img_path.name}: already optimal, copied as-is ({before:.1f} KB)")
            else:
                saved = ((before - after) / before) * 100
                print(f"  {img_path.name}: {before:.1f} KB -> {after:.1f} KB  ({saved:.0f}% smaller)")

        except Exception as e:
            print(f"  Skipped {img_path.name}: {e}")

    print("\nDone! Check the 'compressed' folder.")

# ---- CHANGE THIS PATH to your images folder ----
batch_compress(
    input_dir  = r"C:\Users\YourNAME\Pictures\compress_input",
    output_dir = r"C:\Users\YourName\Pictures\compress_output",
    quality    = 10   # best compress i think, you can go to 40,70 or more
)
