from vect import Vect


# the name of the image that will be transformed into a mosaic
IMAGE_NAME = "example.jpg"

# the name of the folder that contains all the images that will compose the mosaic
TILE_SET = "persian"

# the dimensions of each tile of the mosaic
TILE_SIZE = Vect(35)

# the compression ratio of the original image dimensions
COMPRESSION_RATE = 2