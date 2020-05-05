# 42-Docker

The aim of the Docker-1 project is to make you handle docker and docker-machine, the bases to understand the idea of containerization of services. You can see this project as
an initiation.

## 1. How to Docker (00_how_to_docker):
In this first part you will be introduced to Docker and its main options

## 2. Dockerfiles (01_dockerfiles):
Docker makes it possible to create yourself OWN containers for your OWN applications!  Dockerfiles use a specific syntax that reuses a base image or an existing container to add your own dependencies and your own files.

## 3. Bonus (02_bonus):
Now we can create our future work environments, such as:
* Python
* Golang
* C


# Docker Installation:

### What is Docker?
https://tinyurl.com/yac98tgc


### 1. Install homebrew:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

### 2. Install docker
brew install docker

### 3. Install docker-machine
brew install docker-machine

### 4. Install VirtualBox
brew cask install virtualbox

### Useful commands:
- List available machines
docker-machine ls

- Create a new virtual machine
docker-machine create --driver virtualbox default

- Run the following command to tell the Docker ‘which machine’ to execute docker command to:
docker-machine env default

- Connect your shell to the new machine
eval $(docker-machine env default)


Source: https://tinyurl.com/yjzesbc7

# Stuff:
### Creating an Ubuntu Docker Image
Refer step 4 onwards : https://tinyurl.com/y24z2357 

### How to open multiple terminals in docker?
- Open a docker terminal
- Get the image running as a container in the background: docker run -d -it <image_id>

Tip: docker ps will show the container_id that you just fired up from said image.
- docker exec -it <container_id> bash
		Now your docker terminal is showing an interactive terminal to the container.
- Open up another docker terminal and perform step 3 to create another interactive terminal to the container. (Rinse and Repeat)


### How to install vim in Linux
apt-get update && apt-get install vim -y 

### Committing Changes in a Container to a Docker Image
docker commit -m "What you did to the image" -a "Author Name" container_id repository/new_image_name

Example:
docker commit -m "installed vim" -a "MGRM" 16ff6774e0c9 mariagore/ubuntu-vim
