import os
import subprocess as sp
import time
import remote_start
import remote_main_menu
########################################## DOCKER_CONT ################################################
def remote_docker_container():
	os.system("clear")
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print('''
[1] RUN NEW COMMAND
[2] HELP
[3] RUN CONTAINER
[4] SHOW RUNNING CONTAINERS
[5] SHOW (RUNNING + STOPPED) CONTAINERS
[6] REMOVE ALL CONTAINERS
[7] START THE STOPPED CONTAINER
[8] RUN COMMAND IN CONTAINER WITHOUT GOING IN 
[9] CONTAINER IP
[10] CONTAINER DETAIL

[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("COMMAND : ")
			os.system(f"ssh {remote_main_menu.remoteIP} {inp}")
		elif i==2:
			inp=input("COMMAND DETAILS : ")
			os.system(f"ssh {remote_main_menu.remoteIP} man {inp}")
		elif i==3:
			os.system("clear")
			while True:
				remote_start.remote_start()
				os.system("tput setaf 10")
				print("[1] RUN NORMAL CONTAINER\n[2] RUN SPECIFIC CONTAINER\n\n[0] BACK\n[99] EXIT")
				os.system("tput setaf 15")
				inp=int(input("\nENTER CHOICE : "))
				if inp==1:
					inp=input("ENTER THE IMAGE_NAME:VERSION : ")
					os.system(f"ssh {remote_main_menu.remoteIP} docker run -dit {inp}")
				elif inp==2:
					st=f"ssh {remote_main_menu.remoteIP} docker run -dit"
					i=input("\nENTER CONTAINER NAME : ")
					st1 = st if i=='' else  st +"  --name "+i 
					i1=input("RUN CONTAINER IN BACKGROUND (if NO, press enter) : ")
					st2 = st1 if i1=='' else st1 +" -d "
					i2=input("ENTER THE NETWORK NAME ( host / null / your own network name / default ( press enter ) ) : ")
					st3 = st2 if i2=='' else st2 +" --network "+ i2
					i4=input("ENTER THE VOLUME NAME:PATH TO THE FOLDER (if NO, press enter) : ")	
					st4 = st3 if i4=='' else st3 + " -v "+i4
					i6=input("ENTER THE PORT TO RUN CONTAINER WITH PORT NATTING (if NO, press enter) : ")
					st6 = st4 if i6=='' else st4 + " -p "+i6
					i5=input("FOR LINKING ENTER THE CONTAINER NAME (if NO, press enter) : ")
					st5 = st6 if i5=='' else st6 + " --link " +i5
					i3=input("ENTER THE IMAGE NAME:VERSION : ")
					st5 = st5 +" " + i3
					
					os.system(st5)
					
				elif inp==0:
					remote_docker_container()
				elif inp==99:
					os.system("reset")
					exit()
				else:
					os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
					time.sleep(1)
				os.system("tput setaf 4")
				inp=input("enter to continue.......")
				os.system("tput setaf 15 && clear")
		elif i==4:
			os.system(f"ssh {remote_main_menu.remoteIP} docker container ps")
		elif i==5:
			os.system(f"ssh {remote_main_menu.remoteIP} docker ps -a")
		elif i==6:
			os.system(f"ssh {remote_main_menu.remoteIP} docker container rm -f $(ssh {remote_main_menu.remoteIP} docker container ls -q -a)")
		elif i==7:
			inp=input("ENTER THE CONTAINER NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker start {inp}")
			os.system("tput setaf 4 && echo -e 'CONTAINER STARTED' && tput setaf 15")
		elif i==8:
			inp=input("ENTER THE CONTAINER NAME (or ID) : ")
			inp1=input("ENTER THE COMMAND : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker exec {inp} {inp1}")
		elif i==9:
			inp=input("ENTER THE CONTAINER NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker container inspect  --format  '{{.NetworkSettings.IPAddress}}' "+ inp)
		elif i==10:
			inp=input("ENTER THE CONTAINER NAME :")
			os.system(f"ssh {remote_main_menu.remoteIP} docker container inspect {inp}")
		elif i==0:
			remote_main_menu.items()
		elif i==99:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue.......")
		os.system("tput setaf 15 && clear")


