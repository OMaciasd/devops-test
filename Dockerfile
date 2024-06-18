ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine

WORKDIR /app

LABEL Name="MiApp" \
      Version="1.0"

COPY myapp /app/myapp

ENV PYTHONPATH /app
RUN pip install --upgrade pip \
      && pip install --upgrade --no-cache-dir -r /app/myapp/requirements.txt \
      && rm -rf /var/cache/apk/*

EXPOSE 5000

CMD ["python", "-m", "myapp"]
