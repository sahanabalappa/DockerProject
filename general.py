import os
import subprocess as sp
import time
import start
import main_menu
########################################## GENERAL ####################################################
def general():
	os.system("clear")
	while True:
		start.start()
		os.system("tput setaf 10")
		print('''
[1] RUN NEW COMMAND
[2] HELP
[3] RUN CONTAINER
[4] DOCKER INFO
[5] RAM CONSUMPTION
[6] RAM CONSUMPTION IN REAL TIME
[7] ALL STOPPED / RUNNING CONTAINERS
[8] REMOVE ALL (stopped + running) DOCKER  CONTAINER
[9] CREATE IMAGE
[10] CONTAINER DETAIL 
[11] CPU SHARE 
[12] PORTS RUNNING
[13] CONTAINER LOGS
[14] YUM WHATPROVIDES
[15] KERNAL VERSION
[16] ID OF ALL CONTAINERS
[17] PROCESS TREE
[18] IPTABLES
[19] SEND FILE / FOLDER
 
[0] BACK
[99] EXIT 
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("COMMAND : ")
			os.system(f"{inp}")
		elif i==2:
			inp=input("COMMAND  : ")
			os.system(f"man {inp}")
		elif i==16:
			os.system("docker container ls -a -q")
		elif i==19:
			inp2=input("FILE / FOLDER NAME : ")
			inp=input("IP ADDRESS : ")
			inp1=input("DESTINATION PATH : ")
			output=sp.getoutput(f"nmap -sT {inp} | grep ^H | cut -c 1-4")
			if "Host" in output:
				os.system(f"scp {inp2} root@{inp}:{inp1}")
			else:
				os.system("tput setaf 9 && echo 'HOST IS NOT UP !!!' && tput setaf 15")
		elif i==3:
			inp=input("IMAGE_NAME:VERSION : ")
			os.system(f"docker run -it {inp}")
		elif i==4:
			os.system("docker info")
		elif i==5:
			os.system("free -m")
		elif i==6:
			os.system("watch -n 1 free -m")
		elif i==7:
			os.system("docker ps -a")
		elif i==8:
			os.system("docker container rm -f $(docker container ls -q -a)")
		elif i==9:
			inp=input("CONTAINER NAME : ")
			inp1=input("IMAGENAME WITH VERSION : ")
			os.system(f"docker commit {inp} {inp1}")
		elif i==10:
			inp=input ("CONTAINER NAME : ")
			os.system(f"docker container inspect {inp}")
		elif i==11:
			os.system("lscpu")
		elif i==12:
			os.system("netstat -tnlp")
		elif i==13:
			inp=input("ENTER THE CONTAINER NAME  : ")
			os.system(f"docker logs  -f {inp}") # -f -> to show logs in real time
		elif i==14:
			inp=input("ENTER THE SOFTWARE NAME : ")
			os.system(f"yum whatprovides {inp}")
		elif i==15:
			os.system("uname -r")
		elif i==17:
			os.system("pstree")
		elif i==18:
			os.system("iptables -F && iptables -nvL")
		elif i==0:
			main_menu.main_menu()
		elif i==99:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue..........")
		os.system("tput setaf 15 && clear")


