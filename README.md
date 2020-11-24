# ArxApp Backend

This repository has the backend for ArxApp made as a submission for the course CSN-291, Indian Institute of Technology, Roorkee.

## Setup Guidelines

- Firstly, clone this repository on your local computer. Then, change directory.
	```bash
	git clone https://github.com/aitalshashank2/ArxivAppBackend-Pro.git
	cd ArxivAppBackend
	```

- Clone the frontend web repository to the ```frontend/``` directory
	```bash
	cd frontend
	git clone https://github.com/ShreyasTheOne/arxiv-app-frontend-web.git
	```

- Copy ```code/configuration/config-stencil.yml``` to ```code/configuration/config.yml``` and populate the values.

- Build the **docker images**
	```bash
	cd ..
	docker-compose build
	```

- Start the project
	```bash
	docker-compose up -d
	```

- Now, visit `http://localhost:54321` to view the Project.

## Happy Research!
