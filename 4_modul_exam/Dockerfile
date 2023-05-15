FROM python:3.11-alpine

WORKDIR /apps
COPY . /apps

ENV TOKEN=my_value
RUN pip install -r requirement.txt

ENTRYPOINT ["python", "exam.py"]
