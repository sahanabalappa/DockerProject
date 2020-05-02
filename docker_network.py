import os
import subprocess as sp
import time
import start
import main_menu
########################################## DOCKER NETWORK #############################################
def docker_network():
	os.system("clear")
	while True:
		start.start()
		os.system("tput setaf 10")
		print('''
[1] SHOW NETWORK
[2] CREATE NETWORK
[3] DISCONNECT NETWORK
[4] RUN CONTAINER IN USERMADE NETWORK
[5] INFO OF A NETWORK
[6] REMOVE NETWORK
[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("CHOICE : "))
		if i==1:
			os.system("docker network ls")
		elif i==2:
			inp=input("NETWORK NAME : ")
			inp1=input("DRIVER NAME : ")
			inp2=input("SUBNET RANGE : ")
			os.system(f"docker network create --driver {inp1} --subnet {inp2} {inp}")
		elif i==3:
			inp=input("NETWORK NAME : ")
			inp1=input("CONTAINER NAME : ")
			os.system(f"docker network disconnect {inp} {inp1}")
		elif i==4:
			inp=input("CONTAINER NAME : ")
			inp1=input("NETWORK NAME : ")
			inp2=input("IMAGE NAME : ")
			os.system(f"docker run -it --name {inp} --network {inp1} {inp2}")
		elif i==5:
			inp=input("NETWORK NAME : ")
			os.system(f"docker network inspect {inp}")
		elif i==6:
			inp=input("NETWORK NAME : ")
			os.system(f"docker network rm {inp}")
		elif i==0:
			main_menu.main_menu()
		elif i==99:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue.......")
		os.system("tput setaf 15 && clear")

