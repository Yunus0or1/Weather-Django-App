# Django Production Server Host
 - Install Python using this command :
   ```
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install python3
   sudo apt-get install -y python3-pip
   ```

 - Install Virtual Environment 
   ```
   sudo apt-get install virtualenv
   OR
   sudo apt-get install python3-virtualenv
   ```
   	
 **Install Django with other requirements**

   - Create a virtualenv inside the Django Project folder or where you want : 
     ```
     virtualenv -p python3 django_env
     ```
   - Activate it (Linux)
     ```
     source django_env/bin/activate
     ```
	
     > Regardless of which version of Python you are using, when the virtual environment is activated, you should use the pip command (not pip3).
    
   - When you are in Virtual Environment install Django and other libraries :	
     ```
     pip install -r requirements.txt
     ```

   - You must create the .env file inside the project folder and run these commands:	
     ```
     sudo touch .env
	 sudo chmod a+rwx .env
	 echo "DEBUG=False" >> .env
	 echo "SECRET_KEY=YOUR_SECRET_KEY" >> .env (Do not add !, #, / character in SECRET_KEY when using this command)
	 echo "WEATHER_API_KEY=YOUR_WEATHER_API_KEY" >> .env
     ```

   - Bind gunicorn with wsgi to test the server:
     ```
     gunicorn --bind 0.0.0.0:8000 <folder_name_where_wsgi_file_exists>.wsgi # Example ecom.wsgi or myProject.wsgi
     ```	

 - **Create a Gunicorn systemd Service File to start Django server on boot**
   - Type this command.
     ```
     sudo nano /etc/systemd/system/gunicorn.service
     ```
   - Copy paste these lines and set **project locations** according to your config :
     ```
     [Unit]
     Description=gunicorn daemon
     After=network.target
     [Service]
     User=<user>
     Group=www-data
     WorkingDirectory=/home/<user>/Desktop/<django_project_folder>
     ExecStart=/home/<user>/Desktop/<django_project_folder>/django_env/bin/gunicorn --access-logfile - --workers 3 --timeout 300 --bind unix:/home/<user>/Desktop/<django_project_folder>/<any_name>.sock <django_project_folder>.wsgi:application
     [Install]
     WantedBy=multi-user.target
     #<any_name>.sock will be created automatically
     ```
   - Now write these.
     ```
     sudo systemctl start gunicorn
     sudo systemctl enable gunicorn
     ```
     
     > Next, check for the existence of the <any_name>.sock file within your project directory
	
 - **Configure Nginx**
   - Install it 
     ```
	 sudo fuser -k 80/tcp
	 sudo fuser -k 443/tcp
     sudo apt-get install nginx
     ```
   - Create a coniguration file using this command with the any name.
     ```
     sudo nano /etc/nginx/sites-available/<file_name>
     ```
   - Copy-paste these and change location according to your config :
     ```
     server {
		server_name IP_ADDRESS;

		location = /favicon.ico { access_log off; log_not_found off; }

		location / {
			include proxy_params;
			proxy_pass http://unix:/home/<user>/Desktop/<django_project_folder>/<your_socket_name>.sock;
		}

	 }
     ```
   - Run this command to enable that site.
     ```
     sudo ln -s /etc/nginx/sites-available/<your_nginx_file_name_for_that_project> /etc/nginx/sites-enabled
     ```
   - Test your Nginx configuration for syntax errors by typing.
     ```
     sudo nginx -t
     ```
   - Go to **/etc/nginx/** and delete **Defualt** from both sites-enabled and sites-available
		
   - Now write these commands.
     ```
     sudo systemctl restart nginx
     ```
	 
	 

***YOU DO HAVE A FULL RUNNING DJANGO SERVER***
 






















