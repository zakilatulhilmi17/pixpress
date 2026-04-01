![pixpress logo](logo.png)

# Image Batch Compressor

A simple Python script to batch compress images in a folder using Pillow. Supports JPG, PNG, and WebP. Automatically skips files that would become larger after compression.

## Requirements

- Python 3.x
- Pillow library

## Installation

First, Install Pillow via pip:

```bash
pip install Pillow
```

## Usage

1. Open `compress.py` in any text editor
2. Change the `input_dir` and `output_dir` paths at the bottom of the file:

```python
batch_compress(
    input_dir  = r"C:\Users\YourName\Pictures\compress_input",
    output_dir = r"C:\Users\YourName\Pictures\compress_output",
    quality    = 80
)
```
3. Add your images to the `input_dir` folder.
4. Run the script on cmd or terminal:

```bash
python compress.py
```

## Configuration

| Parameter | Description | Default |
|---|---|---|
| `input_dir` | Folder containing your original images | — |
| `output_dir` | Folder where compressed images will be saved | — |
| `quality` | Compression quality, 1 (smallest) to 95 (best) | `10` |

### Quality guide

| Value | Result |
|---|---|
| `90` | High quality, slightly smaller file |
| `80` | Good balance between quality and size |
| `65–75` | Noticeable compression, much smaller |
| `10–50` | Aggressive compression, visible quality loss |

## Supported formats

- `.jpg` / `.jpeg`
- `.png`
- `.webp`

## How it works

- Scans the `input_dir` folder for supported image files
- Compresses each image at the given quality level
- Compares the compressed size to the original — if the compressed version is **bigger**, it copies the original as-is instead
- Saves all output to `output_dir` without modifying the originals

## Example output

```
Found 4 image(s). Compressing...

  photo1.jpg: 678.0 KB -> 410.3 KB  (40% smaller)
  photo2.jpg: 744.0 KB -> 512.1 KB  (31% smaller)
  logo.png: already optimal, copied as-is (467.5 KB)
  banner.webp: 545.6 KB -> 398.2 KB  (27% smaller)

Done! Check the 'compressed' folder.
```

## Notes

- Original files are **never modified**
- The output folder is created automatically if it doesn't exist
- RGBA images (transparent PNGs) are automatically converted to RGB when needed
- Works on Windows, Linux, and macOS
