FROM python:3.11-alpine

#RUN mkdir /tg_bot
#WORKDIR /tg_bot
#COPY main.py /tg_bot/
#COPY requirement.txt /tg_bot
#RUN pip install -r /tg_bot/requirement.txt
#ENTRYPOINT ["python3", "main.py"]
#
#ENV API_TOKEN=5935641446:AAFYXxw4IuVwChnDElESEWazcm81nDINSBc

RUN mkdir /
WORKDIR /
COPY main1.py /
COPY requirement.txt /