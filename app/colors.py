# Source for named colors list and hex/rgb values:
# World Wide Web Consortium (W3C) CSS Color Module Level 4 - Named Colors
# https://www.w3.org/TR/css-color-4/#named-colors

import random
from typing import Dict, Any, Optional

# Dictionary of CSS3 named colors with hex, rgb, and name
COLOR_DATA: Dict[str, Dict[str, str]] = {
    "aliceblue": {"hex": "#F0F8FF", "rgb": "(240,248,255)", "name": "aliceblue"},
    "antiquewhite": {"hex": "#FAEBD7", "rgb": "(250,235,215)", "name": "antiquewhite"},
    "aqua": {"hex": "#00FFFF", "rgb": "(0,255,255)", "name": "aqua"},
    "aquamarine": {"hex": "#7FFFD4", "rgb": "(127,255,212)", "name": "aquamarine"},
    "azure": {"hex": "#F0FFFF", "rgb": "(240,255,255)", "name": "azure"},
    "beige": {"hex": "#F5F5DC", "rgb": "(245,245,220)", "name": "beige"},
    "bisque": {"hex": "#FFE4C4", "rgb": "(255,228,196)", "name": "bisque"},
    "black": {"hex": "#000000", "rgb": "(0,0,0)", "name": "black"},
    "blanchedalmond": {"hex": "#FFEBCD", "rgb": "(255,235,205)", "name": "blanchedalmond"},
    "blue": {"hex": "#0000FF", "rgb": "(0,0,255)", "name": "blue"},
    "blueviolet": {"hex": "#8A2BE2", "rgb": "(138,43,226)", "name": "blueviolet"},
    "brown": {"hex": "#A52A2A", "rgb": "(165,42,42)", "name": "brown"},
    "burlywood": {"hex": "#DEB887", "rgb": "(222,184,135)", "name": "burlywood"},
    "cadetblue": {"hex": "#5F9EA0", "rgb": "(95,158,160)", "name": "cadetblue"},
    "chartreuse": {"hex": "#7FFF00", "rgb": "(127,255,0)", "name": "chartreuse"},
    "chocolate": {"hex": "#D2691E", "rgb": "(210,105,30)", "name": "chocolate"},
    "coral": {"hex": "#FF7F50", "rgb": "(255,127,80)", "name": "coral"},
    "cornflowerblue": {"hex": "#6495ED", "rgb": "(100,149,237)", "name": "cornflowerblue"},
    "cornsilk": {"hex": "#FFF8DC", "rgb": "(255,248,220)", "name": "cornsilk"},
    "crimson": {"hex": "#DC143C", "rgb": "(220,20,60)", "name": "crimson"},
    "cyan": {"hex": "#00FFFF", "rgb": "(0,255,255)", "name": "cyan"},
    "darkblue": {"hex": "#00008B", "rgb": "(0,0,139)", "name": "darkblue"},
    "darkcyan": {"hex": "#008B8B", "rgb": "(0,139,139)", "name": "darkcyan"},
    "darkgoldenrod": {"hex": "#B8860B", "rgb": "(184,134,11)", "name": "darkgoldenrod"},
    "darkgray": {"hex": "#A9A9A9", "rgb": "(169,169,169)", "name": "darkgray"},
    "darkgreen": {"hex": "#006400", "rgb": "(0,100,0)", "name": "darkgreen"},
    "darkkhaki": {"hex": "#BDB76B", "rgb": "(189,183,107)", "name": "darkkhaki"},
    "darkmagenta": {"hex": "#8B008B", "rgb": "(139,0,139)", "name": "darkmagenta"},
    "darkolivegreen": {"hex": "#556B2F", "rgb": "(85,107,47)", "name": "darkolivegreen"},
    "darkorange": {"hex": "#FF8C00", "rgb": "(255,140,0)", "name": "darkorange"},
    "darkorchid": {"hex": "#9932CC", "rgb": "(153,50,204)", "name": "darkorchid"},
    "darkred": {"hex": "#8B0000", "rgb": "(139,0,0)", "name": "darkred"},
    "darksalmon": {"hex": "#E9967A", "rgb": "(233,150,122)", "name": "darksalmon"},
    "darkseagreen": {"hex": "#8FBC8F", "rgb": "(143,188,143)", "name": "darkseagreen"},
    "darkslateblue": {"hex": "#483D8B", "rgb": "(72,61,139)", "name": "darkslateblue"},
    "darkslategray": {"hex": "#2F4F4F", "rgb": "(47,79,79)", "name": "darkslategray"},
    "darkturquoise": {"hex": "#00CED1", "rgb": "(0,206,209)", "name": "darkturquoise"},
    "darkviolet": {"hex": "#9400D3", "rgb": "(148,0,211)", "name": "darkviolet"},
    "deeppink": {"hex": "#FF1493", "rgb": "(255,20,147)", "name": "deeppink"},
    "deepskyblue": {"hex": "#00BFFF", "rgb": "(0,191,255)", "name": "deepskyblue"},
    "dimgray": {"hex": "#696969", "rgb": "(105,105,105)", "name": "dimgray"},
    "dodgerblue": {"hex": "#1E90FF", "rgb": "(30,144,255)", "name": "dodgerblue"},
    "firebrick": {"hex": "#B22222", "rgb": "(178,34,34)", "name": "firebrick"},
    "floralwhite": {"hex": "#FFFAF0", "rgb": "(255,250,240)", "name": "floralwhite"},
    "forestgreen": {"hex": "#228B22", "rgb": "(34,139,34)", "name": "forestgreen"},
    "fuchsia": {"hex": "#FF00FF", "rgb": "(255,0,255)", "name": "fuchsia"},
    "gainsboro": {"hex": "#DCDCDC", "rgb": "(220,220,220)", "name": "gainsboro"},
    "ghostwhite": {"hex": "#F8F8FF", "rgb": "(248,248,255)", "name": "ghostwhite"},
    "gold": {"hex": "#FFD700", "rgb": "(255,215,0)", "name": "gold"},
    "goldenrod": {"hex": "#DAA520", "rgb": "(218,165,32)", "name": "goldenrod"},
    "gray": {"hex": "#808080", "rgb": "(128,128,128)", "name": "gray"},
    "green": {"hex": "#008000", "rgb": "(0,128,0)", "name": "green"},
    "yellowgreen": {"hex": "#9ACD32", "rgb": "(154,205,50)", "name": "yellowgreen"},
    "khaki": {"hex": "#F0E68C", "rgb": "(240,230,140)", "name": "khaki"},
    "lavender": {"hex": "#E6E6FA", "rgb": "(230,230,250)", "name": "lavender"},
    "lavenderblush": {"hex": "#FFF0F5", "rgb": "(255,240,245)", "name": "lavenderblush"},
    "lawngreen": {"hex": "#7CFC00", "rgb": "(124,252,0)", "name": "lawngreen"},
    "lemonchiffon": {"hex": "#FFFACD", "rgb": "(255,250,205)", "name": "lemonchiffon"},
    "lightblue": {"hex": "#ADD8E6", "rgb": "(173,216,230)", "name": "lightblue"},
    "lightcoral": {"hex": "#F08080", "rgb": "(240,128,128)", "name": "lightcoral"},
    "lightcyan": {"hex": "#E0FFFF", "rgb": "(224,255,255)", "name": "lightcyan"},
    "lightgoldenrodyellow": {"hex": "#FAFAD2", "rgb": "(250,250,210)", "name": "lightgoldenrodyellow"},
    "lightgray": {"hex": "#D3D3D3", "rgb": "(211,211,211)", "name": "lightgray"},
    "lightgreen": {"hex": "#90EE90", "rgb": "(144,238,144)", "name": "lightgreen"},
    "lightpink": {"hex": "#FFB6C1", "rgb": "(255,182,193)", "name": "lightpink"},
    "lightsalmon": {"hex": "#FFA07A", "rgb": "(255,160,122)", "name": "lightsalmon"},
    "lightseagreen": {"hex": "#20B2AA", "rgb": "(32,178,170)", "name": "lightseagreen"},
    "lightskyblue": {"hex": "#87CEFA", "rgb": "(135,206,250)", "name": "lightskyblue"},
    "lightslategray": {"hex": "#778899", "rgb": "(119,136,153)", "name": "lightslategray"},
    "lightsteelblue": {"hex": "#B0C4DE", "rgb": "(176,196,222)", "name": "lightsteelblue"},
    "lightyellow": {"hex": "#FFFFE0", "rgb": "(255,255,224)", "name": "lightyellow"},
    "lime": {"hex": "#00FF00", "rgb": "(0,255,0)", "name": "lime"},
    "limegreen": {"hex": "#32CD32", "rgb": "(50,205,50)", "name": "limegreen"},
    "linen": {"hex": "#FAF0E6", "rgb": "(250,240,230)", "name": "linen"},
    "magenta": {"hex": "#FF00FF", "rgb": "(255,0,255)", "name": "magenta"},
    "maroon": {"hex": "#800000", "rgb": "(128,0,0)", "name": "maroon"},
    "mediumaquamarine": {"hex": "#66CDAA", "rgb": "(102,205,170)", "name": "mediumaquamarine"},
    "mediumblue": {"hex": "#0000CD", "rgb": "(0,0,205)", "name": "mediumblue"},
    "mediumorchid": {"hex": "#BA55D3", "rgb": "(186,85,211)", "name": "mediumorchid"},
    "mediumpurple": {"hex": "#9370DB", "rgb": "(147,112,219)", "name": "mediumpurple"},
    "mediumseagreen": {"hex": "#3CB371", "rgb": "(60,179,113)", "name": "mediumseagreen"},
    "mediumslateblue": {"hex": "#7B68EE", "rgb": "(123,104,238)", "name": "mediumslateblue"},
    "mediumspringgreen": {"hex": "#00FA9A", "rgb": "(0,250,154)", "name": "mediumspringgreen"},
    "mediumturquoise": {"hex": "#48D1CC", "rgb": "(72,209,204)", "name": "mediumturquoise"},
    "mediumvioletred": {"hex": "#C71585", "rgb": "(199,21,133)", "name": "mediumvioletred"},
    "midnightblue": {"hex": "#191970", "rgb": "(25,25,112)", "name": "midnightblue"},
    "mintcream": {"hex": "#F5FFFA", "rgb": "(245,255,250)", "name": "mintcream"},
    "mistyrose": {"hex": "#FFE4E1", "rgb": "(255,228,225)", "name": "mistyrose"},
    "moccasin": {"hex": "#FFE4B5", "rgb": "(255,228,181)", "name": "moccasin"},
    "navajowhite": {"hex": "#FFDEAD", "rgb": "(255,222,173)", "name": "navajowhite"},
    "navy": {"hex": "#000080", "rgb": "(0,0,128)", "name": "navy"},
    "oldlace": {"hex": "#FDF5E6", "rgb": "(253,245,230)", "name": "oldlace"},
    "olive": {"hex": "#808000", "rgb": "(128,128,0)", "name": "olive"},
    "olivedrab": {"hex": "#6B8E23", "rgb": "(107,142,35)", "name": "olivedrab"},
    "orange": {"hex": "#FFA500", "rgb": "(255,165,0)", "name": "orange"},
    "orangered": {"hex": "#FF4500", "rgb": "(255,69,0)", "name": "orangered"},
    "orchid": {"hex": "#DA70D6", "rgb": "(218,112,214)", "name": "orchid"},
    "palegoldenrod": {"hex": "#EEE8AA", "rgb": "(238,232,170)", "name": "palegoldenrod"},
    "palegreen": {"hex": "#98FB98", "rgb": "(152,251,152)", "name": "palegreen"},
    "paleturquoise": {"hex": "#AFEEEE", "rgb": "(175,238,238)", "name": "paleturquoise"},
    "palevioletred": {"hex": "#DB7093", "rgb": "(219,112,147)", "name": "palevioletred"},
    "papayawhip": {"hex": "#FFEFD5", "rgb": "(255,239,213)", "name": "papayawhip"},
    "peachpuff": {"hex": "#FFDAB9", "rgb": "(255,218,185)", "name": "peachpuff"},
    "peru": {"hex": "#CD853F", "rgb": "(205,133,63)", "name": "peru"},
    "pink": {"hex": "#FFC0CB", "rgb": "(255,192,203)", "name": "pink"},
    "plum": {"hex": "#DDA0DD", "rgb": "(221,160,221)", "name": "plum"},
    "powderblue": {"hex": "#B0E0E6", "rgb": "(176,224,230)", "name": "powderblue"},
    "purple": {"hex": "#800080", "rgb": "(128,0,128)", "name": "purple"},
    "rebeccapurple": {"hex": "#663399", "rgb": "(102,51,153)", "name": "rebeccapurple"},
    "red": {"hex": "#FF0000", "rgb": "(255,0,0)", "name": "red"},
    "rosybrown": {"hex": "#BC8F8F", "rgb": "(188,143,143)", "name": "rosybrown"},
    "royalblue": {"hex": "#4169E1", "rgb": "(65,105,225)", "name": "royalblue"},
    "saddlebrown": {"hex": "#8B4513", "rgb": "(139,69,19)", "name": "saddlebrown"},
    "salmon": {"hex": "#FA8072", "rgb": "(250,128,114)", "name": "salmon"},
    "sandybrown": {"hex": "#F4A460", "rgb": "(244,164,96)", "name": "sandybrown"},
    "seagreen": {"hex": "#2E8B57", "rgb": "(46,139,87)", "name": "seagreen"},
    "seashell": {"hex": "#FFF5EE", "rgb": "(255,245,238)", "name": "seashell"},
    "sienna": {"hex": "#A0522D", "rgb": "(160,82,45)", "name": "sienna"},
    "silver": {"hex": "#C0C0C0", "rgb": "(192,192,192)", "name": "silver"},
    "skyblue": {"hex": "#87CEEB", "rgb": "(135,206,235)", "name": "skyblue"},
    "slateblue": {"hex": "#6A5ACD", "rgb": "(106,90,205)", "name": "slateblue"},
    "slategray": {"hex": "#708090", "rgb": "(112,128,144)", "name": "slategray"},
    "snow": {"hex": "#FFFAFA", "rgb": "(255,250,250)", "name": "snow"},
    "springgreen": {"hex": "#00FF7F", "rgb": "(0,255,127)", "name": "springgreen"},
    "steelblue": {"hex": "#4682B4", "rgb": "(70,130,180)", "name": "steelblue"},
    "tan": {"hex": "#D2B48C", "rgb": "(210,180,140)", "name": "tan"},
    "teal": {"hex": "#008080", "rgb": "(0,128,128)", "name": "teal"},
    "thistle": {"hex": "#D8BFD8", "rgb": "(216,191,216)", "name": "thistle"},
    "tomato": {"hex": "#FF6347", "rgb": "(255,99,71)", "name": "tomato"},
    "turquoise": {"hex": "#40E0D0", "rgb": "(64,224,208)", "name": "turquoise"},
    "violet": {"hex": "#EE82EE", "rgb": "(238,130,238)", "name": "violet"},
    "wheat": {"hex": "#F5DEB3", "rgb": "(245,222,179)", "name": "wheat"},
    "white": {"hex": "#FFFFFF", "rgb": "(255,255,255)", "name": "white"},
    "whitesmoke": {"hex": "#F5F5F5", "rgb": "(245,245,245)", "name": "whitesmoke"},
    "yellow": {"hex": "#FFFF00", "rgb": "(255,255,0)", "name": "yellow"},
}

