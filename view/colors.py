
class Colorize:
    def __init__(self, text: str, foreground_color: str = 'default', background_color: str = 'default', center: int = 0) -> None:
        self.foreground_color: str = foreground_color
        self.background_color: str = background_color
        self.center: int = center
        self.text: str = text.center(center)
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        self.representation: str = self._structure(self.foreground_color, self.background_color) + self.text + self.clear()
    
    def clear(self) -> str:
        return '\33[0m'

    def foreground(self, color_match: str) -> str:
        match color_match:
            case 'black':
                return '30'
            case 'red':
                return '31'
            case 'green':
                return '32'
            case 'yellow':
                return '33'
            case 'blue':
                return '34'
            case 'pink':
                return '35'
            case 'cyan':
                return '36'
            case 'white':
                return '37'

    def background(self, color_match: str) -> str:
        match color_match:
            case 'black':
                return '40'
            case 'red':
                return '41'
            case 'green':
                return '42'
            case 'yellow':
                return '43'
            case 'blue':
                return '44'
            case 'pink':
                return '45'
            case 'cyan':
                return '46'
            case 'white':
                return '47'
    
    def _structure(self, foreground_color: str = 'default', background_color: str = 'default') -> str:
        return '\33[' + (self.foreground(foreground_color) if foreground_color != 'default' else '') + (';' + self.background(background_color) if background_color != 'default' else '') + 'm' 

    def __repr__(self) -> str:
        return self.representation
    
    def __mul__(self, other: int) -> str:
        return self.representation * other
    
    def __str__(self) -> str:
        return self.representation

    def __add__(self, other: str) -> str:
        return self.representation + other
