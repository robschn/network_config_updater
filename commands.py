
import multiprocessing
from netmiko import ConnectHandler
from my_devices import device_list


def issue_command(a_device, config_commands):
    
    ip_address = a_device['ip']

    print(f'\nConnected to {ip_address}..')
    
    net_connect = ConnectHandler(**a_device)
    
    net_connect.send_config_set(config_commands)

    show_run = net_connect.send_command('sh run | inc http')

    if 'no' in show_run:
        print(f'Config updated for {ip_address}!')
    else:
        print(f'Config **NOT** updated {ip_address}!!')
    

def main():
    
    commands = [
        'no ip http server',
        'no ip http secure-server'
    ]

    for device in device_list:
        issue_command(device, commands)

if __name__ == "__main__":
    main()