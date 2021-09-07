# Getting it running
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
 

The Service
-----------

We would like to make the following calls against this web service using 
[curl](https://curl.haxx.se/)

The submitted result will be put through automated testing to verify the API
is working as expected.

### `/ping`

This is a simple health check that we can use to determine that the service is
running, and provides information about the application. The `"version"`
attribute in the response should match the version number in the `VERSION`
file.

```bash
$ curl -si http://localhost:8080/ping

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
  "name": "weatherservice",
  "status": "ok",
  "version": "1.0.0"
}
```

### `/forecast/<city>`

This endpoint allows a user to request a breakdown of the current weather for
a specific city. The response should include a description of the cloud cover,
the humidity as a percentage, the pressure in hecto Pascals (hPa), and
temperature in Celsius.

For example fetching the weather data for London should look like this:

```bash
$ curl -si http://localhost:8080/forecast/london/

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
    "clouds": "broken clouds",
    "humidity": "66.6%",
    "pressure": "1027.51 hPa",
    "temperature": "14.4C"
}
```

The endpoint should also take an `at` query string parameter that will
return the weather forecast for a specific date or datetime. The `at`
parameter should accept both date and datetime stamps in the [ISO
8601](https://en.wikipedia.org/wiki/ISO_8601) format. Ensure that your service
respects time zone offsets.

```bash
$ curl -si http://localhost:8080/forecast/london/?at=2018-10-14T14:34:40+0100

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
    "clouds": "sunny",
    "humidity": "12.34%",
    "pressure": "1000.51 hPa",
    "temperature": "34.4C"
}

$ curl -si http://localhost:8080/forecast/london/?at=2018-10-14

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{
    "clouds": "overcast",
    "humidity": "20.6%",
    "pressure": "1014.51 hPa",
    "temperature": "28.0C"
}
```

### Errors

When no data is found or the endpoint is invalid the service should respond
with `404` status code and an appropriate message:

```bash
$ curl -si http://localhost:8080/forecast/westeros

HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8
{
    "error": "Cannot find country 'westeros'",
    "error_code": "country_not_found"
}
```

Similarly invalid requests should return a `400` status code:

```bash
$ curl -si http://localhost:8080/forecast/london?at=1938-12-25

HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=utf-8
{
    "error": "Date is in the past",
    "error_code": "invalid date"
}
```

If anything else goes wrong the service should response with a `500` status code
and a message that doesn't leak any information about the service internals:

```bash
$ curl -si http://localhost:8080/forecast/london

HTTP/1.1 500 Internal Server Error
Content-Type: application/json; charset=utf-8
{
    "error": "Something went wrong",
    "error_code": "internal_server_error"
}
```




















