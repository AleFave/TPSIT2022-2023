from socket import AF_INET, SOCK_DGRAM, SOCK_RDM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        msg = "hello world"
        msg = msg.encode('utf8')

        s.sendto(msg, ("192.168.88.255", 5000)) #.255 perchè è il broadcast

if __name__ == "__main__":
    chatClient()