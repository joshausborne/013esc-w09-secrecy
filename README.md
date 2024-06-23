# Overview

I'm attempting to learn a bit about how to write software that can be used to facilitate direct communication between computers. I chose Python because I like writing Python code, and it's what I'm focusing on learning at this point in my education.

This software utilizes two scripts.
1. The first is server.py. In this file, the server IP address and the port number are hard-coded to that of one of the computers on my home network.
2. The second is client.py. In this case, we also hard-code the IP address and port number of the server.

Starting the server.py is done by running `python server.py` on the server machine.

Starting the client.py is done by running `python client.py` on the client machine(s).

I wrote this software just as first-time experiment. I was given a list, and this idea looked like the second most interestinng option. After failing at building the *most* interesting option, I built this instead. It still has a number of bugs to it, but that's okay. That's the way first drafts are supposed to be.


# Network Communication

This is technically client/server, but kinda has a peer-to-peer feel to it when implemented. There is a server.py running, and the clients all check in with the server, but it feels like peer-to-peer to the end user.

It's TCP, and I'm running it on a custom port (40623).

The messages that are being sent using 1024 bit RSA encryption.

# Development Environment

I wrote this in vim on my Mac Studio and MacBook Pro.

I wrote this in Python, and am using the socket, threading, and key_utils modules.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Geeks for Geeks](https://www.geeksforgeeks.org/simple-chat-room-using-python/) I didn't use anything from here, but I did get some inspiration for how I'd like to improve things.

# Future Work

* I really want to make this a bit nicer.
* I need to make it so that it doesn't send empty lines if I hit enter on a client where I've not input any text.
