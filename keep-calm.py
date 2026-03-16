# This script is available on GitHub Gist at https://gist.github.com/FJrodafo/63a81f9e1dcb7a64579f4ad01bb8aec9
# Explore more gists by Francisco José Rodríguez Afonso at https://gist.github.com/FJrodafo

# A simple Python script that generates customisable "Keep Calm and Carry On" style images with configurable text, colours, and dimensions!
# The output is a PNG image with a solid background colour, the crown at the top, and five lines of customisable text centered below it.

import argparse
from os import path
from PIL import Image, ImageFont, ImageDraw

with open("./assets/colors/colors.txt", "r") as f:
    colors = [line.strip() for line in f]

VERSION = "1.0.0"
HELP_TEXT = """This script has five arguments, all of them are optional, here is a description of each of them:
- [--width], [-w]: Specifies the width of the image in pixels. It accepts an integer value. If not provided, it defaults to 200 pixels.
- [--text], [-t]: Specifies the text content to be displayed on the image. It accepts up to 5 strings as arguments. If not provided, it defaults to ["keep", "calm", "and", "carry", "on"].
- [--bg-colour]: Specifies the background color of the image. It accepts a string representing a color name chosen from a predefined list of colors. If not provided, it defaults to "red".
- [--text-colour]: Specifies the color of the text displayed on the image. It accepts a string representing a color name chosen from a predefined list of colors. If not provided, it defaults to "white".
- [--output], [-o]: Specifies the output file path and name for the generated image. It accepts a string representing the file path. If not provided, it defaults to "./output/carry_on.png"."""


def parse_arguments():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"{VERSION}",
    )
    parser.add_argument(
        "--help",
        "-h",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=200,
        help="image width",
    )
    parser.add_argument(
        "--text",
        "-t",
        type=str,
        nargs=5,
        default=["keep", "calm", "and", "carry", "on"],
        help="keep calm message",
    )
    parser.add_argument(
        "--bg-colour",
        type=str,
        default="red",
        choices=colors,
        help="background colour",
    )
    parser.add_argument(
        "--text-colour",
        type=str,
        default="white",
        choices=colors,
        help="background colour",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="./output/carry_on.png",
        help="output image file path",
    )
    args = parser.parse_args()
    if args.help:
        print(HELP_TEXT)
        parser.exit()

    return args


def create_image(args):
    MARGIN = 20
    HEIGHT = 300
    WIDTH = args.width
    LINES = args.text
    BACKGROUND = args.bg_colour
    TEXT = args.text_colour
    FONTSIZE = 30
    DIRNAME = path.dirname(__file__)
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BACKGROUND)
    draw = ImageDraw.Draw(img)
    fontsize = FONTSIZE
    lines = list(map(str.upper, LINES))

    def getFont(line, size, index=0):
        font_path = path.join(DIRNAME, "./assets/font/KeepCalm-Medium.ttf")
        font = ImageFont.truetype(
            font_path, size if index != 2 else int(2 * round(size / 4))
        )
        bbox = font.getbbox(line)
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        return (width, height, font)

    maxlength = 0
    while True:
        for n, line in enumerate(lines):
            width, height, font = getFont(line, fontsize, n)
            maxlength = max(width, maxlength)
        if maxlength < WIDTH - (2 * MARGIN):
            break
        else:
            maxlength = 0
            fontsize = fontsize - 1
    y = (
        HEIGHT
        - (MARGIN if fontsize == FONTSIZE else ((WIDTH - maxlength) / 2))
        + fontsize / 2
    )
    for n, line in enumerate(reversed(lines)):
        width, height, font = getFont(line, fontsize, n)
        x = (WIDTH / 2) - (width / 2)
        y = y - height - (fontsize / 2)
        draw.text((x, y), line, TEXT, font)
    crown = "^"
    width, height, font = getFont(crown, 77)
    x = (WIDTH / 2) - (width / 2)
    y = (y / 2) - (height / 2) - 5
    draw.text((x, y), crown, TEXT, font)
    img.save(args.output)


if __name__ == "__main__":
    args = parse_arguments()
    create_image(args)
