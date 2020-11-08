import os
import getpass
print("\t\t\t\t WELCOME TO MY MENU")
os.system("espeak-ng 'Welcome to my menu' ")
passwd = getpass.getpass("Enter your password")
if passwd !=  "lw" :
 print("password incorrect ....")
 exit()

r = input("enter your choice remote/local: ")


#print(ch)
while True:
	os.system("sleep 3")
	os.system("clear")
	print("""
	\n
	press 0: to show ip_address
	press 1: to run date
	press 2 : to cal
	press 3 : to reboot
	press 4 : to user create
	press 5 : start webserver
	press 5.1 : stop webserver
	press 6 : check status of webserver.
	press 7 : to exit 
	press 8 : to activate the slave node
	press 9 : to activate the master
	press 10 : show the hadoop cluster
	press 11 : to start docker
	press 12 : to stop docker
	press 13 : check the status of docker
	press 14 : check the images available in docker
	press 15 : launch docker container
	press 16 : downlaod new docker image  
	press 17 : check the staus of ram
	press 18 : list the partion in hardisks
	press 19 : list the block storage in system
	press 20 : speak for me
	press 21 : show all working ports
	press 22 : ping another system
	press 23 : list the files
	press 24 : create a file
	press 25 : create a empty file
	press 26 : view a file
	press 27 : create and append a file.
	press 28 : copy one file to another
	press 29 : create a direcroty
	press 30 : remove a file
	press 31 : remove a directory
	press 32 : capture the packets
	press 33 : check the process id
	press 34 : kill a program 
	press 35 : open python terminal
	press 36 : tell me evrthing about cpu 
	press 37 : open the task manager
	press 38 : clear cache
	
	""")




	#r = input("enter your choice remote/local: ")

	ch = input("Enter ur choice : ")
	print(ch)


	if  r == "local" :
	 if int(ch) == 0:
	  os.system("ifconfig")
	 if int(ch) == 1:
	  os.system("date")
	 elif int(ch) == 2:
	  os.system("cal")
	 elif int(ch) == 3:
	  os.system("reboot")
	 elif int(ch) == 5:
	  os.system("systemctl start httpd")
	 elif int(ch) == 6:
	  os.system("systemctl status httpd")
	 elif int(ch) == 8:
	  os.system("hadoop-daemon.sh start datanode")
	  os.system("jps")
	  
	 elif int(ch) == 9:
	  print("please choose the remote login to configure master")

	 elif int(ch) == 10:
	  os.system("hadoop dfsadmin -report")
	 elif int(ch) == 11:
	  os.system("systemctl start docker")
	 elif int(ch) == 12:
	  os.system("systemctl stop docker")
	 elif int(ch) == 13:
	  os.system("systemctl status docker")
	 elif int(ch) == 14:
	  os.system("docker images")
	 elif int(ch) == 15:
	  img = input("Enter the image you want to launch : ")
	  ver = input("Enter the version you want to launch : ")
	  os.system("docker run -it {}:{}". format(img,ver))
	 elif int(ch) == 16:
	  img = input("Enter the image name : ")
	  ver = input("Enter the version : ")
	  os.system("docker run -it {}:{}". format(img,ver))
	 elif int(ch) == 17:
	  os.system("free -m")
	 elif int(ch) == 18:
	  os.system("fdisk -l")
	 elif int(ch) == 19:
	  os.system("lsblk")
	 elif int(ch) == 20:
	  ch = input("Enter the keyword : ")
	  os.system("espeak-ng {}". format(ch))
	 elif int(ch) == 21:
	  os.system("netstat -tnlp")
	 elif int(ch) == 22:
	  n =input("Enter the ip : ")
	  os.system("ping {}". format(n))
	 elif int(ch) == 23:
	  os.system("ls")
	 elif int(ch) == 24:
	  name=input("Enter the name of the file : ")
	  os.system("gedit {}". format(name))
	 elif int(ch) == 25:
	  empty = input("Enter the file name : ")
	  os.system("touch {}". format(empty))
	 elif int(ch) == 26:
	  empty = input("Enter the file name to view : ")
	  os.system("cat {}". format(empty))
	 elif int(ch) == 27:
	  empty = input("Enter the file name to edit : ")
	  os.system("cat > {}". format(empty))
	 elif int(ch) == 28:
	  empty = input("Enter the file to copy from with path : ")
	  new = input("Enter the name of newfile : ")
	  os.system("cp {} {}". format(empty,new))
	 elif int(ch) == 29:
	  empty = input("Enter directory name : ")
	  os.system("mkdir /{}". format(empty))
	 elif int(ch) == 30:
	  empty = input("Enter file name with path : ")
	  os.system("rm {}". format(empty))
	 elif int(ch) == 31:
	  empty = input("Enter the directory name with path to be removed : ")
	  os.system("rm -rf {}". format(empty))
	 elif int(ch) == 32:
	  os.system("tcpdump")
	 elif int(ch) == 33:
	  empty = input("Enter the process name : ")
	  os.system("pgrep {}". format(empty))
	 elif int(ch) == 34:
	  empty = input("Enter the processid of the program : ")
	  os.system("kill {}". format(empty))
	 elif int(ch) == 35:
	  os.system("python3")
	 elif int(ch) == 36:
	  os.system("lscpu")
	 elif int(ch) == 36:
	  os.system("top")
	 elif int(ch) == 37:
	  os.system("lscpu")
	 elif int(ch) == 38:
	  os.system("free -m")
	  os.system("echo 3 > /proc/sys/rm/drop-caches")
	  os.system("free-m")



	 elif int(ch) == 7:
	  exit()
	 else:
	  print("not supported")
	elif r == "remote":
	 ip=input("enter remote ip: ")
	 if int(ch) == 0:
	  os.system(" ssh {} ifconfig ". format(ip))
	 if int(ch) == 1:
	  os.system(" ssh {} date ". format(ip))
	 elif int(ch) ==2 :
	  os.system(" ssh {} cal". format(ip))
	 elif int(ch) == 3 : 
	  os.system(" ssh {} reboot" .  format(ip))
	 elif int(ch) == 5:
	  os.system("ssh {} systemctl start httpd" .format(ip))
	 elif int(ch) == 6:
	  os.system("ssh {} systemctl status httpd" .format(ip))
	 elif int(ch) ==8 :
	  print("this system is configures as data node , choose local login")
	 elif int(ch) ==9 :
	  os.system(" ssh {} hadoop-daemon.sh start namenode" . format(ip))
	  os.system(" ssh {} jps" . format(ip))

	 elif int(ch) == 10:
	  os.system("ssh {} hadoop dfsadmin -report". format(ip))
	 elif int(ch) == 11:
	  os.system("ssh {} systemctl start docker". format(ip))
	 elif int(ch) == 12:
	  os.system("ssh {} systemctl stop docker". format(ip))
	 elif int(ch) == 13:
	  os.system("ssh {} systemctl status docker". format(ip))
	 elif int(ch) == 14:
	  os.system("ssh {} docker images". format(ip))
	 elif int(ch) == 15:
	  img = input("Enter the image you want to launch : ")
	  ver = input("Enter the version you want to launch : ")
	  os.system("ssh {} docker run -it {}:{}". format(ip,img,ver))
	 elif int(ch) == 16:
	  img = input("Enter the image : ")
	  ver = input("Enter the version : ")
	  os.system("ssh {} docker run -it {}:{}". format(ip,img,ver))
	 elif int(ch) == 17:
	  os.system("ssh {} free -m". format(ip))
	 elif int(ch) == 18:
	  os.system("ssh {} fdisk -l". format(ip))
	 elif int(ch) == 19:
	  os.system("ssh {} lsblk". format(ip))
	 elif int(ch) == 20:
	  ch = input(" Enter the keyword : ")
	  os.system("ssh {} espeak-ng {}". format(ip,ch))
	 elif int(ch) == 21:
	  os.system("ssh {} netstat -tnlp". format(ip))
	 elif int(ch) == 22:
	  n =input("Enter the ip : ")
	  os.system("ssh {} ping {}". format(ip,n))
	 elif int(ch) == 23:
	  os.system("ls")
	 elif int(ch) == 24:
	  name=input("Enter the name of the file : ")
	  os.system("ssh {} gedit {}". format(ip,name))
	 elif int(ch) == 25:
	  empty = input("Enter the file name : ")
	  os.system("ssh {} touch {}". format(ip,empty))
	 elif int(ch) == 26:
	  empty = input("Enter the file name to view : ")
	  os.system("ssh {} cat {}". format(ip,empty))
	 elif int(ch) == 27:
	  empty = input("Enter the file name to edit : ")
	  os.system("ssh {} cat > {}". format(ip,empty))
	 elif int(ch) == 28:
	  empty = input("Enter the file to copy from with path : ")
	  new = input("Enter the name of newfile : ")
	  os.system("ssh {} cp {} {}". format(ip,empty,new))
	 elif int(ch) == 29:
	  empty = input("Enter directory name : ")
	  os.system("ssh {} mkdir /{}". format(ip,empty))
	 elif int(ch) == 30:
	  empty = input("Enter file name with path : ")
	  os.system("ssh {} rm {}". format(ip,empty))
	 elif int(ch) == 31:
	  empty = input("Enter the directory name with path to be removed : ")
	  os.system("ssh {} rm -rf {}". format(ip,empty))
	 elif int(ch) == 32:
	  os.system("ssh {} tcpdump". format(ip))
	 elif int(ch) == 33:
	  empty = input("Enter the process name : ")
	  os.system("ssh {} pgrep {}". format(ip,pempty))
	 elif int(ch) == 34:
	  empty = input("Enter the processid of the program : ")
	  os.system("ssh {} kill {}". format(ip,empty))
	 elif int(ch) == 35:
	  os.system("ssh {} python3". format(ip))
	 elif int(ch) == 36:
	  os.system("ssh {} lscpu". format(ip))
	 elif int(ch) == 36:
	  os.system("ssh {} top". format(ip))
	 elif int(ch) == 37:
	  os.system("ssh {} lscpu". format(ip))
	 elif int(ch) == 38:
	  os.system("ssh {} free -m". format(ip))
	  os.system("ssh {} echo 3 > /proc/sys/rm/drop-caches". format(ip))
	  os.system("ssh {} free-m". format(ip))



	 else:
	  print("not supported")
	else:
	 print("not supported login")



