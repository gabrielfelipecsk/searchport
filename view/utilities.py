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

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(Colorize('\rLoading ','yellow','black',0).representation + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(Colorize('\r Done!     ', 'green', 'black', 0).representation)

# t = threading.Thread(target=animate)
# t.start()
# #processo
# time.sleep(5)
# done = True

def print_banner(banner: str, color: str = 'white', background: str = 'black') -> None:
    clear()
    print(Colorize(banner, color, background))

print_banner(DOOR_SIMBOL, 'green', 'black')
