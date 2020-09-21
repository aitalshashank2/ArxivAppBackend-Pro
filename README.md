# ArxApp Backend

This repository has the backend for ArxApp made as a submission for the course CSN-291, Indian Institute of Technology, Roorkee.

---

## Setup Guidelines

- Firstly, clone this repository on your local computer. Then, change directory.
	```
	git clone https://github.com/aitalshashank2/ArxivAppBackend.git
	cd ArxivAppBackend
	```
- Initialize a python virtual environment with the name ```.env```. For example you could use ```virtualenv```
	```
	virtualenv .env
	```

- Activate the virtual environment ```.env```
	```
	. .env/bin/activate
	```

- Check the versions of python and pip. The versions used in development are:
	```
	.../ArxivAppBackend$ python --version
	Python 3.8.2
	.../ArxivAppBackend$ pip --version
	pip 20.0.3 from ... (python 3.8)
	```

- Install all the necessary dependencies using
	```
	pip install -r requirements.txt
	```

- Set up a database in your MySQL Server for ArxivApp with the name ```ArxivAppDB```.
- Copy ```config-stencil.yml``` to ```config.yml``` and populate the values.

- Run migrations to integrate the database
	```
	python manage.py migrate
	```

- Check if ArxAppBackend is installed correctly
	```
	python manage.py runserver
	```

- Now, check if django development server is up and running on port 8000 on your local computer.
