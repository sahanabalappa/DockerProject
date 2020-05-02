import os
import subprocess as sp
import time
import start
import main
import general
import docker_container
import docker_image
import docker_compose
import docker_network
import docker_storage
######################################### MAIN MENU ##################################################
def main_menu():
	os.system("clear")
	while True:
		start.start()
		os.system("tput setaf 10")
		print('''
[1] INSTALL DOCKER								[100] CHANGE LOCATION
[2] GENERAL 
[3] DOCKER CONTAINER
[4] DOCKER IMAGE
[5] DOCKER COMPOSE
[6] DOCKER NETWORK
[7] DOCKER STORAGE
[0] EXIT 
''')		
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			repo = sp.getoutput("rpm -q docker-ce | cut -c 1-9")
			if repo == "docker-ce":
			    os.system("tput setaf 4 && echo -e 'DOCKER IS ALREADY INSTALLED' && tput setaf 15")
			else:
				os.system("echo -e '[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' > /etc/yum.repos.d/docker.repo && dnf install docker-ce -y")
		elif i==2:
			general.general()
		elif i==3:
			docker_container.docker_container()
		elif i==4:
			docker_image.docker_image()
		elif i==5:
			docker_compose.docker_compose()
		elif i==6:
			docker_network.docker_network()
		elif i==7:
			docker_storage.docker_storage()
		elif i==100:
			docker.main()
		elif i==0:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue.......")
		os.system("tput setaf 15 && clear")

