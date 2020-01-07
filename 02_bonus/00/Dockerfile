FROM python:3

ADD amazonApp.py /

RUN pip3 install --user requests &&\
    pip3 install --user bs4

CMD [ "python3", "./amazonApp.py" ]  

## ------ Usage --------
# docker build -t bonus00 .
# docker run -t bonus00