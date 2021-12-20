import time
from view.banners import banner, option_banner
from view.inputs import input_banner, inputc
from controllers.db_manager import *
from controllers.connection import *
from view.utilities import clear


def add_new_host_ip() -> None:
    response = create_new_data_host()

def remove_host_ip() -> None:
    pass

def host_ip_list() -> None:
    pass

def init_port_scanner() -> None:
    pass

def settings() -> None:
    pass

def exit_app() -> None:
    clear()
    banner('Programa Encerrado!', title_foreground_color='red', line_foreground_color='red')
    input('ENTER TO CONTINUE')
    exit()
    

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
        add_new_host_ip()
    elif user_choice == '1':

        input('ENTER TO CONTINUE')
    elif user_choice == '2':

        input('ENTER TO CONTINUE')
    elif user_choice == '3':

        input('ENTER TO CONTINUE')
    elif user_choice == '4':

        input('ENTER TO CONTINUE')
    elif user_choice == '5':
        exit_app()
        
