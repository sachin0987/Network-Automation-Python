import paramiko 

def main():
    '''
    Use Paramiko to retrieve the entire 'show version' output.
    '''
    ip_addr = raw_input("Enter IP address: ")
    username = 'pyclass'
    password = getpass()
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()

    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn)

    output = send_command(remote_conn, cmd='show version')
    print ('\n>>>>')
    print (output)
    print ('>>>>\n')h 