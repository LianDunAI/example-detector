# syntax=docker/dockerfile:1

FROM ubuntu:24.10

ENV APP_ROOT=/detector-serve
WORKDIR ${APP_ROOT}

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv venv
ENV PATH="${APP_ROOT}/venv/bin:${PATH}"

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# install app
COPY *.py .
COPY *.json .

# run the app
EXPOSE 8080
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8088"]
