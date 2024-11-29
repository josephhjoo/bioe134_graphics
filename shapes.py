from PIL import Image, ImageDraw, ImageFont

def rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill, outline, width, z=0):
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    draw.rectangle([(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], fill=fill, outline=outline, width=width)
    return [[(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], fill, width]


def ellipse(top_left_x, top_left_y, bottom_right_x, bottom_right_y, fill, outline, width, z=0):
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    draw.ellipse([(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], fill=fill, outline=outline, width=width)
    return [[(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], fill, width]


def line(top_x, top_y, bottom_x, bottom_y, fill, width):
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    draw.line([(top_x, top_y), (bottom_x, bottom_y)], fill=fill, width=width)
    return [[(top_x, top_y), (bottom_x, bottom_y)], fill, width]


def text(x, y, text, fill, font, z=0):
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, fill, font=font)
    return [[(x, y)], text, fill, font]


def triangle(vertex1, vertex2, vertex3, fill, outline):
    image = Image.new('RGB', (100, 100), 'white')
    draw = ImageDraw.Draw(image)
    draw.polygon([vertex1, vertex2, vertex3], fill=fill, outline=outline)
    return [[vertex1, vertex2, vertex3], fill, outline]

