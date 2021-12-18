from view import *
import controllers
from controllers.db_manager import *

# Main Loop
while True:
    opc = menu(['\033[32mStart Search\033[m','\033[33mList Hosts\033[m', '\033[34mAdd Hosts\033[m', '\033[31mExit\033[m'])
    if opc == 1:
        print('\033[32mStarting...\033[m')
        time.sleep(2)
    elif opc == 2:
        print('\033[33mList Hosts\033[m')
        
        for index, host in enumerate(list_hosts()):
            print(index, host)
        
        input('[ENTER TO CONTINUE]')
        time.sleep(2)

    elif opc == 3:
        print('\033[34mAdd Hosts\033[m')
        time.sleep(2)
    elif opc == 4:
        print('\n \033[31mBye Bye... \033[m \n')
        break
    else:
        print('\033[31mInvalid Option \033[m')
        time.sleep(2)


