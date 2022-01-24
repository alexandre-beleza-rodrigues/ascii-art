import sys
import json
from PIL import Image

SIZE = (150, 75)  # (side, hight = side/2)


with open('character_brightness.json', 'r') as file:
    character_brightness_dict = json.load(file)


def normalize_image_pixel_values(image_pixels: list) -> list:
    b_max = max(image_pixels)
    b_min = min(image_pixels)

    norm_image_pixels = []
    for pixel in image_pixels:
        norm_pixel_value = round(((pixel - b_min) / (b_max - b_min)), 5)

        norm_image_pixels.append(norm_pixel_value)

    return norm_image_pixels


def get_best_character_for_pixel(pixel_value: int) -> str:
    best_character = ('', float('inf'))
    for character in character_brightness_dict:
        diff = abs(pixel_value - character_brightness_dict[character])

        if diff < best_character[1]:
            best_character = (character, diff)

    return best_character[0]


def convert_img_to_ascii(image: Image) -> str:
    image = image.convert('L')
    image = image.resize(SIZE)
    image_pixels = normalize_image_pixel_values(list(image.getdata()))
    
    ascii_image = ''
    pixel_num = 1
    for pixel in image_pixels:
        character = get_best_character_for_pixel(pixel)

        ascii_image += character

        if pixel_num % SIZE[0] == 0:
            ascii_image += '\n'

        pixel_num += 1

    return ascii_image


def main():
    image_file_directory = sys.argv[1]
    image = Image.open(image_file_directory)

    new_image = convert_img_to_ascii(image)

    print(new_image)


if __name__ == '__main__':
    main()
