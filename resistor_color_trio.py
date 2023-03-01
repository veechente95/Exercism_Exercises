color_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}


def label(colors):
    color1 = color_dict[colors[0]]
    color2 = color_dict[colors[1]]
    color3 = color_dict[colors[2]] * '0'
    value = int(f'{color1}{color2}{color3}')

    if value // 1000 == 0:
        final_value = f'{value} ohms'

    elif value // 1000 ** 1 < 1000:
        final_value = f'{value // 1000 ** 1} kiloohms'

    elif value // 1000 ** 2 < 1000:
        final_value = f'{value // 1000 ** 2} megaohms'

    elif value // 1000 ** 3 < 1000:
        final_value = f'{value // 1000 ** 3} gigaohms'
    
    return final_value
