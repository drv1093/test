(requirements.txt contains Pandas
Pyarrow, and other libraries.)

FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3","demo.py" ]

docker build -t demo_csv .
docker run -v /home/ubuntu/drv236:/app demo_csv
