#execute on home directory on new install of wsl debian
sudo apt update && sudo apt install curl -y && sudo apt install python3 -y && sudo apt install python3-pip -y && sudo apt-get install python3-venv 
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
source $HOME/.poetry/env
sudo ln -s /usr/bin/python3.7 /usr/bin/python

#executar no wls 
poetry install