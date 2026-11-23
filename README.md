# Mosaic-Image

A Python script that rebuilds a picture as a mosaic of small images.

Pick an image, point the script at a folder of tile images, and it replaces each region of the picture with the tile whose average color is the closest. It is meant for anyone who wants a photo mosaic from their own image collection.

## Table of contents

- [Mosaic-Image](#mosaic-image)
	- [Table of contents](#table-of-contents)
	- [How it works](#how-it-works)
	- [Tech stack](#tech-stack)
	- [Repository structure](#repository-structure)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Configuration](#configuration)
	- [Running locally](#running-locally)
	- [Useful scripts](#useful-scripts)
	- [License](#license)

## How it works

1. **Tile loading**: every file of the chosen folder in `tile_set/` is opened, resized to `TILE_SIZE` and reduced to its average RGB color. Files that cannot be read as images are skipped.
2. **Downscaling**: the input image is shrunk by `COMPRESSION_RATE`, so that one pixel of the shrunk image maps to one tile.
3. **Matching**: for each pixel, a k-d tree over the tile colors returns the tile with the nearest average color.
4. **Assembly**: the matching tiles are pasted side by side on a new image of `input size × TILE_SIZE / COMPRESSION_RATE`.
5. **Output**: the result is saved in `output/` under the same file name as the input.

Progress is printed in the terminal with a loading bar for steps 1 and 3-4.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Language | Python 3 |
| Image handling | Pillow |
| Color matching | SciPy (`scipy.spatial.KDTree`), NumPy |

## Repository structure

```
.
├── input/        Source images
├── output/       Generated mosaics
├── tile_set/     Folders of tile images (one folder per set)
├── config.py     Settings
├── main.py       Tile loading, matching and image generation
└── vect.py       2D vector class used for sizes and positions
```

The repository ships one tile set, `tile_set/persian`, and one example image, `example.jpg`, present in both `input/` and `output/`. Paths are relative, so the script must be run from the repository root.

## Prerequisites

- [Python](https://www.python.org/) 3 (no specific version is declared by the project)
- [Pillow](https://pypi.org/project/Pillow/), [SciPy](https://pypi.org/project/scipy/) and [NumPy](https://pypi.org/project/numpy/)

## Installation

```bash
git clone git@github.com:maxencebonamy/Mosaic-Image.git
cd Mosaic-Image
```

```bash
pip install pillow scipy numpy
```

## Configuration

Settings are constants in `config.py`.

| Variable | Description | Example |
| --- | --- | --- |
| `IMAGE_NAME` | File name, inside `input/`, of the image to convert | `"example.jpg"` |
| `TILE_SET` | Folder name, inside `tile_set/`, holding the tile images | `"persian"` |
| `TILE_SIZE` | Dimensions in pixels of each tile, as a `Vect` | `Vect(35)` |
| `COMPRESSION_RATE` | Divisor applied to the input dimensions; a higher value gives fewer tiles and a smaller output | `2` |

The output width and height are the input dimensions multiplied by `TILE_SIZE` and divided by `COMPRESSION_RATE`.

## Running locally

Put the image in `input/`, set `IMAGE_NAME` in `config.py`, then run:

```bash
python main.py
```

The mosaic is written to `output/<IMAGE_NAME>`.

To use your own tiles, create a folder in `tile_set/`, fill it with images and set `TILE_SET` to its name.

## Useful scripts

| Command | Effect |
| --- | --- |
| `python main.py` | Generate the mosaic for `IMAGE_NAME` using the `TILE_SET` folder |

## License

This project is licensed under the [MIT License](LICENSE).
