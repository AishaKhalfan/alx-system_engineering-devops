# 0x08-networking_basics_2

## Resources

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

## man or help:

- ifconfig
- telnet
- nc
- cut

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is /etc/hosts
- How to display your machine’s active network interfaces

# TASK 0: Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.
- The checker is running on Docker, so make sure to read this

# TASK 1: Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

Example:

sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
- Obviously, the IPs displayed may be different depending on which machine you are running the script on.

- Note that we can see our localhost IP :)

# TASK 2: Port listening on localhost
Write a Bash script that listens on port 98 on localhost.

Terminal 0

Starting my script.

sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.

sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test
Terminal 0

Receiving the text on the other side.

sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test
