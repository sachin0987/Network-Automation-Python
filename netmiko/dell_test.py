
import time
from netmiko import Netmiko,ConnectHandler
from getpass import getpass
import datetime,time
import logging
from concurrent.futures import ThreadPoolExecutor

def ssh_connection(HOST,username,password):
    
    try:
        net_connect = ConnectHandler(device_type='cisco_xr', host=HOST, username=username, password=password)
        return net_connect
    
    except Exception as err:
        print(err)
        return err
         
def get_data_from_dell(HOST,username,password):
   
    try: 
        net_connect=ssh_connection(HOST,username,password)
        check_conf=net_connect.send_command("sh version")
        print(check_conf)
    except Exception as e:
        remark="Found Error While Post Check"+ e
        pass

    finally:
        net_connect.disconnect()
        print(check_conf)
        
def main():
    #username = input("Please Enter Username: ")
    username=""
    #password = getpass("Enter OS or SSH key password: ")
    password=""
    #sheet_name=input("Please Enter File Name:")
    try:
        pool = ThreadPoolExecutor(max_workers=1)
        logging.info("Main:Before Creating Thread")
        ip_list= open("file.txt","r")
        listIP = ip_list.read().splitlines()
        for host in listIP:
            pool.submit(get_data_from_dell,host,username,password)
        pool.shutdown(wait=True)

    except Exception as e:
        print(e)
            
if __name__ == "__main__": 
    main()
    
