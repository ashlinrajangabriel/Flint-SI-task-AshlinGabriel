*Flint SI-task with python script using python libraries and system utilities*
**Problem Statement**
creating a Python script that configures an 'ens160' local network interface (or one of your choosing) with a static IP address. For the address, select any address from the RFC1918 private address space. You can call out to system utilities or use a Python library to achieve the goal.
Disclaimer: The code must be executed once on existence or nonexistence or multiple times by instantiation.  Class C has been taken for private IP range
**Implementation**
The code has been implemented on two major blocks
1.	Allocate IP to interface if Interface exists
2.	Allocate IP to interface if Interface doesn’t exist
Flow chart 
 
***Pseudocode***
1.	Initialize the program with a function call
2.	Check for interfaces that matches your device criteria with regular expressions
3.	If the Interface is found allocate the IP by device count over the subnet 
4.	Display the IP configuration alongside of device Interface
5.	If the interface is not found create the dummy interface
6.	Allocate the IP by device interface count over subnet
7.	Display the IP configuration alongside of device interface


**Future Enhancements:**

1.	Can be optimized and could be run as a scheduled service or daemon service in active listening loop.
2.	The code can also use subprocess System library instead of OS module
3.	The code can also be improved with object-oriented approach.
