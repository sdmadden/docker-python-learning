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

# Web
View site
`http://localhost:5000`
