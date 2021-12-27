# scheduler_api
- Make to have Docker and Docker Compose already installed.
- Run `docker-compose up --build` to fetch all dependencies and get project built.
- API should be accessible via "http://localhost:8000/api" if the project gets built successfully
- The Database System used for this project is PostgreSQL, a PGAdmin Service has beed attached and can be access via "http://localhost:5050". The master user details require to login to PGAdmin can be read from the docker-compose.yml file
- Run `docker-compose down` may be run to bring down all containers, the `-v` option may be added to delete all volume, however this option should be used with caution to avoid loss of database
