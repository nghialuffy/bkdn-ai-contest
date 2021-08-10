# How to run

## install docker:
```bash
sudo apt install -y docker.io
sudo docker -v
```

## install docker-compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

## build image
```bash
sudo docker-compose build
```

## create docker swarm

```bash
sudo docker swarm init --advertise-addr 127.0.0.1
```

## deploy portainer to control

```bash
sudo docker stack deploy --compose-file docker-compose.yml portainer 
```

link portainer: http://127.0.0.1:9000

## deploy tool

```bash
sudo docker stack deploy --compose-file docker-compose.yml tool
```

## ref:
https://code.viblo.asia/helps