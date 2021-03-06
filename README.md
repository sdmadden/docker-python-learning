# Virtual Environment
Make a virtual environment
```bash
python3.9 -m venv .venv
```

Activate the virtual environment
```bash
source .venv/bin/activate
```

Deactivate the virtual environment
```bash
deactivate
```

# Docker
Build docker image
```bash
sudo docker build -t flask-test .
```

Run docker container from image
```bash
sudo docker run -d -v "$(pwd)"/app:/app -p 5000:5000 --name flask-test flask-test
```

Restart docker container
```bash
sudo docker restart flask-test
```

Remove all stopped containers
```bash
#sudo docker rm $(sudo docker ps -a -q)
sudo docker container prune
```

Remove all dangling images
```bash
#sudo docker rmi $(sudo docker images -f "dangling=true" -q)
sudo docker image prune
```

Run bash in docker container
```bash
sudo docker exec -it flask-test bash
```

# Docker Compose
Start docker-compose
`sudo docker-compose up -d`

Start docker-compose in dev
`sudo docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d`

Stop docker-compose in dev
`sudo docker-compose -f docker-compose.yml -f docker-compose.dev.yml down`

Rebuild container
`sudo docker-compose up -d --build web`

# Web
View site
`http://localhost:5000`

# PGAdmin
View site
`http://localhost:5454`

Make sure to connect to database on `db.hostname` from `docker-compose.yml`
`postgres-host`

# Environment Variables
## Set in environment running docker
Can be set in `/etc/environment` to persist through restarts
```bash
FLASK_APP_PGADMIN_DEFAULT_EMAIL=user@domain.com
FLASK_APP_PGADMIN_DEFAULT_PASSWORD=password
FLASK_APP_POSTGRES_USER=user
FLASK_APP_POSTGRES_PASSWORD=password
FLASK_ENV=development
```

## Loaded into Flask app
Default settings from `app/settings/default_settings.cfg`

Environment specific settings from `app/settings/environment_settings.cfg` will override any default settings.

Need to restart flask container (`sudo docker restart flask`) to pick up setting changes