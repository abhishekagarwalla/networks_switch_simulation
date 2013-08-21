import sys
import getopt
from socket import *

def f_Usage():
        print "python sw.py -s <my port> -p <port-1>, ..., <port-N>"
        sys.exit(1)

def check_port(port):
        #Checks if the port number is valid or not
        if port not in range(1024,65536):
                print "INVALID PORT NUMBER!Port number must be in range  1024-65535"
                return False
        else:
                return True

def sendAll(message,addr):
        #Broadcasts the message if the MAC addr(port num) is not found in switch table
        for each in ports:
                if each != addr :  #Condition to Avoid sending message back to the  sender [ i.e., No reverse path ]
                        mySocket.sendto(message , ('',each))

def send_uni(message):
        #Sends to unique PC [ Unicast message in case the MAC addr(port num) is found in table
        msg = message.split(",")
        if check_port(int(msg[0])): #msg[0] is dest port number
                mySocket.sendto(message,('',int(msg[0])))

def check_table(port_val):
        #checks if the port number is present in table or not.
        if port_val in table:
                return True
        else :
                return False

def update_table(port_val):
        '''
                Updates the Switch table if the port number is not present
                else print the MAC Address exists in table
        '''

        global table           #To refer global variable : table
        if port_val in table:
                print "Received MAC Address " , port_val ," exists in table"
        else:
                table.append(port_val)        # To add port num[MAC ADDR] to table 
                print "updated table is " , table



myport = 12345  #Default source port number
ports  = []     #switch table
table  = []     #switch interface list


try:
        opts, args = getopt.getopt(sys.argv[1:],"s:p:")

except getopt.GetoptError:
        print "error"
        f_Usage()

for opt, arg in opts:
        if(opt in ("-s")):      #source port number
                try:
                        myport = int(arg)
                        if(check_port(myport)== False): #function to validate port number
                                f_Usage()
                except ValueError as e:
                        print "Invalid port number :" , e
                        f_Usage()

        if(opt in ("-p")):      #switch interface port numbers
                try:
                        pts = arg.split(",")
                        for each in pts:
                                if int(each) != myport:   #switch interface number(s) should not be same as src port.
                                        ports.append(int(each))    #Add valid interface number to ports list.
                                        if (check_port(int(each)) == False):    #function to validate port number
                                                f_Usage()
                                else:
                                        print "Connecting a switch interface to itself to not allowed :Interface " ,each," Deactivated"
                        if len(ports) > 8 :     #Maximum 8 switch interface ports allowed. 
                                print "More than 8 interface ports not allowed"
                                sys.exit(1)
                except ValueError as e:
                        print "Invalid port number :" , e
                        f_Usage()


print "myport is " , myport
print "Initial table : ", table
print "Switch interface ports are " , ports
print "------------------------------------"
print "Enter ctrl-c to exit"


mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(('', myport))
try:
        while(1):
                recdMessage, rcvd_addr = mySocket.recvfrom(2048)
                print recdMessage , "from" , rcvd_addr[1]  #rcvd_addr[1] is port number of sender
                update_table(int(rcvd_addr[1]))

                if check_table(int(recdMessage.split(',')[0])): #Function to check if port no. present in table or not
                        send_uni(recdMessage)   #Function to send packet to unique PC [Unicast message]
                else:
                        sendAll(recdMessage , int(rcvd_addr[1]))        #Function to Broadcast the packet to all connected interface

except KeyboardInterrupt as e:

        mySocket.close()
        print "---------------------- Exiting---------------------------"
        sys.exit(0)

