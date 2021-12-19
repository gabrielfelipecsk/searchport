from colors import Colorize


def banner(text: str, simbol: str = '-', size: int = 50, text_foreground_color: str = 'default', text_background_color: str = 'default',
           line_foreground_color: str = 'default', line_background_color: str = 'default') -> None:
    print(Colorize(simbol, line_foreground_color, line_background_color) * size)
    print(Colorize(text, text_foreground_color, text_background_color, center=size))
    print(Colorize(simbol, line_foreground_color, line_background_color) * size)

banner('hello', text_foreground_color='blue')
