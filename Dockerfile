FROM python3.10
RUN mkdir /app
WORKDIR /app
COPY src/* app/