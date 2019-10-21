
def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""

    if (rgb[0] >= 0 and rgb[0] <= 255) and (rgb[1] >= 0 and rgb[1] <= 255) and (rgb[2] >= 0 and rgb[2] <= 255):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2]).upper()
    else:
        raise ValueError


#print(rgb_to_hex((10, 0, 0)))