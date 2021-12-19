from .colors import Colorize
from .banners import banner

def inputc(text: str, foreground_color: str = 'default', background_color: str = 'default') -> str:
    return input(Colorize(text, foreground_color, background_color))


def input_banner(text: str, simbol: str = '-', size: int = 50, text_foreground_color: str = 'default', 
                 text_background_color: str = 'default', line_foreground_color: str = 'default', 
                 line_background_color: str = 'default') -> str:
    banner(text, simbol, size, text_foreground_color, text_background_color, line_foreground_color, line_background_color)
    return inputc('>>> ', text_foreground_color, text_background_color)
