FROM docker:19.03.12
LABEL Description="Test HTTP Web Server App" Vendor="github.com/zeph1rus" Version="0.1.5"
WORKDIR /usr/src/app
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
COPY ci_environment.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "./ci_environment.py" ]