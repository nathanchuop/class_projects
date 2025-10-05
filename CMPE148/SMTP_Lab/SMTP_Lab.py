from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("127.0.0.1", 1025)
#Fill in
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Nathan\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM:<natchuop@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server after MAIL FROM.')    
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO:<nathan.chuop@sjsu.edu>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] not in ('250', '251'):
    print('250 pr 251 reply not received from server after RCPT TO.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCmd = "DATA\r\n"
clientSocket.send(dataCmd.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server after DATA.')
# Fill in end

# Send message data.
# Fill in start
message = (
    "From: Nathan <natchuop@gmail.com>\r\n"
    "To: School Email <nathan.chuop@sjsu.edu>\r\n"
    "Subject: SMTP Lab Test Message\r\n"
    "\r\n" + msg + "\r\n"
)
clientSocket.send(message.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server after sending message data.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCmd = "QUIT\r\n"
clientSocket.send(quitCmd.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server after QUIT.')


clientSocket.close()
# Fill in end