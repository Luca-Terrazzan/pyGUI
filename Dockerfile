FROM python

COPY . .

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "zsh"]
RUN ["apt-get", "install", "-y", "vim"]
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN pip install -r requirements.txt
