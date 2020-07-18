
from napalm_base import get_network_driver
import napalm_ios
from pprint import pprint

def main():
    ips = input("Enter Ips with spaces: ")
    ipadd = ips.split()
    for ip in ipadd:
        print("connecting to router", ip)
        driver = get_network_driver('ios')
        rtr = driver(ip, 'admin', 'admin') 
        rtr.open()
        pprint(rtr.get_config())
        interfaces = rtr.get_interfaces()
        pprint(interfaces)
        pprint(rtr.get_facts())


if __name__ == "__main__":
    main()

