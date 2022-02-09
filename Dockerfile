# Pull base image
FROM python:3.7

ENV PROJECT_DIR /usr/src/asteroid_strike
WORKDIR ${PROJECT_DIR}
COPY . .
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

EXPOSE 5000

CMD ["python", "app/api.py"]