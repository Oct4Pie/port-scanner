# Port-Scanner
A fast and multi-threaded port scanner written in python

Usage:
`python3 scanner.py [-h] ip port_range threads [timeout]`

timeout is optional and set to None by deafult

The number of threads are recommended to be between 100 and 300 for normal computers.

e.g.

`python3 scanner.py 127.0.0.1 0-500 150 1`


![nmap](/images/nmap.png)
![scanner.py](/images/scanner.png)

