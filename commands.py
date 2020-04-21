import yaml

from netmiko import ConnectHandler
from getpass import getpass

def grab_devices():
    with open('devices.yaml', 'r') as f:
        doc = yaml.safe_load(f)

    switches = doc['switch']

    device_ips = []

    for i in switches.keys():
        device_ips.append(switches[i])

    username = input('Enter standard username: ')
    password = getpass('Enter standard password: ')

    device_list = []

    for ip_address in device_ips:
        curr_device = {
            "device_type": "cisco_ios",
            "ip": ip_address,
            "username": username,
            "password": password,
        }
        device_list.append(curr_device)
    
    return device_list


def issue_command(a_device, config_commands):
    
    net_connect = ConnectHandler(**a_device)
    
    # Grab hostname
    find_hostname = net_connect.find_prompt()
    hostname = find_hostname.replace("#","")
    print(f'\nConnected to {hostname}..')

    # Send commands
    print(f'Sending commands... {config_commands}')
    net_connect.send_config_set(config_commands)

    # write mem
    print('Writing to memory, please wait...')
    net_connect.send_command('write mem')
    print('Done!')


def main():

    device_list = grab_devices()

    print(device_list)

    commands = [
        'int g1/0/11',
        'shut',
        'desc Updated With Python',
        'no shut'
    ]

    for device in device_list:
        issue_command(device, commands)

    print('All switches have been updated! Exitting..')

if __name__ == "__main__":
    main()
