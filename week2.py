import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def t_login(username, password, enablepw, ip_addr):
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    outstr = remote_conn.read_until(b"sername:", TELNET_TIMEOUT)
    remote_conn.write(username.encode('utf-8')+b"\n")
    outstr = remote_conn.read_until(b"ssword:", TELNET_TIMEOUT)
    remote_conn.write(password.encode('utf-8')+b"\n")
    outstr = remote_conn.read_very_eager()
    if enablepw:
        remote_conn.write(b"enable\n")
        outstr = remote_conn.read_until(b"ssword:", TELNET_TIMEOUT)
        remote_conn.write(enablepw.encode('utf-8')+b"\n")
        outstr = remote_conn.read_very_eager()
    print(outstr.decode('ascii'))
    time.sleep(1)
    return remote_conn

def t_command(conn_handler, cmd):
    cmd=cmd.rstrip()
    conn_handler.write(cmd.encode('utf-8') + b"\n")
    time.sleep(1)
    outstr = conn_handler.read_very_eager()
    return outstr

def main():
    t_handler = t_login("cisco", "cisco", "cisco", "192.168.5.10")
    print(t_command(t_handler,"term len 0").decode('ascii'))
    print(t_command(t_handler,"sh ver").decode('ascii'))
    t_handler.close


if __name__ == "__main__":
    main()
