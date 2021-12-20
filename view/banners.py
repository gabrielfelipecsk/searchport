from .colors import Colorize


def line(simbol: str = '-', size: int = 50, foreground_color: str = 'default', 
         background_color: str = 'default') -> None:
    print(Colorize(simbol, foreground_color, background_color) * size)


def banner(title: str, simbol: str = '-', size: int = 50, title_foreground_color: str = 'default', title_background_color: str = 'default',
           line_foreground_color: str = 'default', line_background_color: str = 'default') -> None:
    line(simbol, size, line_foreground_color, line_background_color)
    print(Colorize(title, title_foreground_color, title_background_color, center=size))
    line(simbol, size, line_foreground_color, line_background_color)

def option_banner(title: str, simbol: str = '-', size: int = 50, title_foreground_color: str = 'default', title_background_color: str = 'default',
           line_foreground_color: str = 'default', line_background_color: str = 'default', options: list = []) -> None:
    banner(title, simbol, size, title_foreground_color, title_background_color, line_foreground_color, line_background_color)

    for option in enumerate(options):
        print(Colorize(str(option[0]) + ' -'), Colorize(**option[1]))
    
    line(simbol=simbol, foreground_color=line_foreground_color, background_color=line_background_color)
