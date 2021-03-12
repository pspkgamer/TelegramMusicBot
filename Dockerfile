
FROM nikolaik/python-nodejs:python3.9-nodejs15-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install -yqq \
        python3-pip \
        git \
        ffmpeg && \
    git clone https://github.com/sangramghangale47/TelegramMusicBot && \
    cd TelegramMusicBot && \
    git clone https://github.com/pytgcalls/pytgcalls/tree/65d718472d058b8a0b7c5e70cbb27ffcb660a409 && \
    cd pytgcalls && \
    npm install && \
    npm run prepare && \
    cd pytgcalls/js && \
    npm install && \
    cd ../../ && \
    pip3 install -r requirements.txt && \
    cp -r ./pytgcalls /TelegramMusicBot/ && \
    cd /TelegramMusicBot && \
    pip3 install -U -r requirements.txt

WORKDIR /TelegramMusicBot
CMD ["python3" "main.py"]
