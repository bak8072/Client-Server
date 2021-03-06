from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Learning Computer Networking"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = (1025, '127.0.0.1')

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailServer, mailPort))

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] !='220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'ELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailFrom = "Mail FROM : <myemail@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print("After MAIL FROM Command: "+recv2)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: <destination@gmail.com>\r\n"
    clientsSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print("After MAIL FROM command: "+recv3)
    if recv1[:3] !='250':
        print('250 reply not received from server.')

    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv.decode()
    print("After DATA command:"+recv4)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send message data.
    message = raw_impute("Enter your message:r\n")
   
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:"+recv_msge.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and get server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv5 = clientSocket.recv(1024)
    print(recv5.decode())
    clientSocket.close()

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
