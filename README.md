# Computer Network Programming
This project is deviled in three parts a mail client for sending email with a file attachment, programs for penetration testing  and a chat room application. Currently I am looking for some more ideas that I can leverage socket programming with. Feel free to fork and add some more of your stuff to it. (<strong>WARNING: do not use the programs for penetration testing on a network without permission. You are committing a crime if you do so!</strong>)
## Usage
You can use the mail client to send an email from your email address to a 10 min mail address. I used a Microsoft mail address because it doesn't require a TLS connection. Make sure that you don't hard code your password if you want publish your code later on. Save your password in an encrypted text file. Do not keep your encryption key in same directory as the project that you want to upload in your repo. There is no use for encryption if you make the key also available.<br>
With the pen.testing programs you can DDOS a server in your private network or port scan your own network to see which ports are open.<br>
The chat room application is a client server program on a terminal.
<li> You run the server first then multiple clients on different terminal windows. 
<li> When you run a client at the beginning you type in your chat alias and hit enter.
<li>After you get a message back from the server you now can type in messages that get broadcasted.<li>If you type in the message quit() your client program will be terminated.<br>
You can even setup you own private chat room with your friends. All you have to do is open the port 30333 on your router and allow traffic trough port 30333 on your firewall settings. Now you friends can use your ip address to connect to your chat server. 

## License
[MIT](https://choosealicense.com/licenses/mit/)