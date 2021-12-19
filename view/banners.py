from .colors import Colorize


def line(simbol: str = '-', size: int = 50, foreground_color: str = 'default', 
         background_color: str = 'default') -> None:
    print(Colorize(simbol, foreground_color, background_color) * size)


def banner(text: str, simbol: str = '-', size: int = 50, text_foreground_color: str = 'default', text_background_color: str = 'default',
           line_foreground_color: str = 'default', line_background_color: str = 'default') -> None:
    line(simbol, size, line_foreground_color, line_background_color)
    print(Colorize(text, text_foreground_color, text_background_color, center=size))
    line(simbol, size, line_foreground_color, line_background_color)
