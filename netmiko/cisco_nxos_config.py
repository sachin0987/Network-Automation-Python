from netmiko import Netmiko,ConnectHandler
from getpass import getpass
from concurrent.futures import ThreadPoolExecutor

def ssh_connection(host,user,password):
    
    try:
        net_connect = ConnectHandler(device_type='cisco_nxos', host=host, username=user, password=password,port=8181)
        print("connection  Successfull!")
        return net_connect
    except Exception as err:
        print(err)
        return "SSH_Failed"

    
def config_push(host,user,password,interface_name_remove,interface_name_add,vlan):
    interface_name_remove="interface {}".format(interface_name_remove)
    interface_name_add="interface {}".format(interface_name_add)
    cmd_vlan_add="switchport trunk allowed vlan add {}".format(vlan)
    cmd_vlan_remove="switchport trunk allowed vlan remove {}".format(vlan)
    try:
        net_connect=ssh_connection(host,user,password)
        print(net_connect)
        if "SSH_Failed" not in str(net_connect):
            config_commands = [interface_name_remove,cmd_vlan_remove,"exit",interface_name_add,cmd_vlan_add]
            print(config_commands)

            output = net_connect.send_config_set(config_commands) # returns output of config_commands
            print(output)
            print(net_connect.find_prompt())
            
            print("Configuration Successfull!!!!!!")
        else:
            print("Device SSH Failed!! ...Aborting Configuration Task!!!!!!!!!")
            
    except Exception as e:
        print("Error Occurred While Configuring ________Aborting Configuration Task!!!!!!!!!!!!"+e)
 
if __name__ == "__main__":
    host=input("Enter Device IP:")
    user=input("Enter Device User ID:")
    password = getpass("Enter Device Password: ")
    interface_name_remove=input("Enter Device Interface 1:") #Interface Name from which vlan need to remove 
    interface_name_add=input("Enter Device Interface 2:") #Interface Name from where need to add
    vlan=input("Enter VLAN ID:")

    config_push(host,user,password,interface_name_remove,interface_name_add,vlan)
