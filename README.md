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
   	
 - Install Django with other requirements 

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

    - Bind gunicorn with wsgi to test the server:
      ```
      gunicorn --bind 0.0.0.0:8000 <folder_name_where_wsgi_file_exists>.wsgi # Example ecom.wsgi or myProject.wsgi
      ```	

 - Create a Gunicorn systemd Service File to start Django server on boot.
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
     User=yunus
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
	
 - Configure Nginx
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
		server_name <your_domain_name>.com www.<your_domain_name>.com;

		location = /favicon.ico { access_log off; log_not_found off; }
		location /static/ {
			alias /home/<user>/Desktop/staticRootFile/;
		}

		location / {
			include proxy_params;
			proxy_pass http://unix:/home/<user>/Desktop/<django_project_folder>/<your_socket_name>.sock;
		}

		location /media/ {
			alias   /home/<user>/Desktop/<django_project_folder>/<folder_name_like_your_django_project_folder>/media/;
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
 - Let Python and Nginx access the staticfile and Mediafile properly. Write these commands.
   ```
   sudo 777 -R staticfile
   sudo 777 -R mediafile
   ```
 - Install SSL in Server Nginx
   ```
   sudo apt-get install software-properties-common
   sudo add-apt-repository ppa:certbot/certbot
   sudo apt-get install python-certbot-nginx
   sudo ufw enable
   sudo ufw allow 'Nginx Full'
   sudo ufw delete allow 'Nginx HTTP'
   sudo certbot --nginx -d <your_domain_name>.com -d www.<your_domain_name>.com
   ```
   
   > If you are using **AWS** do not enable ***ufw***. AWS routing works as firewall.

	
# Tutorial Links
  - [SSL Installation Nginx with Django](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)
  - [Nginx + Django](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
  - [Nginx + Django](https://jee-appy.blogspot.com/2017/01/deply-django-with-nginx.html)
  - [Start Xampp on startup](https://salitha94.blogspot.com/2017/08/how-to-start-xampp-automatically-in.html)
	
	 
# Debugging Rules :


1. First stop nginx, gunicorn.
2. Start server using python3 manage.py runserver.
3. Fix what has gone wrong.
4. Start gunicorn and type : sudo systemctl status gunicorn.
5. If everything is ok, type : sudo systemctl start gunicorn and sudo systtemctl start nginx.
6. HTTP Port 80 must be forwarded in TCP. Or use Default HTTP port forward. 
7. Check if MySQL xampp database is up or not. Stop Xampp apache server.
8. Check if ufw has all port forwarding like Port 80 and 443.





























