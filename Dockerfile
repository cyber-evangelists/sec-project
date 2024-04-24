FROM kalilinux/kali-rolling

RUN apt-get update
RUN apt-get install -y exploitdb
RUN apt-get install -y python3
WORKDIR /root


