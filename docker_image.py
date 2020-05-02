import os
import subprocess as sp
import time
import start
import main_menu
########################################## DOCKER_IMAGE ###############################################
def docker_image():				
	os.system("clear")
	while True:
		start.start()
		os.system("tput setaf 10")
		print(''' 
[1] RUN NEW COMMAND 
[2] COMMIT CONTAINER 
[3] SHOW ALL IMAGES
[4] REMOVE IMAGE
[5] PULL IMAGES 
[6] PUSH IMAGES TO REGISTRY
[7] SHARE IMAGE

[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("ENTER COMMAND : ")
			os.system(f"{inp}")
		elif i==2:
			inp=input("ENTER THE CONTAINERNAME : ")
			inp1=input("ENTER THE IMAGENAME WITH VERSION : ")
			os.system(f"docker commit {inp} {inp1}")
		elif i==3:
			os.system("docker image ls")
		elif i==4:
			inp=input("ENTER IMAGE NAME : ")
			os.system(f"docker image rmi {inp}")
		elif i==5:
			inp=input("ENTER THE IMAGE NAME : ")
			os.system(f"docker pull {inp}") 
		elif i==6:
			inp=input("ENTER IMAGENAME:VERSION : ")
			inp1=input("ENTER YOUR DOCKER ID : ")
			os.system("docker login")
			os.system(f"docker tag {inp} {inp1}/{inp} && docker push {inp1}/{inp}")
		elif i==7:
			inp=input("ENTER IMAGENAME:VERSION : ")
			inp1=input("ENTER THE SHAREABLE NAME (with extension .tar) : ")
			inp2=input("ENTER THE IP ADDRESS : ")
			inp3=input("ENTER THE DESTINATION FOLDER PATH : ")
			output=sp.getoutput(f"nmap -sT {inp2} | grep ^H | cut -c 1-4")
			if "Host" in output:
				os.system(f"docker save {inp} -o {inp1}")
				os.system(f"scp {inp1} root@{inp2}:{inp3}")
				os.system("tput setaf 4 && echo -e 'ACTION COMPLETED , GO TO DESTINATION MACHINE TO LOAD IMAGE' && tput setaf 15")		  
			else:
				os.system("tput setaf 9 && echo -e 'ACTION NOT COMPLETED , ETIEHR HOST IS NOT UP ,CHECK YOUR CONNECTION !!!' && tput setaf 15")		
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

