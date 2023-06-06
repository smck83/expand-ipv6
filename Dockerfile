FROM debian:stable
LABEL maintainer="s@mck.la"
ARG MY_APP_PATH=/opt/expand-ipv6

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp python3 pip \
    && mkdir -p ${MY_APP_PATH}

ADD main.py run.py ${MY_APP_PATH}
RUN pip3 install fastapi uvicorn["standard"]
WORKDIR ${MY_APP_PATH}


VOLUME [${MY_APP_PATH}]

ENTRYPOINT /usr/bin/python3 -u run.py

EXPOSE 8000/tcp
