FROM python:3.10.4

RUN apt update

RUN apt install socat -y

RUN useradd -m usero

ADD chall.py /home/usero/chall.py

RUN chmod 500 /home/usero/chall.py

RUN chown -R usero:root /home/usero

USER usero

WORKDIR /home/usero

RUN pip install pycryptodome --user

CMD socat TCP-L:13373,fork EXEC:"python3 ./chall.py",reuseaddr,stderr
