-------------------------------------------------
Abhhishek Agarwalla
1pi10is135
-------------------------------------------------

  Assignment : 02
  Project    : B3

-------------------------------------------------

Group Members :
---------------
Akshay R Bastawad       1PI10IS010
Kushwant singh Saluja   1PI10IS127
Abhishek Agarwalla      1PI10IS135

-------------------------------------------------

STEPS:
-----
step1: Program names: (1)sw.py          (2)pc.py
--------------------

step2:Execution:
---------------
(1)sw.py
        python sw.py -s <my port>, -p <port-1>, ..., <port-N>
Example:python sw.py -s 12345 -p 5001,5002,5003,5004

(2)pc.py
        python pc.py -s <my src port> -d <switch udp port>
Example:python pc.py -s 5001 -d 12345

UNDERSTANDING:
--------------
Usage of Command-Line Arguments.
1)Switch that has maximum of 8 ports.
2)PCs connected to the switch.
3)UDP connection between the switch and PCs.
4)Port number to be used instead of MAC ADDRESS of the PC.
5)When PC sends the packet for the first time the switch learns the pcs mac address(here port no.) and then forwards the packet.
6)The packet is to be send in the format <dstport> ,<src port>, <msg data>.
7)The switch updates the table if there is no entry for port number else it does not update.
8)If the destination port no. is not known,the switch will broadcast the message to all PCs except the sender.
9)If destination port no. is known then it unicast it to the specific destination PC.

Note:
-----
a)When PC sends to itself,packet is send to switch.The switch learns and then forward the packet back to PC

b)When switch port is assigned as PC port/switch connected to itself
  Example:python sw.py -s 12345 -d 5001,5002,12345
   then there shall be looping thus the condition is avoided.

c)When PC input as <dst port>, <msg data>
                         5002,a,a,a.
  It takes <dst port> as 5002
           <msg data> as "a,a,a,"


TESTING:
--------
Done on local system,i.e. same system using multiple terminal.
1)Self-Looping:If Switch port connected to itself.Prevent this condition by checking and deacivating the port.
2)If "," in message then must not split and take as a part of message.
3)Wrong port no., Port no. out of range, if port no. is string.
4)Command-line input and possible exceptions.
5)prints the message as Discarded message if broadcasted message is not for the destined PC.
6)Max of 8 ports.More than 8 ports not allowed.
7)when ctrl+C pressed, closing of socket and exit.


MODULES USED:
-------------
1 socket : To handle creation and operation of sockets and respective functions.
2 getopt : To take values from Commandline.
3 sys : For successful or unsuccessful termination of program using sys.exit([status]).
4 select:To use select.select() to wait for I/O efficiently


CONTRIBUTION:
-------------
1.1PI10IS010 : Core programming , command-line script , testing
2.1PI10IS127 : Core Programming , Text-Decoration     , testing
3.1PI10IS135 : Core Programming , Exception-handling  , testing


CHALLENGES FACED:
----------------
1)Checking various exception cases.
2)understanding select.select() implementation.(Took reference from stackoverflow.com)
3)Implementing condition:if there is "," in the message,then it should not split it.

THINGS NOT DONE:
----------------
1)The code handles only one switch (does not handle multiple switches).
        Handles multiple switch only if there is no loop.
2)Buffer problem not handled using select.select().