# Reverse lookup by hex code (normalized uppercase)
HEX_DATA: Dict[str, Dict[str, str]] = {
    color_info["hex"].upper(): color_info
    for color_info in COLOR_DATA.values()
}


def get_random_color() -> Dict[str, Dict[str, str]]:
    """Returns a dictionary formatted as {color_name: {hex, rgb, name}} for a random color."""
    name = random.choice(list(COLOR_DATA.keys()))
    return {name: COLOR_DATA[name]}


def get_color_by_spec(color_spec: str) -> Optional[Dict[str, Dict[str, str]]]:
    """
    Finds a color by name or hex code.
    color_spec can be 'khaki', '#F0E68C', or 'F0E68C'.
    Returns {color_name: {hex, rgb, name}} or None if not found.
    """
    clean_spec = color_spec.strip().lower()
    if clean_spec in COLOR_DATA:
        return {clean_spec: COLOR_DATA[clean_spec]}

    hex_spec = clean_spec if clean_spec.startswith('#') else f'#{clean_spec}'
    hex_spec_upper = hex_spec.upper()

    if hex_spec_upper in HEX_DATA:
        color_info = HEX_DATA[hex_spec_upper]
        return {color_info["name"]: color_info}

    return None


def get_all_colors() -> Dict[str, Dict[str, str]]:
    """Returns the complete dictionary of colors."""
    return COLOR_DATA


def get_readable_font_color(color_info: Dict[str, str]) -> Dict[str, str]:
    """
    Given a color dict with 'rgb' key formatted as '(r,g,b)',
    calculates relative luminance and returns the COLOR_DATA entry for 'black' or 'white'
    that maximizes contrast for readability.
    """
    rgb_str = color_info.get("rgb", "(0,0,0)").strip("()")
    r, g, b = [int(c.strip()) for c in rgb_str.split(",")]

    def calc_lin(c: int) -> float:
        c_s = c / 255.0
        return c_s / 12.92 if c_s <= 0.04045 else ((c_s + 0.055) / 1.055) ** 2.4

    r_lin = calc_lin(r)
    g_lin = calc_lin(g)
    b_lin = calc_lin(b)

    luminance = 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

    contrast_white = (1.0 + 0.05) / (luminance + 0.05)
    contrast_black = (luminance + 0.05) / (0.0 + 0.05)

    if contrast_white > contrast_black:
        return COLOR_DATA["white"]
    else:
        return COLOR_DATA["black"]
