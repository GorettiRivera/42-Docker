FROM debian

RUN apt-get update && apt-get install -y cowsay fortune lolcat

ENTRYPOINT /usr/games/fortune | /usr/games/cowsay | /usr/games/lolcat


## ------ Usage --------
# docker build -t bonus04 .
# docker run --rm -t bonus04
