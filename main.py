import os
import subprocess as sp
import time
import start
import remote_main_menu
import main_menu

def main():
	count=0
	while count <= 2:
		start.start()
		os.system("tput setaf 4")
		print('LOCATION [ LOCAL / REMOTE ] : ',end='')
		os.system("tput setaf 15")
		i=input()
		if i.lower()=='local':	
			main_menu.main_menu()
		elif i.lower()=='remote':
			remote_main_menu.remote_main_menu()
		else:
			os.system("tput setaf 9  && echo -e 'OPTION NOT SUPPORTED' && tput setaf 15")
			time.sleep(1)
			count+=1
	
	if count>2:
		os.system("tput setaf 9 && echo -e 'TRIAL EXCEEDED THE LIMIT !!!'")
		time.sleep(1)
		os.system("reset")		
		exit()
########################################### IF NAME == MAIN ############################################
if __name__ =='__main__':
	main()
