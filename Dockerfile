FROM python:3-alpine

LABEL Description="Test HTTP Web Server App" Vendor="github.com/zeph1rus" Version="0.1.5"
WORKDIR /usr/src/app

COPY ci_environment.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "./ci_environment.py" ]
