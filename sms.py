from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

IPAddress = input("Enter IP Adress: ")

ip = IPv4Address(IPAddress)  # let's create an IP address object
# now create a session
session = AirmoreSession(ip, 2333)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

session.is_server_running  # True if Airmore is running
was_accepted = session.request_authorization()

print(was_accepted)  # True if accepted

service = MessagingService(session)

while 1:
    SMS = input("Enter SMS: ")
    i=int(input("Enter Counter "))
    y=0
    while y<i:
        try:
            j=str(y)
            NSMS=SMS+j
            service.send_message("28880", NSMS)
            y= y+1
            print(f"{bcolors.WARNING}{bcolors.BOLD}")
            print(y)
        except:
            print("SMS Sending Failed")
    print("\nCounting Completed")


