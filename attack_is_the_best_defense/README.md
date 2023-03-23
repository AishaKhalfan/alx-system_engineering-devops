# Attack is the best defense
- DevOps - Scripting - Hacking

### Concepts
For this project, we expect you to look at these concepts:

- [Network basics](https://intranet.alxswe.com/concepts/33)
  * [What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)
  * [What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
  * [What is TCP/IP](https://www.avast.com/c-what-is-tcp-ip#)
  * [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)

- [Docker](https://intranet.alxswe.com/concepts/65)
# Docker
### Readme
- [What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
  
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

Note that docker command will pull the Ubuntu docker container image from the Internet and run it. I let you look at the meaning of the flags using the command docker run --help, the main idea is that it keeps the container up and running.

vagrant@ubuntu-xenial:~$ docker exec -ti e1fc0d4bbb5d /bin/bash
root@e1fc0d4bbb5d:/# echo "I am in $(hostname) Docker container"
I am in e1fc0d4bbb5d Docker container
root@e1fc0d4bbb5d:/# exit
exit
vagrant@ubuntu-xenial:~$

If you want to stop a container, use docker stop:
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
e1fc0d4bbb5d        ubuntu:16.04        "/bin/bash"         5 minutes ago       Up 5 minutes                            keen_blackwell
vagrant@ubuntu-xenial:~$ docker stop e1fc0d4bbb5d
e1fc0d4bbb5d
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
vagrant@ubuntu-xenial:~$
```

# Resources
### Read or watch:

- Network sniffing
- ARP spoofing
- Connect to SendGrid’s SMTP relay using telnet
- What is Docker and why is it popular?
- Dictionary attack

### man or help:

- tcpdump
- hydra
- telnet
- docker

#TASKS
## Tasks 0: ARP spoofing and sniffing unencrypted traffiC
![alt text](https://github.com/AishaKhalfan/alx-system_engineering-devops/blob/master/attack_is_the_best_defense/ARP.png?raw=true)

Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. Traffic going through a network can be intercepted by a malicious machine pretending to be another network device. Once the traffic is redirected to the malicious machine, the hacker can keep a copy of it and analyze it for potential interesting information. It is important to note that the traffic must then be forwarded to the actual device it was supposed to go (so that users and the system keep going as if nothing happened).

Any information that is not encrypted and sniffed by an attacker can be seen by the attacker - that could be your email password or credit card information. While today’s network security is much stronger than it used to be, there are still some legacy systems that are using unencrypted communication means. A popular one is telnet.

In this project, we will not go over ARP spoofing, but we’ll start by sniffing unencrypted traffic and getting information out of it.

[Sendgrid](https://sendgrid.com/) offers is an emailing service that provides state of the art secure system to send emails, but also supports a legacy unsecured way: telnet. You can create an account for free, which is what I did, and send an email using telnet:

```
khalfan@ubuntu$ telnet smtp.sendgrid.net 587
Trying 167.89.121.145...
Connected to smtp.sendgrid.net.
Escape character is '^]'.
220 SG ESMTP service ready at ismtpd0013p1las1.sendgrid.net
EHLO ismtpd0013p1las1.sendgrid.net
250-smtp.sendgrid.net
250-8BITMIME
250-PIPELINING
250-SIZE 31457280
250-STARTTLS
250-AUTH PLAIN LOGIN
250 AUTH=PLAIN LOGIN
auth login           
334 VXNlcm5hbWU6
VGhpcyBpcyBteSBsb2dpbg==
334 UGFzc3dvcmQ6
WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA==
235 Authentication successful
mail from: khalfan@aisha.fr
250 Sender address accepted
rcpt to: urban@google.com
250 Recipient address accepted
data
354 Continue
To: Urban
From: Khalfan
Subject: Hello from the insecure world

I am sending you this email from a Terminal.
.
250 Ok: queued as Aq1zhMM3QYeEprixUiFYNg
quit
221 See you later
Connection closed by foreign host.
khalfan@ubuntu$
```

I wrote the script user_authenticating_into_server that performs the authentication steps that I just showed above. Your mission is to execute user_authenticating_into_server locally on your machine and, using tcpdump, sniff the network to find my password. Once you find it, paste the password in your answer file. This script will not work on a Docker container or Mac OS, use your Ubuntu vagrant machine or any other Linux machine.

You can download the script user_authenticating_into_server [here](https://intranet.alxswe.com/rltoken/GE_FoAUArlVccQlt7CuBGA)

DISCLAIMER: you will probably see Authentication failed: Bad 
username / password in the tcpdump trace. It’s normal, we deleted the user to our Sendgrid account. You can’t verify the password found via Sendgrid, only the correction system can!

## TASK 1:Dictionary attack
Password-based authentication systems can be easily broken by using a dictionary attack (you’ll have to find your own password dictionary). Let’s try it on an SSH account.

- Install Docker on your machine Ubuntu
- Pull and run the Docker image sylvainkalache/264-1 with the command docker run -p 2222:22 -d -ti sylvainkalache/264-1
- Find a password dictionary (you might need multiple of them)
- Install and use hydra to try to brute force the account sylvain via SSH on the Docker container
- Because the Docker container is running locally, hydra should access the SSH account via IP 127.0.0.1 and port 2222
- Hint: the password is 11 characters long
Once you found the password, share it in your answer file.
