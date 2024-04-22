FROM kalilinux/kali-rolling

RUN apt-get update
RUN apt-get install -y exploitdb

WORKDIR /root

CMD ["/bin/bash"]
