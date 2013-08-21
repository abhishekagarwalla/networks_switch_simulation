import sys
import getopt
import select
from socket import *

def f_Usage():
        print "Usage:"
        print "python pc.py -s <my src port> -d <switch udp port>"
        exit(1)

def check_port(port):
        #Checks if the port number is valid or not
        if port not in range(1024,65536):
                print "INVALID PORT NUMBER!Port number must be in range 1024-65535"
                f_Usage()
                exit(1)
        else:
                return


def string_manip(temp):
        '''
                In case of more than one comma in input,
                it returns as a string/message after the 2nd comma
        '''
        i=0                     #Flag i : keeps track of string index
        j=0                     #Flag j : keeps track of number of comma's i.e., ","
        for each in temp:
                i=i+1
                if each==",":
                        j=j+1
                        if j ==2:
                                return temp[i:]  # Returns the string from 2nd comma to END

def sender():
        '''
                Accepts the input from user(in PC) and
                also checks if the input is in correct format(<destport>,<message> then
                formats the packet and sends the packet
        '''
        message = raw_input()
        try:
                port,msg_temp = message.split(',',1)

                if int(port) not in range(1024,65536):
                                print "INVALID PORT NUMBER!Port must be range of 1024-65535"
                                print "Enter the input in the format <dst port>,<msg data>"
                else:
                        if len(message)>=1:                             #To check that message is not null/empty
                                msg = port + "," + str(srcport) + "," + msg_temp   #sending message protocol <destport>,<srcport>,<msg>

                        if message !='':
                                mySocket.sendto(msg, ('',destport))
        except ValueError as e:
                print e
                print "Enter the input in the format <dst port>,<msg data>."
                print "<dst port> should be a INTEGER"

def receiver():
        '''
                Prints the message and source port number  and
                if the message is addressed to it ,it displays 
                else discards the message by displaying discarded message
        '''
        recdmessage , addr = mySocket.recvfrom(2048)
        if int(recdmessage.split(',')[0]) == srcport:
                print "Message:",string_manip(recdmessage),"from",recdmessage.split(",")[1]
        else :
                print string_manip(recdmessage),"from",recdmessage.split(",")[1] +"---->  MESSAGE DISCARDED"


srcport  = 5001
destport = 12345

try:
        opts, args = getopt.getopt(sys.argv[1:],"s:d:")

except getopt.GetoptError:
        f_Usage()

for opt, arg in opts:
        if(opt in ("-s")):      #source port number
                try:
                        srcport = int(arg)
                        check_port(srcport)     #function to validate port number
                except ValueError as e:         #ValueError is raised in case port port number is not a integer
                        print "Invalid port number :" , e
                        f_Usage()


        elif(opt in ("-d")):    #destination port number
                try:
                        destport = int(arg)
                        check_port(destport)    #function to validate port number
                except ValueError as e:
                        print "Invalid port number :" , e
                        f_Usage()
        else:
                f_Usage()



print "source port is " , srcport
print "destination port is " , destport
print "---------------------------------"
print "Enter the input in the format <dst port>,<msg data>"
print "Enter ctrl-c to exit"

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(('', srcport))
inputs = [mySocket,sys.stdin]
running=1

try:
        while running:
                inputready,outputready,exceptns = select.select(inputs,[],[])
                for s in inputready:
                        if s == sys.stdin:
				   sender()        #Function to handle inputs
                        else:
                                receiver()      #Function to handle received message
except KeyboardInterrupt as e:
        mySocket.close()
        print "----------------------------Exiting----------------------------------"
        sys.exit(0)

