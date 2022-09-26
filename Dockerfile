FROM python:3.10
LABEL author='NitinSachdev'

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Environment
RUN apt-get update
RUN apt-get install -y netcat
RUN apt-get install -y bash vim nano postgresql-client
RUN pip install --upgrade pip

# Major pinned python dependencies
RUN pip install --no-cache-dir flake8==3.8.4 uWSGI

# Regular Python dependencies
COPY requirements.txt /app/

# Copy our codebase into the container
COPY entrypoint.sh /app/

COPY . /app/

# Ops Parameters
# run entrypoint.sh

ENV WORKERS=2
ENV PORT=8000
EXPOSE ${PORT}

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh", "db"]

CMD uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module autocompany.wsgi:application

