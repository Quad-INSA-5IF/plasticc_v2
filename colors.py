from typing import List, Union

from PIL import Image

Number = Union[int, float]

teal = '#267278'
purple = '#65338d'
blue = '#4770b3'
pink = '#d21f75'
blue_dark = '#3b3689'
blue_light = '#50aed3'
green = '#48b24f'
orange = '#e57438'
green_dark = '#569d79'
grey_dark = '#58595b'
orange_light = '#e4b031'
lime = '#cad93f'
salmon = '#f5c8af'
green_light = '#9ac483'
grey_light = '#9e9ea2'

passband_colors = [
    '#7f629e', # u: purple
    '#99bb61', # g: green
    '#c0504f', # r: red
    '#f8954e', # i: orange
    '#b78373', # z: brown
    '#484753' # Y: grey
]

category_3 = [
    blue,
    lime,
    purple
]

category_6 = [
    blue,
    teal,
    orange,
    blue_light,
    lime,
    grey_light
]

category_12 = [
    teal,
    purple,
    blue,
    pink,
    blue_dark,
    blue_light,
    green,
    orange,
    green_dark,
    green_dark,
    orange_light,
    grey_light
]

category_15 = [
    teal,
    purple,
    blue,
    pink,
    blue_dark,
    blue_light,
    green,
    orange,
    green_dark,
    grey_dark,
    orange_light,
    lime,
    salmon,
    green_light,
    grey_light
]


def build_scale(color_name: str) -> List[str]:
    png_image = Image.open('color_scales/{}.png'.format(color_name))
    pixels = png_image.load()
    color_scale = []
    for i in range(0, png_image.size[0]):
        pixel = pixels[i, 0]
        if type(pixel) is int:
            r = pixel
            g = pixel
            b = pixel
        else:
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
        color_scale.append("#{0:02x}{1:02x}{2:02x}".format(r, g , b))
    return color_scale


blue_scale = build_scale('Blues')
cool_scale = build_scale('Cool')
cubehelix_scale = build_scale('Cubehelix')
green_scale = build_scale('Greens')
grey_scale = build_scale('Greys')
inferno_scale = build_scale('Inferno')
magma_scale = build_scale('Magma')
orange_scale = build_scale('Oranges')
plasma_scale = build_scale('Plasma')
purple_scale = build_scale('Purples')
rainbow_scale = build_scale('Rainbow')
red_scale = build_scale('Reds')
sinebow_scale = build_scale('Sinebow')
spectral_scale = build_scale('Spectral')
viridis_scale = build_scale('Viridis')
warm_scale = build_scale('Warm')


def rescale(scale: List[str], values: List[Number], reverse: bool = False) -> List[str]:
    _min = min(values)
    _max = max(values)
    c = []
    last_idx = len(scale) - 1
    for x in values:
        idx = int( ((x - _min) / (_max - _min)) * last_idx )
        if reverse:
            idx = last_idx - idx
        c.append(scale[idx])
    return c
