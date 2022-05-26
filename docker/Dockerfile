FROM nimmis/ubuntu:18.04

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

# set default java environment variable
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=111 \
    JAVA_HOME=/usr/lib/jvm/default-jvm \
    PATH=${PATH}:/usr/lib/jvm/default-jvm/bin/


RUN add-apt-repository ppa:openjdk-r/ppa -y && \
    # update data from repositories
    apt-get update && \
    # upgrade OS
    apt-get -y dist-upgrade && \
    # Make info file about this build
    printf "Build of nimmis/java:openjdk-8-jdk, date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/java && \
    # install application
    apt-get install -y --no-install-recommends openjdk-8-jdk && \
    # fix default setting
    ln -s java-8-openjdk-amd64  /usr/lib/jvm/default-jvm && \
    # remove apt cache from image
    apt-get clean all

RUN java -version && \
    javac -version

# Install linux packages
RUN apt-get update
RUN apt-get -qq -y install git curl build-essential subversion perl wget unzip vim

RUN apt install -y python3-pip

RUN apt-get install bc

WORKDIR /root

# D4J Setup
COPY resources/install_defects4j.sh install_defects4j.sh
RUN chmod +x install_defects4j.sh
RUN ./install_defects4j.sh
ENV PATH="${PATH}:/root/defects4j/framework/bin"

RUN python3.6 -m pip install tqdm tabulate
RUN python3.6 -m pip install numpy scipy pandas
RUN python3.6 -m pip install torch==1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu


ENV TZ="America/Los_Angeles"
ENV D4J_HOME="/root/defects4j"
ENV PATH="${PATH}:/root/defects4j/framework/bin"
ENV JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8"

ENV TMP_DIR="/tmp"
ENV COVERAGE_DIR="/root/coverage"
RUN mkdir /root/coverage

ENV PYTHONIOENCODING=utf-8
