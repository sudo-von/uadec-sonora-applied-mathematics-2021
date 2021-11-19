FROM python:3.7-slim
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        make \
        gcc
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt       
ENTRYPOINT ["python"]
CMD ["main.py"]