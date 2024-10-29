FROM jenkins/jenkins:2.452.2-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
# RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
# https://download.docker.com/linux/debian/gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) \
#   signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
#   https://download.docker.com/linux/debian \
#   $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
# RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install -y pip
RUN apt install -y python3.11-venv
RUN apt install wget -y
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/libu/libu2f-host/libu2f-udev_1.1.4-1_all.deb
RUN dpkg -i libu2f-udev_1.1.4-1_all.deb
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install xdg-utils -y
RUN apt install libxkbcommon-x11-0 -y
RUN apt-get install libxdamage1 -y
RUN apt-get install libvulkan1 -y
RUN apt-get install libpangocairo-1.0-0 -y
RUN apt-get install libnss3-dev -y
RUN apt-get install libasound2 -y
RUN apt-get install libatk1.0-0 -y
RUN apt-get install libglib2.0-dev -y
RUN apt-get install fonts-liberation -y
RUN echo "deb http://deb.debian.org/debian bookworm-backports main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install libatspi2.0-0 -y
RUN apt-get install libatk-bridge2.0-0 -y
RUN apt-get install libcups2 -y
RUN apt install libgtk-3-dev -y
RUN apt-get install libgtk-4-1 -y
# RUN dpkg -i google-chrome-stable_current_amd64.deb
ADD google-chrome-stable_current_amd64.deb google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb

########
#RUN apt-get install unzip
#RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1IawpLza0dw1UbS8-87yyXuCHR9ZRIewq' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1IawpLza0dw1UbS8-87yyXuCHR9ZRIewq" -O _data.zip && rm -rf /tmp/cookies.txt
#RUN ls -lht
#RUN mkdir /tmp/_data
#RUN unzip _data.zip -d /tmp/_data/
#RUN cp -r /tmp/_data/_data/* /var/jenkins_home/
#RUN rm _data.zip 
#RUN rm -rf /tmp/_data/
########

USER jenkins
# RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"