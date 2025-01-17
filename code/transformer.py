from PIL import Image, ImageOps
import random

class SquarePad:
    def __call__(self, image):
        # Voeg padding toe om de afbeelding vierkant te maken
        max_size = max(image.size)
        pad_x = (max_size - image.size[0]) // 2
        pad_y = (max_size - image.size[1]) // 2
        padding = (pad_x, pad_y, max_size - image.size[0] - pad_x, max_size - image.size[1] - pad_y)
        return ImageOps.expand(image, padding, fill=0)  # Vul de padding met zwarte rand

class ResizeWithRandomRotation:
    def __init__(self, size, max_rotate_angle):
        self.size = size
        self.max_rotate_angle = max_rotate_angle

    def __call__(self, image):
        # Genereer een willekeurige rotatiehoek tussen 0 en max_rotate_angle
        random_angle = random.uniform(0, self.max_rotate_angle)

        # Roteer de afbeelding met de willekeurige hoek
        rotated_image = image.rotate(random_angle, expand=True, fillcolor=(0, 0, 0))

        # Voeg vierkante padding toe
        padded_image = SquarePad()(rotated_image)

        # Verander van grootte zonder te croppen
        return padded_image.resize((self.size, self.size), resample=Image.Resampling.LANCZOS)
