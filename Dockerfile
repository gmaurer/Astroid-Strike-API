# Pull base image
FROM python:3.9

ENV PROJECT_DIR /web/app/asteroid_strike
WORKDIR ${PROJECT_DIR}
COPY . .
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

EXPOSE 5000

CMD ["python", "api.py"] 