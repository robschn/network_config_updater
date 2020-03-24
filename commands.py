from netmiko import ConnectHandler
from my_devices import device_list


def issue_command(a_device, config_commands):
    
    ip_address = a_device['ip']

    print(f'\nConnected to {ip_address}..')
    
    net_connect = ConnectHandler(**a_device

    print(f'Sending commands...:\n{config_command}')
    net_connect.send_config_set(config_commands)
    

def main():
    
    new_hostname = input('New hostname: ')
    new_ipaddr = input('New IP: ')
    int_vlan = input('VLAN: ')

    commands = [
        f'hostname {new_hostname}_{new_ipaddr}'
        f'int vlan {int_vlan}',
        f'ip address {new_ipaddr} 255.255.255.0'
         
    ]

    for device in device_list:
        issue_command(device, commands)

if __name__ == "__main__":
    main()
