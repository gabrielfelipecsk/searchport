import time

from view.inputs import input_banner
from controllers.db_manager import *


# Main Loop
while True:
    user_choice: str = input_banner(text='O que deseja fazer?', text_foreground_color='green')