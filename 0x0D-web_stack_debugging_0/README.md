# 0x0D. Web stack debugging #0

### Concepts
For this project, we expect you to look at these concepts:

- Network basics
	- Network basics
	Networking is a big part of what made computers so powerful and why the Internet exists. It allows machines to communicate with each other.

	- [What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)
	- [What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
	- [What is TCP/IP](https://www.avast.com/c-what-is-tcp-ip#)
	- [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)

## Docker
### Readme
[What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
Let’s first pull a Docker image and run a container:

```
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
vagrant@ubuntu-xenial:~$ docker run -d -ti ubuntu:16.04
Unable to find image 'ubuntu:16.04' locally
16.04: Pulling from library/ubuntu
34667c7e4631: Pull complete
d18d76a881a4: Pull complete
119c7358fbfc: Pull complete
2aaf13f3eff0: Pull complete
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:16.04
e1fc0d4bbb5d3513b8f7666c91932812da7640346f6e05b7cfc3130ddbbb8278
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
e1fc0d4bbb5d        ubuntu:16.04        "/bin/bash"         About a minute ago   Up About a minute                       keen_blackwell
vagrant@ubuntu-xenial:~$
```
Note that docker command will pull the Ubuntu docker container image from the Internet and run it. I let you look at the meaning of the flags using the command docker run --help, the main idea is that it keeps the container up and running.

To execute a command on the Docker container, use docker exec:

```
vagrant@ubuntu-xenial:~$ docker exec -i e1fc0d4bbb5d hostname
e1fc0d4bbb5d
vagrant@ubuntu-xenial:~$ hostname
ubuntu-xenial
vagrant@ubuntu-xenial:~$
```
If you want to connect to your Docker container and use Bash, you need to use docker exec -ti:
```
vagrant@ubuntu-xenial:~$ docker exec -ti e1fc0d4bbb5d /bin/bash
root@e1fc0d4bbb5d:/# echo "I am in $(hostname) Docker container"
I am in e1fc0d4bbb5d Docker container
root@e1fc0d4bbb5d:/# exit
exit
vagrant@ubuntu-xenial:~$
```

If you want to stop a container, use docker stop:
```
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
e1fc0d4bbb5d        ubuntu:16.04        "/bin/bash"         5 minutes ago       Up 5 minutes                            keen_blackwell
vagrant@ubuntu-xenial:~$ docker stop e1fc0d4bbb5d
e1fc0d4bbb5d
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
vagrant@ubuntu-xenial:~$
```

# Web stack debugging
### Intro
Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

## Non-exhaustive guide to debugging
### School specific
If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

### Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

- Is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? - ```netstat``` -```lpdn``` - run as root or sudo so that you can see the process for each listening port
- It is listening on the correct server IP? - ```netstat``` is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in ```/var/log``` and ```tail -f``` is your friend
- Can I connect to the HTTP port from the location I am browsing from? - ```curl``` is your friend
There is a good chance that at this point you will already have found part of the issue.

## Get a quick overview of the machine state

[Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw)

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with [5 commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) in a minute or less:

```w```
- shows server [uptime](https://www.techtarget.com/whatis/definition/uptime-and-downtime) which is the time during which the server has been continuously running
- shows which users are connected to the server
- load average will give you a good sense of the server health - (read more about load here and here)

```history```
- shows which commands were previously run by the user you are currently connected to
- you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
- where you might want to start your debugging work

```top``
- shows what is currently running on this server
- order results by CPU, memory utilization and catch the ones that are resource intensive

```df```
- shows disk utilization

```netstat```
- what port and IP your server is listening on
- what processes are using sockets
- try ```netstat -lpn``` on a Ubuntu machine

### Machine
Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

- Does the server have free disk space? - ```df```
- Is the server able to keep up with CPU load? - ```w, top, ps```
- Does the server have available memory? ```free```
- Are the server disk(s) able to keep up with read/write IO? - ```htop```
If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

- free up resources (stop process(es) or reduce their resource consumption)
- increase the machine resources (adding memory, CPU, disk space…)
- distributing the resource usage to other machines


### Network issue

For the machine level, you want to ask yourself these questions:

- Does the server have the expected network interfaces and IPs up and running? ```ifconfig```
- Does the server listen on the sockets that it is supposed to? netstat (netstat -```lpd or netstat -lpn)```
- Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
- Does the server have the correct firewall rules? ```iptables```, ```ufw:```
	- ```iptables -L```
	- ```sudo ufw status```

### Process issue

If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

- Is the software started? init, init.d:
```service NAME_OF_THE_SERVICE status```
```/etc/init.d/NAME_OF_THE_SERVICE status```
- Is the software process running? pgrep, ps:
```pgrep -lf NAME_OF_THE_PROCESS```
```ps auxf```
-Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend

### Debugging is fun

Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :)


