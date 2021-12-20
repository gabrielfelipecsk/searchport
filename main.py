import threading
import time
from view.banners import banner, option_banner
from view.inputs import input_banner, inputc
from controllers.db_manager import *
from controllers.connection import *
from view.utilities import clear, Loading



done_loading: bool = False


def add_new_host_ip() -> None:
    clear()
    banner('Tape the new host ip')
    choiced_host_ip: str = inputc('Host: ')
    response = create_new_data_host(choiced_host_ip)

    clear()
    Loading(20)
    
    if response == False:
        banner(f'Host: {choiced_host_ip} already exist', title_foreground_color='red', line_foreground_color='red')

    input('ENTER TO CONTINUE')


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
    clear()
    if user_choice == '0':
        add_new_host_ip()
    elif user_choice == '1':

        input('ENTER TO CONTINUE')
    elif user_choice == '2':

        input('ENTER TO CONTINUE')
    elif user_choice == '3':
        t = threading.Thread(target=Loading, args=[20]).start()
        
        input('ENTER TO CONTINUE')
    elif user_choice == '4':

        input('ENTER TO CONTINUE')
    elif user_choice == '5':
        exit_app()
        
    time.sleep(.5)