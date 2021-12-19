import time
from view.banners import banner, option_banner
from view.inputs import input_banner, inputc
from controllers.db_manager import *
from controllers.connection import *
from view.utilities import clear


# Main Loop
while True:
    clear()
    option_banner(title='Scanner Host IP', title_background_color='green', line_background_color='green',options=[
        {'text': 'Add New Host IP'},
        {'text': 'Remove Host Ip'},
        {'text': 'Host IP List'},
        {'text': 'Initialize Port Scanner'},
        {'text': 'Settings', 'foreground_color': 'yellow'},
        {'text': 'Exit', 'foreground_color': 'red'},
    ])

    user_choice: str = inputc('>>> ', 'blue')
    
    if user_choice == '0':

        input('ENTER TO CONTINUE')
    elif user_choice == '1':
        
        input('ENTER TO CONTINUE')
