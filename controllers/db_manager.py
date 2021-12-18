import os

def load_data(path: str) -> dict:
    """
    # load_data (function)

    This function will get a txt file and broken the line and columns in a list.
    """
    with open(path, 'r') as dbfile:
        processed_data : list = []

        for line in dbfile.read().splitlines():
            data: list = line.split(',')
            processed_data.append({'port': data[0].strip(), 'status': data[1].strip()})
    
    return processed_data

def check_existence_in_directory(value: str) -> bool:
    """
    # check_existence_in_directory (function)
    """

    directories: list = os.listdir(os.path.abspath('database'))
    return True if value in directories else False

def scan_current_ordering(ip: str) -> int:
    directories: list = os.listdir(os.path.abspath(f'database\\{ip}')) 
    scan_range: list = []

    if len(directories) != 0:
        for value in directories:
            scan_range.append(int(value.replace('scan_', '').replace('.txt', '')))

        scan_range.sort()

        
        for value in enumerate(scan_range):
            if value[1] != scan_range[value[0] - 1] + 1 and value[1] != 1:
                return scan_range[value[0] - 1] + 1

            last = value[1]
        else:
            return last + 1
    else:
        return 1

def create_new_data_host(ip: str) -> None:
    path: str = os.path.abspath('.\database') + '\\' + ip
    existence = check_existence_in_directory(ip)

    if existence == False:
        os.mkdir(path)
    else:
        return f'IP: {ip} already exist'

def create_new_scan(data_scan: list, ip: str) -> None:
    # checking scans
    path: str = os.path.abspath('.\database') + '\\' + ip + '\\' + f'scan_{scan_current_ordering(ip)}.txt'

    with open(path, 'w') as db_file:
        processed: str = ''
        for data in data_scan:
            processed += f"{data['port']}, {data['status']}\n"
        
        db_file.write(processed)

def list_hosts() -> list:
    directories: list = os.listdir(os.path.abspath('database'))
    return directories
