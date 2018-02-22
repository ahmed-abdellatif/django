# Returns your ip address and machine name

# import socket library
import socket

# print machine info function definition
def print_machine_info():
	
# call the gethostname() method from the socket library
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" %host_name) 
    print("IP address: %s " %ip_address)
if __name__ == '__main__':
   print_machine_info()
