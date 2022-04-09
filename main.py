import threading
import time
from view.banners import banner, option_banner
from view.inputs import input_banner, inputc
from controllers.db_manager import *
from controllers.connection import *
from view.utilities import clear, Loading



def add_new_host_ip() -> None:
    clear()
    banner('Tape the new host ip', title_foreground_color='green', line_foreground_color='green')
    print('List of hosts:')
    host_ip_list()
    print('\n')
    choiced_host_ip: str = inputc('Host: ')
    if choiced_host_ip == '':
        return False
    response = create_host(choiced_host_ip)

    clear()
    Loading(20)
    
    if response == False:
        banner(f'Host: {choiced_host_ip} already exist', title_foreground_color='red', line_foreground_color='red')

    input('ENTER TO CONTINUE')


def remove_host_ip() -> None:
    clear()
    banner('Choice the host that you want to remove.', title_foreground_color='red', line_foreground_color='red')
    host_ip_list()
    print('\n')
    choiced_host_ip: str = inputc('Host: ')
    if choiced_host_ip == 'all':
        clear()
        Loading(20)
        remove_host('all')
        input('ENTER TO CONTINUE')
    
    if choiced_host_ip == '':
        return False
    else: 
        clear()
        confirmation: str = inputc('Are you sure about that? (y/n) \n>>>', 'red')

        clear()
        Loading(20)

        if confirmation in ('y', 'Y', 'yes'):
            return remove_host(choiced_host_ip)
        
        input('ENTER TO CONTINUE')
        return False

def host_ip_list() -> None:
    host_ip_list: list = os.listdir(os.path.abspath('database'))
    host_ip_list.sort()

    for host_ip in host_ip_list:
        print(host_ip)



def init_port_scanner() -> None:
    pass

def settings() -> None:
    pass


def exit_app() -> None:
    clear()
    banner('Program Exit!', title_foreground_color='red', line_foreground_color='red')
    input('ENTER TO CONTINUE')
    exit()
    

# Main Loop
while True:
    clear()

    option_banner(title='Scanner Host IP', title_background_color='green', line_background_color='green',options=[
        {'text': 'Add New Host IP', 'foreground_color': 'green'},
        {'text': 'Remove Host Ip', 'foreground_color': 'red'},
        {'text': 'Host IP List', 'foreground_color': 'blue'},
        {'text': 'Initialize Port Scanner', 'foreground_color': 'white'},
        {'text': 'Settings', 'foreground_color': 'yellow'},
        {'text': 'Exit', 'foreground_color': 'red'},
    ])

    user_choice: str = inputc('>>> ', 'blue')
    clear()
    if user_choice == '0':
        add_new_host_ip()
    elif user_choice == '1':
        remove_response = remove_host_ip()
        if remove_response == False:
            clear()
            banner('Error: The host not exist', title_foreground_color='red', line_foreground_color='red')
            input('ENTER TO CONTINUE')

    elif user_choice == '2':
        clear()
        banner('Host IP List', title_foreground_color='blue', line_foreground_color='blue')
        host_ip_list()
        input('ENTER TO CONTINUE')

    elif user_choice == '3':
        t = threading.Thread(target=Loading, args=[20]).start()
        init_port_scanner()
        input('ENTER TO CONTINUE')
    elif user_choice == '4':
        banner('Settings', title_foreground_color='yellow', line_foreground_color='yellow')
        input('ENTER TO CONTINUE')
    elif user_choice == '5':
        exit_app()
        
    time.sleep(.5)
    clear()