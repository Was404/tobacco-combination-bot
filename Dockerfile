FROM python:alpine

WORKDIR /tg_bot_tobacco

COPY . /tg_bot_tobacco

RUN pip3 install -r requirements.txt

EXPOSE 8443

CMD [ "python3", "app.py" ]