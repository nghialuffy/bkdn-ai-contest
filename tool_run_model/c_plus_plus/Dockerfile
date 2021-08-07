#Update ubuntu
FROM ubuntu:18.04

# =========
# TIME_ZONE
# =========
ENV TZ=US
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ==========
# PACKAGE
# ==========
RUN apt-get update && apt-get install -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y zlib1g-dev curl nano nodejs npm
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev xvfb
RUN apt update && apt install -y python3-pip python3-dev ssh python-boto3
RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install -y
RUN apt-get -qq install -y gcc crudini python python-dev libffi-dev python-virtualenv python-setuptools libjpeg-dev zlib1g-dev
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python get-pip.py

# INSTALL JAVA
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get install -y ant && \
    apt-get clean;
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

ENV APP_PATH /home
WORKDIR $APP_PATH

COPY tool $APP_PATH/tool
# ====================
# INSTALL REQUIREMENTS
# ====================
COPY ./requirements3.txt $APP_PATH/requirements3.txt
RUN pip3 install --no-cache-dir -r requirements3.txt

COPY ./requirements2.txt $APP_PATH/requirements2.txt
RUN pip2 install --no-cache-dir -r requirements2.txt
# ==========
# RUN SCRIPT
# ==========
COPY start.sh $APP_PATH
RUN chmod a+x $APP_PATH/start.sh
ENTRYPOINT ["/home/start.sh"]