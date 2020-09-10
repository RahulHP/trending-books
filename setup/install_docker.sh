#!/usr/bin/env bash
# https://docs.docker.com/engine/install/ubuntu/
# Uninstall old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install using the repository
# Set up the repository
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Test docker installation
sudo docker run hello-world


# https://docs.docker.com/engine/install/linux-postinstall/
sudo usermod -aG docker $USER
newgrp docker