import os
import subprocess as sp
import time
import remote_start
import remote_main_menu
########################################## DOCKER COMPOSE #############################################
def remote_docker_compose():
	os.system("clear")
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print('''
[1] INSTALL DOCKER COMPOSE
[2] MAKE A NEW FILE
[3] SEE COMPOSE FILE
[4] RUN PREMADE CONTAINER

[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			os.system(f'ssh {remote_main_menu.remoteIP} curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && ssh {remote_main_menu.remoteIP} chmod +x /usr/local/bin/docker-compose')
		elif i==2:
			inp=input("ENTER THE FOLDER NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} mkdir /root/{inp}") 
			os.system(f"ssh {remote_main_menu.remoteIP} touch /root/{inp}/docker-compose.yml")
		elif i==3:
			inp=input("ENTER THE FILE PATH : ")
			os.system(f"ssh {remote_main_menu.remoteIP} gedit {inp}/docker-compose.yml")
		elif i==4:
			while True:
				remote_start.remote_start()
				os.system("tput setaf 10 && echo -e '[1] WORDPRESS CONTAINER\n[2] OWNCLOUD CONTAINER\n[3] NGINX SERVER\n[4] PHP\n\n[0] BACK\n[99] EXIT' && tput setaf 15")
				inp=int(input("\nCHOICE : "))
				if inp == 1: 
					inp1=input("ENTER THE PATH TO SAVE : ")
					os.system(f"echo -e '''\
version: \"3\"\n\
services:\n\
  dbos:\n\
    image: mysql:5.7\n\
    environment:\n\
      MYSQL_ROOT_PASSWORD: nfsmw\n\
      MYSQL_USER: milind\n\
      MYSQL_PASSWORD: nfsmw\n\
      MYSQL_DATABASE: mydb\n\
    volumes:\n\
      - mysql_storage_new:/var/lib/mysql\n\
    restart: always\n\
\n\
  wpos:\n\
    image: wordpress:5.1.1-php7.3-apache\n\
    restart: always\n\
    environment:\n\
      WORDPRESS_DB_HOST: dbos\n\
      WORDPRESS_DB_USER: milind\n\
      WORDPRESS_DB_PASSWORD: redhat\n\
      WORDPRESS_DB_NAME: mydb\n\
    volumes:\n\
      - wp_storage_new:/var/www/html\n\
    ports:\n\
      - 8081:80\n\
    depends_on:\n\
      - dbos\n\
\n\
volumes:\n\
  wp_storage_new:\n\
  mysql_storage_new:''' | ssh {remote_main_menu.remoteIP} -T 'cat > {inp1}/docker-compose.yml' && ssh -t {remote_main_menu.remoteIP} 'cd {inp1};docker-compose up'")
				elif inp==2:
					 
					inp1=input("ENTER THE PATH TO SAVE : ")
					os.system(f"echo -e '''\
version: \"3\"\n\
services:\n\
  dbos:\n\
    image: mysql:5.7\n\
    environment:\n\
      MYSQL_ROOT_PASSWORD: nfsmw\n\
      MYSQL_USER: milind\n\
      MYSQL_PASSWORD: nfsmw\n\
      MYSQL_DATABASE: mydb\n\
    volumes:\n\
      - mysql_storage_new:/var/lib/mysql\n\
    restart: always\n\
  owncloud:\n\
    image: owncloud\n\
    restart: always\n\
    volumes:\n\
      - owncloud_server:/var/www/html\n\
    ports:\n\
      - 8080:80\n\
    depends_on:\n\
      - dbos\n\
volumes:\n\
  owncloud_server:\n\
  mysql_storage_new:''' | ssh {remote_main_menu.remoteIP} -T 'cat > {inp1}/docker-compose.yml' && ssh -t {remote_main_menu.remoteIP} 'cd {inp1};docker-compose up'")
				elif inp==3:
					inp1=input("ENTER THE PATH TO SAVE : ")
					os.system(f"echo -e '''\
version: \"3\"\n\
services:\n\
  server:\n\
    image: nginx\n\
    ports:\n\
      - 8000:80\n\
    volumes:\n\
      - nginx_storage_new:/var/www/html\n\
    restart: always\n\
volumes:\n\
  nginx_storage_new:''' | ssh {remote_main_menu.remoteIP} -T 'cat > {inp1}/docker-compose.yml' && ssh -t {remote_main_menu.remoteIP} 'cd {inp1};docker-compose up'")
				elif inp==4:
					inp1=input("ENTER THE PATH TO SAVE : ")
					os.system(f"echo -e '''\
version: \"3\"\n\
services:\n\
  php:\n\
    image: mysql:5.7\n\
    build:\n\
    expose:\n\
      - 9000\n\
    volumes:\n\
      - ./php/www:/var/www/html\n\
    restart: always\n\
  apache:\n\
    image: web:v1\n\
    args:\n\
      - PHP_SOCKET: php:9000\n\
    volumes:\n\
      - ./php/www:/var/www/html\n\
    ports:\n\
      - 80:80\n\
      - 443:443\n\
    links:\n\
      -php''' | ssh {remote_main_menu.remoteIP} -T 'cat > {inp1}/docker-compose.yml' && ssh -t {remote_main_menu.remoteIP} 'cd {inp1};docker-compose up'")
				elif inp==0:
					remote_docker_compose()
				elif inp==99:
					os.system("reset")
					exit()
				else:
					os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
					time.sleep(1)
				os.system("tput setaf 4")
				inp=input("enter to continue.......")
				os.system("tput setaf 15 && clear")
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

