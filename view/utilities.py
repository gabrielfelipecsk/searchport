import os, sys, time, itertools, threading
from .banners import *
from .colors import Colorize

DOOR_SIMBOL: str = """
@@####################################@@@@@@@@@@@@
@@###@@@@@@@@@@@###########@@@@@@@@###@@@@@@@@@@@@
@@###@@@@#######@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@#####@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@########@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@#####################&@
@@###@@@@##@@@#@@@@@@@@@@#######################&@
@@###@@@@##@@###@@@@@@@#########################&@
@@###@@@@##@@@#@@@@@@@@@@#######################&@
@@###@@@@##@@@@@@@@@@@@@@@@#####################&@
@@###@@@@##@@@@@@@@@@@@@@@@@@@########@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@#####@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@@@&#@@@@@@@@@@@@@
@@###@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@###@@@@########@@@@@@@@@@@@@@@@@@##@@@@@@@@@@@@@
@@###@@@@@@@@@@@&##########@@@@@@@@###@@@@@@@@@@@@
@@####################################@@@@@@@@@@@@
""".replace('@', ' ').replace('#', '■').replace('&', '■')

def clear() -> None:
    match sys.platform:
        case 'win32':
            os.system('cls')
        case 'linux':
            os.system('clear')
        case 'darwin':
            os.system('clear')

class Loading:
    def __init__(self, limit: int = 10) -> None:
        counter = 0
        for bar in self.loading():

            if counter == limit:
                break
            
            counter += 1
        clear()
        sys.stdout.write(Colorize('Done!', 'green', 'black', 0).representation)
        print()
        
        

    def loading(self) -> None:
        for c in itertools.cycle(['|', '/', '-', '\\']):
            sys.stdout.write(Colorize('\rLoading ','yellow','black',0).representation + c)
            yield sys.stdout.flush()
            time.sleep(0.1)

        


def print_banner(banner: str, color: str = 'white', background: str = 'black') -> None:
    clear()
    return Colorize(banner, color, background)

