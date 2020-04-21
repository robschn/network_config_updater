from netmiko import ConnectHandler
from my_devices import device_list


def issue_command(a_device, config_commands):
    
    net_connect = ConnectHandler(**a_device)
    
    # Grab hostname
    find_hostname = net_connect.find_prompt()
    hostname = find_hostname.replace("#","")
    print(f'\nConnected to {hostname}..')

    # Send commands
    print(f'Sending commands... {config_commands}')
    net_connect.send_config_set(config_commands)
    print("Done!")

    # write mem
    print("\nWriting to memory, please wait...")
    net_connect.send_command('write mem')


def main():

    commands = [
        'int g1/0/11',
        'shut',
        'desc Updated With Python',
        'no shut'
    ]

    for device in device_list:
        issue_command(device, commands)

if __name__ == "__main__":
    main()
