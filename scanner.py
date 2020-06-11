#!/usr/bin/env python3
import sys
import time
import socket
import argparse
from threading import Thread

open_ports = []


def isalive():
    for thread in threads:
        if thread.isAlive():
            return True

    return False


def scan(port):
    # ConnectionRefusedError exception will be raised in case of a
    # closed port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(args.timeout)
        sock.connect((args.ip, port))
    except:
        return  # Terminate the function if there is an exception

    open_ports.append(port)


if __name__ == '__main__':
    threads = []
    length = 0  # Used to keep track of threads' length
    start = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="the target ipv4", type=str)
    parser.add_argument("port_range", help="the port range: 0 to 200 => \
        0-200, inclusive", type=str)
    parser.add_argument("threads", help="the maximun amount of threads to\
         be executed at the same time; recommended: 100-400", type=int)
    parser.add_argument("timeout", nargs='?', help="the time out for each\
        request", type=float, default=None)

    args = parser.parse_args()
    port_range = args.port_range.split('-')

    for port in range(int(port_range[0]), int(port_range[1])+1):
        if length % args.threads == 0:
            # Wait for threads in the list to finish
            while isalive():
                time.sleep(0.0001)
            # Empty the list to make ready for the next cycle, if any
            threads.clear()

        thread = Thread(target=scan, args=[port])
        threads.append(thread)
        thread.start()
        length += 1

    # There might be a remainder if ports' range is not divisible
    # by args.threads
    while isalive():
        time.sleep(0.0001)

    for port in open_ports:
        print(f'port {port} open')

    end = time.time()
    # Shorten the time float
    spent = str(end-start)
    spent = spent[:spent.find('.')+3]
    print(f"\nScanned {length} port(s) for {args.ip} in {str(spent)} seconds")
