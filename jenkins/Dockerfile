FROM jenkins/jenkins:lts

USER root

# Install Python + pip + other needed tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip git curl && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
